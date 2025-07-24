"""
CoinW 期貨交易模組

提供CoinW期貨交易的API封裝
包含完整的 REST API 和 WebSocket API 支援
"""

# REST API 客戶端
from .client import FutureClient
from .market import FutureMarket
from .order import FutureOrder
from .account import FutureAccount
from .position import FuturePosition

# HTTP 管理器
from .http_manager import _ContractHTTPManager as FutureHTTPManager, ContractHTTPConfig

# WebSocket 客戶端
from .ws_client import CoinWFutureWebSocketClient, FuturesWebsocketPublic, FuturesWebsocketPrivate

__all__ = [
    # REST API 客戶端
    'FutureClient',
    'FutureMarket',
    'FutureOrder',
    'FutureAccount',
    'FuturePosition',
    
    # HTTP 管理器
    'FutureHTTPManager',
    'ContractHTTPConfig',
    
    # WebSocket 客戶端
    'CoinWFutureWebSocketClient',    # 完整實現
    'FuturesWebsocketPublic',        # 公共接口函數
    'FuturesWebsocketPrivate',       # 私有接口函數
    
    # 向後兼容別名
    'FutureWebSocketClient',
]

# 向後兼容別名
FutureWebSocketClient = CoinWFutureWebSocketClient

__version__ = "1.0.0"
__author__ = "CoinW API Team"
__description__ = "CoinW 期貨交易 Python SDK - 支援完整的 REST 和 WebSocket API"

# 模塊說明
"""
使用指南：

1. REST API 使用：
   from coinwapi.future import FutureClient
   client = FutureClient(api_key="your_key", secret_key="your_secret")

2. WebSocket 使用：
   from coinwapi.future import CoinWFutureWebSocketClient
   ws_client = CoinWFutureWebSocketClient()
   ws_client.connect()
   ws_client.subscribe_ticker("BTC")

3. 簡單 WebSocket 使用：
   from coinwapi.future import FuturesWebsocketPublic
   FuturesWebsocketPublic(url, params)

示例文件：
- ws_examples.py - 完整的 WebSocket 使用示例
- test_ws_basic.py - 基本功能測試
- README_WebSocket.md - 詳細使用指南
""" 