"""
CoinW API 客戶端

提供CoinW交易所API的Python封裝，包含完整的現貨和期貨API支援
"""

from coinwapi.exceptions import (
    CoinWAPIError,
    InvalidCredentialsError,
    RateLimitError,
    InsufficientBalanceError,
    InvalidParameterError
)

# 現貨模塊導入
from coinwapi.spot import (
    SpotClient,
    CoinWSpotWebSocketClient,
    SpotWebSocketClient,
    SpotHTTPManager,
    SpotRestfulPublic,
    SpotRestfulPrivate,
    SpotWebsocketPublic,
    SpotWebsocketPrivate,

)

# 期貨模塊導入
from coinwapi.future import (
    FutureClient,
    CoinWFutureWebSocketClient,
    FutureWebSocketClient,
    FuturesWebsocketPublic,
    FuturesWebsocketPrivate

)

__version__ = "1.0.0"
__author__ = "CoinW API Team"
__description__ = "CoinW 交易所 Python SDK - 支援完整的現貨和期貨 REST 與 WebSocket API，包含 Java 代碼對應實現"

__all__ = [
    # 現貨 API
    'SpotClient',
    'CoinWSpotWebSocketClient',
    'SpotWebSocketClient',       # 向後兼容
    'SpotHTTPManager',
    
    # 現貨簡單函數
    'SpotRestfulPublic',
    'SpotRestfulPrivate', 
    'SpotWebsocketPublic',
    'SpotWebsocketPrivate',
    

    # 期貨 API
    'FutureClient',
    'CoinWFutureWebSocketClient',
    'FutureWebSocketClient',     # 向後兼容
   
    
    # 期貨簡單函數
    'FuturesWebsocketPublic',
    'FuturesWebsocketPrivate',
    
    # 異常類
    'CoinWAPIError',
    'InvalidCredentialsError',
    'RateLimitError',
    'InsufficientBalanceError',
    'InvalidParameterError'
]

# 快速使用指南
"""
快速開始：

1. 現貨 REST API:
   from coinwapi import SpotClient, SpotRestfulPublic
   client = SpotClient(api_key="your_key", secret_key="your_secret")
   # 或使用簡單函數
   result = SpotRestfulPublic("/spot/public/symbol")

3. 現貨 WebSocket:
   from coinwapi import CoinWSpotWebSocketClient, SpotWebsocketPublic
   client = CoinWSpotWebSocketClient()
   client.connect()
   # 或使用簡單函數
   SpotWebsocketPublic("market.BTCUSDT.ticker")

4. 期貨 REST API:
   from coinwapi import FutureClient
   client = FutureClient(api_key="your_key", secret_key="your_secret")

5. 期貨 WebSocket:
   from coinwapi import CoinWFutureWebSocketClient, FuturesWebsocketPublic
   client = CoinWFutureWebSocketClient()
   client.connect()
   # 或使用簡單函數
   FuturesWebsocketPublic(url, subscription_params)


""" 