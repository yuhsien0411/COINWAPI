"""
CoinW 現貨交易模組

提供CoinW現貨交易的API封裝
包含完整的 REST API 和 WebSocket API 支援
"""

from .market import SpotMarket
from .order import SpotOrder
from .account import SpotAccount
from .client import SpotClient
from .ws_client import CoinWSpotWebSocketClient, SpotWebSocketClient, SpotWebsocketPublic, SpotWebsocketPrivate
from .http_manager import SpotHTTPManager, SpotRestfulPublic, SpotRestfulPrivate

__all__ = [
    # REST API 客戶端
    'SpotMarket',
    'SpotOrder',
    'SpotAccount',
    'SpotClient',
    
    # HTTP 管理器
    'SpotHTTPManager',
    
    # WebSocket 客戶端
    'CoinWSpotWebSocketClient',  # 完整實現
    'SpotWebSocketClient',       # 向後兼容別名
    
    # 簡單函數接口
    'SpotRestfulPublic',         # REST 公共接口函數
    'SpotRestfulPrivate',        # REST 私有接口函數
    'SpotWebsocketPublic',       # WebSocket 公共接口函數
    'SpotWebsocketPrivate',      # WebSocket 私有接口函數
]

__version__ = "1.0.0"
__author__ = "CoinW API Team"
__description__ = "CoinW 現貨交易 Python SDK - 支援完整的 REST 和 WebSocket API"

# 模塊說明
"""
使用指南：

1. REST API 使用：
   from coinwapi.spot import SpotClient
   client = SpotClient(api_key="your_key", secret_key="your_secret")

2. 簡單 REST 函數使用：
   from coinwapi.spot import SpotRestfulPublic, SpotRestfulPrivate
   result = SpotRestfulPublic("/spot/public/symbol")

3. Java 代碼對應實現：
   from coinwapi.spot import JavaSpotRestfulPublic, JavaSpotRestfulPrivate
   # 公共接口
   result = JavaSpotRestfulPublic.spot_restful_public("/api/v1/public?command=returnTicker", {})
   # 私有接口
   client = JavaSpotRestfulPrivate("your_api_key", "your_secret_key")
   result = client.spot_restful_private("/api/v1/private?command=returnBalances", "POST", {})

4. WebSocket 使用：
   from coinwapi.spot import CoinWSpotWebSocketClient
   ws_client = CoinWSpotWebSocketClient()
   ws_client.connect()
   ws_client.subscribe("market.BTCUSDT.ticker")

5. 簡單 WebSocket 使用：
   from coinwapi.spot import SpotWebsocketPublic
   SpotWebsocketPublic("market.BTCUSDT.ticker")

認證要求：
- REST 公共接口：不需要認證
- REST 私有接口：需要 API 密鑰和 MD5 簽名
- WebSocket 公共接口：需要公共令牌
- WebSocket 私有接口：需要 API 密鑰和密鑰

Java 代碼對應：
- JavaSpotRestfulPublic：完全對應 Java SpotRestfulPublic 類
- JavaSpotRestfulPrivate：完全對應 Java SpotRestfulPrivate 類
- 保持相同的方法簽名和參數格式
- 保持相同的API端點和示例
""" 