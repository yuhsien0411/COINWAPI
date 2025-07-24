"""
CoinW 合約 API HTTP 管理器

專門處理合約API的HMAC SHA256簽名認證
"""

import time
import json
import hmac
import hashlib
import base64
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ..exceptions import (
    CoinWAPIError,
    NetworkError,
    InvalidCredentialsError,
    RateLimitError,
    handle_api_error
)


@dataclass
class ContractHTTPConfig:
    """合約HTTP配置"""
    base_url: str = "https://api.coinw.com"
    timeout: int = 30
    max_retries: int = 3
    logging_level: int = logging.INFO


class _ContractHTTPManager:
    """
    CoinW 合約 API HTTP管理器
    
    使用HMAC SHA256簽名，與現貨API的MD5簽名不同
    """
    
    def __init__(
        self,
        api_key: str,
        secret_key: str,
        config: Optional[ContractHTTPConfig] = None
    ):
        self.api_key = api_key
        self.secret_key = secret_key
        self.config = config or ContractHTTPConfig()
        
        # 設定日誌
        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                )
            )
            handler.setLevel(self.config.logging_level)
            self.logger.addHandler(handler)
        
        self.logger.debug("初始化合約HTTP會話")
        
        # 初始化HTTP會話
        self.client = requests.Session()
        self.client.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'CoinW-Contract-Python-API/0.2.0'
        })
        
        # 設定重試策略
        retry_strategy = Retry(
            total=self.config.max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST", "DELETE", "PUT"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.client.mount("http://", adapter)
        self.client.mount("https://", adapter)
        
        self.base_url = self.config.base_url.rstrip('/')
    
    def _generate_signature(self, method: str, api_url: str, params: Dict[str, Any], timestamp: str) -> str:
        """
        生成HMAC SHA256簽名
        
        Args:
            method: HTTP方法
            api_url: API路徑
            params: 請求參數
            timestamp: 時間戳
            
        Returns:
            Base64編碼的簽名
        """
        if not self.api_key or not self.secret_key:
            raise InvalidCredentialsError("合約API需要API密鑰和secret密鑰")
        
        # 根據不同請求方法構建簽名字符串
        if method.upper() == "GET":
            # GET請求：將參數轉換為查詢字符串
            query_params = "&".join(f"{key}={value}" for key, value in params.items() if value is not None)
            if query_params:
                encoded_params = f'{timestamp}{method}{api_url}?{query_params}'
            else:
                encoded_params = f'{timestamp}{method}{api_url}'
        else:
            # POST/PUT/DELETE請求：使用JSON body
            json_body = json.dumps(params) if params else ""
            encoded_params = f'{timestamp}{method}{api_url}{json_body}'
        
        # 生成HMAC SHA256簽名
        signature = base64.b64encode(
            hmac.new(
                bytes(self.secret_key, 'utf-8'),
                msg=bytes(encoded_params, 'utf-8'),
                digestmod=hashlib.sha256
            ).digest()
        ).decode("US-ASCII")
        
        self.logger.debug(f"簽名字符串: {encoded_params}")
        self.logger.debug(f"生成簽名: {signature[:20]}...")
        
        return signature
    
    def _submit_request(
        self,
        method: str = "GET",
        path: str = "",
        query: Optional[Dict[str, Any]] = None,
        auth: bool = False
    ) -> Dict[str, Any]:
        """
        提交請求到合約API
        
        Args:
            method: HTTP方法
            path: API路徑
            query: 查詢參數
            auth: 是否需要認證
            
        Returns:
            API響應數據
            
        Raises:
            相應的異常類型
        """
        if query is None:
            query = {}
        
        url = f"{self.base_url}{path}"
        
        # 記錄請求信息
        self.logger.debug(f"提交合約請求: {method} {url}")
        self.logger.debug(f"參數: {query}")
        
        try:
            headers = {}
            
            if auth:
                # 生成時間戳
                timestamp = str(int(time.time() * 1000))
                
                # 生成簽名
                signature = self._generate_signature(method, path, query, timestamp)
                
                # 設置認證頭
                headers.update({
                    "sign": signature,
                    "api_key": self.api_key,
                    "timestamp": timestamp,
                })
            
            if method.upper() == "GET":
                # GET請求
                response = self.client.get(
                    url,
                    params=query,
                    headers=headers,
                    timeout=self.config.timeout
                )
            else:
                # POST/PUT/DELETE請求
                if auth:
                    headers["Content-type"] = "application/json"
                
                data = json.dumps(query) if query else "{}"
                
                if method.upper() == "POST":
                    response = self.client.post(
                        url,
                        data=data,
                        headers=headers,
                        timeout=self.config.timeout
                    )
                elif method.upper() == "DELETE":
                    response = self.client.delete(
                        url,
                        data=data,
                        headers=headers,
                        timeout=self.config.timeout
                    )
                elif method.upper() == "PUT":
                    response = self.client.put(
                        url,
                        data=data,
                        headers=headers,
                        timeout=self.config.timeout
                    )
                else:
                    raise ValueError(f"不支援的HTTP方法: {method}")
            
            # 記錄響應信息
            self.logger.debug(f"響應狀態碼: {response.status_code}")
            
            # 檢查HTTP狀態碼
            if response.status_code != 200:
                try:
                    error_data = response.json()
                except ValueError:
                    error_data = {"message": response.text}
                
                self.logger.error(f"HTTP錯誤: {response.status_code}, {error_data}")
                handle_api_error(error_data, response.status_code)
            
            # 解析響應
            try:
                response_data = response.json()
                self.logger.debug(f"響應數據: {str(response_data)[:200]}...")
            except ValueError as e:
                self.logger.error(f"JSON解析錯誤: {e}")
                raise NetworkError(f"無法解析API響應: {e}")
            
            # 檢查業務邏輯錯誤 (合約API的錯誤格式可能不同)
            if isinstance(response_data, dict):
                # 常見的錯誤字段
                if 'code' in response_data and response_data['code'] != 0:
                    self.logger.error(f"API業務錯誤: {response_data}")
                    handle_api_error(response_data, 200)
                elif 'success' in response_data and not response_data['success']:
                    self.logger.error(f"API業務錯誤: {response_data}")
                    handle_api_error(response_data, 200)
            
            return response_data
            
        except requests.exceptions.Timeout:
            self.logger.error("請求超時")
            raise NetworkError("請求超時")
        except requests.exceptions.ConnectionError:
            self.logger.error("網路連接錯誤")
            raise NetworkError("網路連接錯誤")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"HTTP請求錯誤: {e}")
            raise NetworkError(f"HTTP請求錯誤: {e}")
    
    def close(self):
        """關閉HTTP會話"""
        self.logger.debug("關閉合約HTTP會話")
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close() 