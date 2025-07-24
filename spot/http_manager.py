"""
CoinW 現貨 API HTTP 管理器

基於用戶提供的現貨API實現，使用MD5簽名機制
"""

import time
import json
import hashlib
import urllib.parse
import logging
from typing import Dict, Any, Optional, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SpotHTTPManager:
    """
    CoinW 現貨 API HTTP管理器
    
    處理所有HTTP請求、MD5簽名認證和錯誤處理
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        base_url: str = "https://api.coinw.com",
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        初始化HTTP管理器
        
        Args:
            api_key: API金鑰（私有接口需要）
            secret_key: 密鑰（私有接口需要）
            base_url: API基礎URL
            timeout: 請求超時時間
            max_retries: 最大重試次數
        """
        self._api_key = api_key
        self._secret_key = secret_key
        self._base_url = base_url
        self._timeout = timeout
        
        # 創建session
        self._session = requests.Session()
        
        # 設置重試策略
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)
        
        # 設置請求頭
        self._session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'CoinW-Python-SDK/1.0'
        })
    
    def generate_signature(self, params: Dict[str, Any]) -> str:
        """
        生成MD5簽名
        
        Args:
            params: 請求參數
            
        Returns:
            MD5簽名字符串
        """
        if not self._secret_key:
            raise ValueError("secret_key 必須設置才能生成簽名")
        
        # 添加API金鑰
        if self._api_key:
            params["api_key"] = self._api_key
        
        # 按key排序參數
        sorted_params = sorted(params.items())
        
        # 構建查詢字符串
        query_string = "&".join([f"{k}={v}" for k, v in sorted_params]) + "&"
        
        # 添加密鑰
        sign_string = query_string + f"secret_key={self._secret_key}"
        
        # MD5加密並轉為大寫
        signature = hashlib.md5(sign_string.encode("utf-8")).hexdigest().upper()
        
        return signature
    
    def spot_restful_public(self, api_url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        現貨REST公共接口
        
        Args:
            api_url: API路徑，例如 "/api/v1/public"
            params: 請求參數
            
        Returns:
            API響應數據
        """
        url = f"{self._base_url}{api_url}"
        
        try:
            logger.debug(f"發送公共請求: {url}, 參數: {params}")
            
            response = self._session.get(
                url, 
                params=params or {},
                timeout=self._timeout
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"請求失敗，狀態碼: {response.status_code}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}",
                    "message": response.text
                }
                
        except requests.exceptions.RequestException as e:
            logger.error(f"網絡請求錯誤: {e}")
            return {
                "success": False,
                "error": "NetworkError",
                "message": str(e)
            }
    
    def spot_restful_private(
        self, 
        api_url: str, 
        method: str = "POST", 
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        現貨REST私有接口
        
        Args:
            api_url: API路徑
            method: HTTP方法
            params: 請求參數
            
        Returns:
            API響應數據
        """
        if not self._api_key or not self._secret_key:
            raise ValueError("私有接口需要設置 api_key 和 secret_key")
        
        request_params = params.copy() if params else {}
        
        try:
            # 生成簽名
            signature = self.generate_signature(request_params.copy())
            request_params["sign"] = signature
            
            url = f"{self._base_url}{api_url}"
            
            logger.debug(f"發送私有請求: {url}, 方法: {method}, 參數: {request_params}")
            
            if method.upper() == "GET":
                response = self._session.get(
                    url,
                    params=request_params,
                    timeout=self._timeout
                )
            else:
                response = self._session.post(
                    url,
                    data=request_params,
                    timeout=self._timeout
                )
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"請求失敗，狀態碼: {response.status_code}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}",
                    "message": response.text
                }
                
        except requests.exceptions.RequestException as e:
            logger.error(f"網絡請求錯誤: {e}")
            return {
                "success": False,
                "error": "NetworkError", 
                "message": str(e)
            }
    
    def get(self, endpoint: str, params: Optional[Dict] = None, auth_required: bool = False) -> Dict[str, Any]:
        """
        通用GET請求
        
        Args:
            endpoint: API端點
            params: 請求參數
            auth_required: 是否需要認證
            
        Returns:
            API響應數據
        """
        if auth_required:
            return self.spot_restful_private(endpoint, "GET", params)
        else:
            return self.spot_restful_public(endpoint, params)
    
    def post(self, endpoint: str, params: Optional[Dict] = None, auth_required: bool = False) -> Dict[str, Any]:
        """
        通用POST請求
        
        Args:
            endpoint: API端點
            params: 請求參數
            auth_required: 是否需要認證
            
        Returns:
            API響應數據
        """
        if auth_required:
            return self.spot_restful_private(endpoint, "POST", params)
        else:
            # 公共POST請求（如果需要）
            url = f"{self._base_url}{endpoint}"
            try:
                response = self._session.post(
                    url,
                    json=params or {},
                    timeout=self._timeout
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    return {
                        "success": False,
                        "error": f"HTTP {response.status_code}",
                        "message": response.text
                    }
                    
            except requests.exceptions.RequestException as e:
                return {
                    "success": False,
                    "error": "NetworkError",
                    "message": str(e)
                }


def SpotRestfulPublic(api_url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
    """
    現貨REST公共接口簡單函數
    
    Args:
        api_url: API路徑
        params: 請求參數
        
    Returns:
        API響應數據
    """
    manager = SpotHTTPManager()
    return manager.spot_restful_public(api_url, params)


def SpotRestfulPrivate(
    api_url: str,
    method: str,
    api_key: str,
    secret_key: str,
    params: Optional[Dict] = None,
    host: str = "https://api.coinw.com"
) -> Dict[str, Any]:
    """
    現貨REST私有接口簡單函數
    
    Args:
        api_url: API路徑
        method: HTTP方法
        api_key: API金鑰
        secret_key: 密鑰
        params: 請求參數
        host: 主機地址
        
    Returns:
        API響應數據
    """
    manager = SpotHTTPManager(api_key=api_key, secret_key=secret_key, base_url=host)
    return manager.spot_restful_private(api_url, method, params) 