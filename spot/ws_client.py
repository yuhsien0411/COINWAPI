"""
CoinW 現貨 WebSocket 客戶端
基於官方 ws.md 文檔實現的 WebSocket API
"""

import json
import time
import threading
import logging
from typing import Dict, List, Callable, Optional, Union, Any

import requests
import websocket

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CoinWSpotWebSocketClient:
    """
    CoinW 現貨 WebSocket 客戶端
    
    支援兩種連接方式（根據官方文檔）：
    方法1: wss://ws.futurescw.info?token={token} (需要公共令牌)
    方法2: wss://ws.futurescw.com (不需要令牌)
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        method: int = 1,  # 1 或 2，對應官方文檔的兩種方法
        public_token_url: str = "https://www.coinw.com/pusher/public-token",
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
            method: 連接方法 (1 或 2，對應官方文檔)
            public_token_url: 公共令牌獲取URL
            on_message: 接收消息的回調函數
            on_error: 錯誤處理的回調函數
            on_close: 連接關閉的回調函數
            on_open: 連接打開的回調函數
        """
        self._api_key = api_key
        self._secret_key = secret_key
        self._method = method
        self._public_token_url = public_token_url
        
        # 根據方法設置正確的 WebSocket URL
        if method == 1:
            self._ws_url = "wss://ws.futurescw.info"
        elif method == 2:
            self._ws_url = "wss://ws.futurescw.com"
        else:
            raise ValueError("method 必須是 1 或 2")
        
        # 回調函數
        self._user_on_message = on_message
        self._user_on_error = on_error
        self._user_on_close = on_close
        self._user_on_open = on_open
        
        # 連接狀態
        self._is_connected = False
        self._is_authenticated = False
        self._public_token = None
        
        # WebSocket 客戶端
        self._ws = None
        self._ws_thread = None
        
        # 訂閱管理
        self._subscriptions = []
    
    def _get_public_token(self) -> Optional[str]:
        """獲取公共令牌（方法1需要）"""
        try:
            response = requests.get(self._public_token_url)
            if response.status_code == 200:
                data = response.json()
                token = data.get("data", {}).get("token")
                logger.info("成功獲取公共令牌")
                return token
            else:
                logger.error(f"獲取公共令牌失敗: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"獲取公共令牌時發生錯誤: {e}")
            return None
    
    def connect(self) -> bool:
        """
        建立WebSocket連接
        
        Returns:
            是否連接成功
        """
        try:
            # 根據方法決定連接URL
            if self._method == 1:
                # 方法1: 需要獲取公共令牌
                if not self._api_key:  # 公共接口需要令牌
                    self._public_token = self._get_public_token()
                    if not self._public_token:
                        logger.error("無法獲取公共令牌")
                        return False
                    url = f"{self._ws_url}?token={self._public_token}"
                else:
                    # 私有接口不需要令牌（直接使用 method 2 的邏輯）
                    url = "wss://ws.futurescw.com"
            else:
                # 方法2: 直接連接，不需要令牌
                url = self._ws_url
            
            self._ws = websocket.WebSocketApp(
                url,
                on_message=self._on_websocket_message,
                on_error=self._on_websocket_error,
                on_close=self._on_websocket_close,
                on_open=self._on_websocket_open
            )
            
            self._ws_thread = threading.Thread(
                target=self._ws.run_forever,
                kwargs={"ping_interval": 30, "ping_timeout": 10}
            )
            self._ws_thread.daemon = True
            self._ws_thread.start()
            
            return True
            
        except Exception as e:
            logger.error(f"WebSocket 連接失敗: {e}")
            if self._user_on_error:
                self._user_on_error(e)
            return False
    
    def _on_websocket_message(self, ws, message):
        """WebSocket消息處理"""
        try:
            data = json.loads(message)
            logger.debug(f"收到WebSocket消息: {data}")
            
            # 處理認證回應
            if "channel" in data and data["channel"] == "login":
                if data.get("data", {}).get("result"):
                    self._is_authenticated = True
                    logger.info("私有頻道認證成功")
                else:
                    logger.error("私有頻道認證失敗")
                return
            
            if self._user_on_message:
                self._user_on_message(data)
        except Exception as e:
            logger.error(f"處理WebSocket消息錯誤: {e}")
    
    def _on_websocket_error(self, ws, error):
        """WebSocket錯誤處理"""
        logger.error(f"WebSocket錯誤: {error}")
        if self._user_on_error:
            self._user_on_error(error)
    
    def _on_websocket_close(self, ws, close_status_code, close_msg):
        """WebSocket連接關閉處理"""
        logger.info(f"WebSocket連接關閉: {close_status_code} - {close_msg}")
        self._is_connected = False
        if self._user_on_close:
            self._user_on_close(close_status_code, close_msg)
    
    def _on_websocket_open(self, ws):
        """WebSocket連接打開處理"""
        logger.info("WebSocket連接已建立")
        self._is_connected = True
        
        # 如果是私有連接，先進行認證
        if self._api_key and self._secret_key:
            self._authenticate_websocket()
        
        if self._user_on_open:
            self._user_on_open()
    
    def _authenticate_websocket(self):
        """WebSocket私有頻道認證"""
        if not self._api_key or not self._secret_key:
            logger.error("私有頻道認證需要API金鑰和密鑰")
            return
        
        login_data = {
            "event": "login",
            "params": {
                "api_key": self._api_key,
                "passphrase": self._secret_key
            }
        }
        
        self._send_message(login_data)
        logger.info("發送私有頻道認證請求")
    
    def _send_message(self, data: Dict):
        """發送消息"""
        try:
            if self._ws and self._is_connected:
                self._ws.send(json.dumps(data))
                logger.debug(f"發送消息: {data}")
            else:
                logger.error("WebSocket未連接，無法發送消息")
        except Exception as e:
            logger.error(f"發送消息失敗: {e}")
    
    def subscribe_method1(self, args: Union[str, List[str]]):
        """
        方法1 訂閱（官方文檔方法1）
        
        Args:
            args: 訂閱參數，格式如 "spot/market-api-ticker:BTC-USDT"
        """
        if not self._is_connected:
            logger.error("WebSocket未連接，無法訂閱")
            return
        
        if isinstance(args, str):
            subscription_args = [args]
        else:
            subscription_args = args
        
        subscription_data = {
            "event": "subscribe",
            "args": subscription_args
        }
        
        self._send_message(subscription_data)
        self._subscriptions.extend(subscription_args)
        logger.info(f"方法1 訂閱: {subscription_args}")
    
    def subscribe_method2(self, biz: str, message_type: str, pair_code: Optional[str] = None, **kwargs):
        """
        方法2 訂閱（官方文檔方法2）
        
        Args:
            biz: 頻道，如 "exchange"
            message_type: 消息類型，如 "ticker", "depth_snapshot", "candles", "fills"
            pair_code: 交易對代碼，如 "78" (BTC-USDT)
            **kwargs: 其他參數，如 interval
        """
        if not self._is_connected:
            logger.error("WebSocket未連接，無法訂閱")
            return
        
        params = {
            "biz": biz,
            "type": message_type
        }
        
        if pair_code:
            params["pairCode"] = pair_code
        
        # 添加其他參數
        params.update(kwargs)
        
        subscription_data = {
            "event": "sub",
            "params": params
        }
        
        self._send_message(subscription_data)
        self._subscriptions.append(f"{biz}:{message_type}:{pair_code or 'all'}")
        logger.info(f"方法2 訂閱: {subscription_data}")
    
    def subscribe(self, *args, **kwargs):
        """
        智能訂閱方法，根據參數自動選擇方法1或方法2
        """
        if len(args) == 1 and isinstance(args[0], (str, list)):
            # 如果是單個字符串或列表，使用方法1
            self.subscribe_method1(args[0])
        else:
            # 否則使用方法2
            self.subscribe_method2(*args, **kwargs)
    
    def unsubscribe_method1(self, args: Union[str, List[str]]):
        """方法1 取消訂閱"""
        if isinstance(args, str):
            unsubscribe_args = [args]
        else:
            unsubscribe_args = args
        
        unsubscribe_data = {
            "event": "unsubscribe",
            "args": unsubscribe_args
        }
        
        self._send_message(unsubscribe_data)
        for arg in unsubscribe_args:
            if arg in self._subscriptions:
                self._subscriptions.remove(arg)
        
        logger.info(f"方法1 取消訂閱: {unsubscribe_args}")
    
    def unsubscribe_method2(self, biz: str, message_type: str, pair_code: Optional[str] = None, **kwargs):
        """方法2 取消訂閱"""
        params = {
            "biz": biz,
            "type": message_type
        }
        
        if pair_code:
            params["pairCode"] = pair_code
        
        params.update(kwargs)
        
        unsubscribe_data = {
            "event": "unsub",
            "params": params
        }
        
        self._send_message(unsubscribe_data)
        logger.info(f"方法2 取消訂閱: {unsubscribe_data}")
    
    def close(self):
        """關閉WebSocket連接"""
        self._is_connected = False
        
        if self._ws:
            self._ws.close()
        
        if self._ws_thread and self._ws_thread.is_alive():
            self._ws_thread.join(timeout=1)
        
        logger.info("WebSocket連接已關閉")
    
    def wait(self):
        """等待連接（阻塞模式）"""
        if self._ws_thread:
            self._ws_thread.join()
    
    def is_connected(self) -> bool:
        """檢查是否已連接"""
        return self._is_connected
    
    def is_authenticated(self) -> bool:
        """檢查私有頻道是否已認證"""
        return self._is_authenticated


# 向後兼容別名
SpotWebSocketClient = CoinWSpotWebSocketClient


def SpotWebsocketPublic(
    args_or_url: Union[str, List[str]], 
    subscription_params: Optional[Dict] = None, 
    method: int = 1,
    on_message: Optional[Callable] = None
):
    """
    現貨WebSocket公共接口簡單函數
    
    Args:
        args_or_url: 方法1的訂閱參數 或 方法2的URL
        subscription_params: 方法2的訂閱參數
        method: 使用的方法 (1 或 2)
        on_message: 消息處理回調函數
    """
    def default_message_handler(data):
        print(f"收到公共消息: {data}")
    
    message_handler = on_message or default_message_handler
    
    if method == 1:
        # 方法1: wss://ws.futurescw.info?token={token}
        _websocket_method1_public(args_or_url, message_handler)
    else:
        # 方法2: wss://ws.futurescw.com
        _websocket_method2_public(subscription_params or {}, message_handler)


def _websocket_method1_public(args: Union[str, List[str]], message_handler: Callable):
    """方法1 公共連接"""
    try:
        # 獲取公共令牌
        res = requests.get("https://www.coinw.com/pusher/public-token")
        token = res.json().get("data")["token"]
        
        url = f"wss://ws.futurescw.info?token={token}"
        
        ws = websocket.WebSocket()
        ws.connect(url)
        print(f"✅ 方法1已連接到: {url}")
        
        # 發送訂閱消息（方法1格式）
        subscription_data = {
            "event": "subscribe",
            "args": args if isinstance(args, list) else [args]
        }
        ws.send(json.dumps(subscription_data))
        print(f"📡 方法1訂閱已發送: {subscription_data}")
        
        while True:
            try:
                response = ws.recv()
                try:
                    data = json.loads(response)
                    message_handler(data)
                except json.JSONDecodeError:
                    print(f"⚠️ 無法解析的消息: {response}")
                
                time.sleep(1)
                
            except websocket.WebSocketTimeoutException:
                print("⏰ WebSocket 超時，繼續等待...")
                continue
            except websocket.WebSocketConnectionClosedException:
                print("❌ WebSocket 連接已關閉")
                break
    
    except KeyboardInterrupt:
        print("\n🛑 用戶中斷連接")
    except Exception as e:
        print(f"❌ 錯誤: {e}")
    finally:
        try:
            ws.close()
            print("🔐 WebSocket 連接已關閉")
        except:
            pass


def _websocket_method2_public(subscription_params: Dict, message_handler: Callable):
    """方法2 公共連接"""
    try:
        url = "wss://ws.futurescw.com"
        
        ws = websocket.WebSocket()
        ws.connect(url)
        print(f"✅ 方法2已連接到: {url}")
        
        # 發送訂閱消息（方法2格式）
        ws.send(json.dumps(subscription_params))
        print(f"📡 方法2訂閱已發送: {subscription_params}")
        
        while True:
            try:
                response = ws.recv()
                try:
                    data = json.loads(response)
                    message_handler(data)
                except json.JSONDecodeError:
                    print(f"⚠️ 無法解析的消息: {response}")
                
                time.sleep(1)
                
            except websocket.WebSocketTimeoutException:
                print("⏰ WebSocket 超時，繼續等待...")
                continue
            except websocket.WebSocketConnectionClosedException:
                print("❌ WebSocket 連接已關閉")
                break
    
    except KeyboardInterrupt:
        print("\n🛑 用戶中斷連接")
    except Exception as e:
        print(f"❌ 錯誤: {e}")
    finally:
        try:
            ws.close()
            print("🔐 WebSocket 連接已關閉")
        except:
            pass


def SpotWebsocketPrivate(
    subscription_payload: Dict,
    api_key: str,
    sec_key: str,
    url: str = "wss://ws.futurescw.com",
    on_message: Optional[Callable] = None
):
    """
    現貨WebSocket私有接口簡單函數
    
    Args:
        subscription_payload: 訂閱載荷
        api_key: API金鑰
        sec_key: 密鑰
        url: WebSocket URL
        on_message: 消息處理回調函數
    """
    def default_message_handler(data):
        print(f"收到私有消息: {data}")
    
    message_handler = on_message or default_message_handler
    
    try:
        ws = websocket.WebSocket()
        ws.connect(url)
        print(f"✅ 已連接到: {url}")
        
        # 發送登錄消息
        login_payload = {
            "event": "login",
            "params": {
                "api_key": api_key,
                "passphrase": sec_key
            }
        }
        ws.send(json.dumps(login_payload))
        print("🔑 登錄請求已發送")
        
        # 等待登錄確認
        login_response = ws.recv()
        print(f"🔓 登錄回應: {login_response}")
        
        # 發送訂閱消息
        ws.send(json.dumps(subscription_payload))
        print(f"📡 私有訂閱已發送: {subscription_payload}")
        
        while True:
            try:
                response = ws.recv()
                try:
                    data = json.loads(response)
                    message_handler(data)
                except json.JSONDecodeError:
                    print(f"⚠️ 無法解析的消息: {response}")
                
                time.sleep(0.5)
                
            except websocket.WebSocketTimeoutException:
                print("⏰ WebSocket 超時，繼續等待...")
                continue
            except websocket.WebSocketConnectionClosedException:
                print("❌ WebSocket 連接已關閉")
                break
    
    except KeyboardInterrupt:
        print("\n🛑 用戶中斷連接")
    except Exception as e:
        print(f"❌ 錯誤: {e}")
    finally:
        try:
            ws.close()
            print("🔐 WebSocket 連接已關閉")
        except:
            pass 