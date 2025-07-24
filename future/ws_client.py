"""
CoinW 期貨 WebSocket 客戶端
基於官方 API 文檔 ws.md 的完整實現
"""

import json
import time
import websocket
import threading
import logging
from typing import Dict, List, Callable, Optional, Union, Any

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CoinWFutureWebSocketClient:
    """
    CoinW 期貨 WebSocket 客戶端
    
    提供期貨市場數據和交易更新的實時訂閱
    支援所有公共和私有 WebSocket 接口
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        on_message: Optional[Callable] = None,
        on_error: Optional[Callable] = None,
        on_close: Optional[Callable] = None,
        on_open: Optional[Callable] = None,
    ):
        """
        初始化 WebSocket 客戶端
        
        Args:
            api_key: API金鑰 (用於私有訂閱)
            secret_key: 密鑰 (用於私有訂閱)
            on_message: 接收消息的回調函數
            on_error: 錯誤處理的回調函數
            on_close: 連接關閉的回調函數
            on_open: 連接打開的回調函數
        """
        self._api_key = api_key
        self._secret_key = secret_key
        
        # WebSocket URL - 根據文檔使用正確的端點
        self._ws_url = "wss://ws.futurescw.com/perpum"
        
        # 回調函數
        self._user_on_message = on_message
        self._user_on_error = on_error
        self._user_on_close = on_close
        self._user_on_open = on_open
        
        # WebSocket連接
        self._ws: Optional[websocket.WebSocketApp] = None
        self._ws_thread: Optional[threading.Thread] = None
        self._is_connected = False
        self._is_authenticated = False
        self._reconnect_attempts = 0
        self._max_reconnects = 5
        
        # 訂閱管理
        self._subscriptions: Dict[str, Dict] = {}
        
        # 心跳管理
        self._last_ping_time = 0
        self._ping_interval = 30
    
    def connect(self) -> bool:
        """
        建立WebSocket連接
        
        Returns:
            bool: 連接是否成功
        """
        try:
            logger.info("正在連接到 CoinW 期貨 WebSocket...")
            
            self._ws = websocket.WebSocketApp(
                self._ws_url,
                on_message=self._on_message,
                on_error=self._on_error,
                on_close=self._on_close,
                on_open=self._on_open
            )
            
            self._ws_thread = threading.Thread(
                target=self._ws.run_forever,
                kwargs={"ping_interval": 30, "ping_timeout": 10}
            )
            self._ws_thread.daemon = True
            self._ws_thread.start()
            
            # 等待連接建立
            timeout = 10
            start_time = time.time()
            while not self._is_connected and time.time() - start_time < timeout:
                time.sleep(0.1)
            
            return self._is_connected
            
        except Exception as e:
            logger.error(f"連接失敗: {e}")
            return False
    
    def _on_message(self, ws, message) -> None:
        """WebSocket消息處理"""
        try:
            data = json.loads(message)
            logger.debug(f"收到消息: {data}")
            
            # 處理認證回應
            if "event" in data and data["event"] == "login":
                if data.get("success"):
                    self._is_authenticated = True
                    logger.info("私有頻道認證成功")
                else:
                    logger.error("私有頻道認證失敗")
                return
            
            # 調用用戶的回調函數
            if self._user_on_message:
                self._user_on_message(data)
        
        except Exception as e:
            logger.error(f"處理消息時出錯: {e}")
    
    def _on_error(self, ws, error) -> None:
        """WebSocket錯誤處理"""
        logger.error(f"WebSocket錯誤: {error}")
        
        if self._user_on_error:
            self._user_on_error(error)
    
    def _on_close(self, ws, close_status_code, close_msg) -> None:
        """WebSocket連接關閉處理"""
        logger.info(f"WebSocket連接關閉: {close_status_code} - {close_msg}")
        self._is_connected = False
        self._is_authenticated = False
        
        # 嘗試重新連接
        if self._reconnect_attempts < self._max_reconnects:
            self._reconnect_attempts += 1
            logger.info(f"嘗試重新連接... (第 {self._reconnect_attempts} 次)")
            time.sleep(self._reconnect_attempts * 2)  # 指數退避
            self.connect()
        
        if self._user_on_close:
            self._user_on_close(close_status_code, close_msg)
    
    def _on_open(self, ws) -> None:
        """WebSocket連接打開處理"""
        logger.info("WebSocket連接已建立")
        self._is_connected = True
        self._reconnect_attempts = 0
        
        # 重新訂閱
        for topic, params in self._subscriptions.items():
            self._send_subscription(params)
        
        if self._user_on_open:
            self._user_on_open()
    
    def _authenticate(self) -> bool:
        """私有頻道身份驗證"""
        if not self._api_key or not self._secret_key:
            logger.error("私有訂閱需要API金鑰和密鑰")
            return False
        
        login_params = {
            "event": "login",
            "params": {
                "api_key": self._api_key,
                "passphrase": self._secret_key
            }
        }
        
        try:
            self._ws.send(json.dumps(login_params))
            logger.info("發送身份驗證請求")
            
            # 等待認證回應
            timeout = 10
            start_time = time.time()
            while not self._is_authenticated and time.time() - start_time < timeout:
                time.sleep(0.1)
            
            return self._is_authenticated
        except Exception as e:
            logger.error(f"認證時出錯: {e}")
            return False
    
    def _send_subscription(self, params: Dict) -> bool:
        """發送訂閱請求"""
        if not self._is_connected or not self._ws:
            logger.error("WebSocket未連接，無法訂閱")
            return False
        
        try:
            # 如果是私有訂閱，先進行身份驗證
            if params.get("private", False) and not self._is_authenticated:
                if not self._authenticate():
                    logger.error("身份驗證失敗，無法訂閱私有頻道")
                    return False
            
            # 清理參數（移除內部標記）
            clean_params = {k: v for k, v in params.items() if k != "private"}
            
            # 發送訂閱請求
            self._ws.send(json.dumps(clean_params))
            logger.info(f"已發送訂閱: {clean_params}")
            return True
        
        except Exception as e:
            logger.error(f"訂閱時出錯: {e}")
            return False
    
    def subscribe(self, subscription_params: Dict, callback: Optional[Callable] = None) -> bool:
        """
        通用訂閱方法
        
        Args:
            subscription_params: 訂閱參數，格式與文檔一致
            callback: 可選的回調函數
            
        Returns:
            bool: 訂閱是否成功
        """
        if callback:
            self._user_on_message = callback
        
        # 生成唯一的訂閱key
        params = subscription_params.get("params", {})
        topic = f"{params.get('type', 'unknown')}_{params.get('pairCode', 'all')}"
        
        self._subscriptions[topic] = subscription_params
        
        if self._is_connected:
            return self._send_subscription(subscription_params)
        else:
            logger.warning("WebSocket未連接，訂閱將在連接後自動執行")
            return True
    
    def unsubscribe(self, subscription_params: Dict) -> bool:
        """
        取消訂閱
        
        Args:
            subscription_params: 訂閱參數，將event改為unsub
            
        Returns:
            bool: 取消訂閱是否成功
        """
        try:
            unsub_params = subscription_params.copy()
            unsub_params["event"] = "unsub"
            
            if self._is_connected and self._ws:
                self._ws.send(json.dumps(unsub_params))
                logger.info(f"已發送取消訂閱: {unsub_params}")
            
            # 從訂閱列表中移除
            params = subscription_params.get("params", {})
            topic = f"{params.get('type', 'unknown')}_{params.get('pairCode', 'all')}"
            if topic in self._subscriptions:
                del self._subscriptions[topic]
            
            return True
            
        except Exception as e:
            logger.error(f"取消訂閱時出錯: {e}")
            return False
    
    def close(self) -> None:
        """關閉WebSocket連接"""
        self._is_connected = False
        
        if self._ws:
            self._ws.close()
        
        if self._ws_thread and self._ws_thread.is_alive():
            self._ws_thread.join(timeout=1)
        
        logger.info("WebSocket連接已關閉")
    
    def is_connected(self) -> bool:
        """檢查WebSocket是否已連接"""
        return self._is_connected
    
    def is_authenticated(self) -> bool:
        """檢查是否已通過私有頻道身份驗證"""
        return self._is_authenticated


# 簡化的函數接口，對應文檔中的示例

def FuturesWebsocketPublic(url: str, subscription_params: Dict, on_message: Optional[Callable] = None) -> None:
    """
    期貨公共WebSocket接口函數
    對應文檔中的 FuturesWebsocketPublic() 函數
    
    Args:
        url: WebSocket URL
        subscription_params: 訂閱參數
        on_message: 消息回調函數
    """
    client = CoinWFutureWebSocketClient(on_message=on_message)
    
    if client.connect():
        client.subscribe(subscription_params)
        
        try:
            # 保持連接運行
            while client.is_connected():
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("用戶中斷連接")
        finally:
            client.close()
    else:
        logger.error("連接失敗")


def FuturesWebsocketPrivate(url: str, subscription_payload: Dict, api_key: str, sec_key: str, on_message: Optional[Callable] = None) -> None:
    """
    期貨私有WebSocket接口函數
    對應文檔中的 FuturesWebsocketPrivate() 函數
    
    Args:
        url: WebSocket URL
        subscription_payload: 訂閱參數
        api_key: API密鑰
        sec_key: 密鑰
        on_message: 消息回調函數
    """
    # 標記為私有訂閱
    subscription_payload["private"] = True
    
    client = CoinWFutureWebSocketClient(
        api_key=api_key,
        secret_key=sec_key,
        on_message=on_message
    )
    
    if client.connect():
        client.subscribe(subscription_payload)
        
        try:
            # 保持連接運行
            while client.is_connected():
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("用戶中斷連接")
        finally:
            client.close()
    else:
        logger.error("連接失敗")


# 向後兼容的別名
FutureWebSocketClient = CoinWFutureWebSocketClient 