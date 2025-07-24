"""
CoinW 現貨市場數據模組

專門處理現貨市場數據 API
端點格式: /api/v1/public?command=...
"""

from typing import Dict, Any, Optional
from .http_manager import SpotHTTPManager


class SpotMarket:
    """現貨市場數據接口"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        base_url: str = "https://api.coinw.com",
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        初始化現貨市場數據接口
        
        Args:
            api_key: API金鑰（市場數據不需要，但保持接口一致）
            secret_key: 密鑰（市場數據不需要，但保持接口一致）
            base_url: API基礎URL
            timeout: 請求超時時間
            max_retries: 最大重試次數
        """
        self._http_manager = SpotHTTPManager(
            api_key=api_key,
            secret_key=secret_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries
        )
    
    def get_ticker(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取現貨 ticker 數據
        
        Args:
            symbol: 交易對，如 "BTC_USDT"，為空則返回所有
            
        Returns:
            ticker 數據
        """
        params = {'command': 'returnTicker'}
        if symbol:
            params['symbol'] = symbol
        
        return self._http_manager.spot_restful_public("/api/v1/public", params)
    
    def get_orderbook(self, symbol: str, size: int = 5) -> Dict[str, Any]:
        """
        獲取現貨訂單簿數據
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            size: 深度級別，只支援 5 或 20，預設 5
            
        Returns:
            訂單簿數據
        """
        # 確保 size 參數正確
        if size not in [5, 20]:
            size = 5
            
        params = {
            'command': 'returnOrderBook',
            'symbol': symbol,
            'size': size  # 修正：使用 'size' 而不是 'depth'
        }
        return self._http_manager.spot_restful_public("/api/v1/public", params)
    
    def get_trades(self, symbol: str, start: Optional[str] = None, end: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取現貨最近成交記錄
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            start: 開始時間戳（可選）
            end: 結束時間戳（可選）
            
        Returns:
            成交記錄
        """
        params = {
            'command': 'returnTradeHistory',
            'symbol': symbol
        }
        
        # 添加時間範圍參數（如果提供）
        if start:
            params['start'] = start
        if end:
            params['end'] = end
            
        return self._http_manager.spot_restful_public("/api/v1/public", params)
    
    def get_symbols(self) -> Dict[str, Any]:
        """
        獲取所有現貨交易對信息
        
        Returns:
            交易對信息
        """
        return self._http_manager.spot_restful_public("/api/v1/public", {'command': 'returnSymbol'})
    
    def get_currencies(self) -> Dict[str, Any]:
        """
        獲取所有幣種信息
        
        Returns:
            幣種信息
        """
        return self._http_manager.spot_restful_public("/api/v1/public", {'command': 'returnCurrencies'})
    
    def get_24hr_volume(self) -> Dict[str, Any]:
        """
        獲取24小時成交量統計
        
        Returns:
            24小時成交量數據
        """
        return self._http_manager.spot_restful_public("/api/v1/public", {'command': 'return24hVolume'})
    
    def get_kline(self, symbol: str, period: int, start: Optional[str] = None, end: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取K線數據
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            period: 時間週期（秒），如 60=1分鐘, 300=5分鐘, 900=15分鐘, 1800=30分鐘, 7200=2小時, 14400=4小時
            start: 開始時間戳（Unix 毫秒級，可選）
            end: 結束時間戳（Unix 毫秒級，可選）
            
        Returns:
            K線數據
        """
        params = {
            'command': 'returnChartData',
            'currencyPair': symbol,  # 注意：K線接口使用 currencyPair 而不是 symbol
            'period': period  # 修正：period 是數字（秒數）
        }
        
        # 添加時間範圍參數（如果提供）
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        
        return self._http_manager.spot_restful_public("/api/v1/public", params)
    
    def get_server_time(self) -> Dict[str, Any]:
        """
        獲取服務器時間
        
        Returns:
            服務器時間信息
        """
        return self._http_manager.spot_restful_public("/api/v1/public", {'command': 'returnServerTime'}) 