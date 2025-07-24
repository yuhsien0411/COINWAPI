"""
CoinW 現貨交易模組

專門處理現貨交易 API
端點格式: /api/v1/private?command=...
認證方式: MD5 簽名
"""

from typing import Dict, Any, Optional
from .http_manager import SpotHTTPManager
from ..exceptions import InvalidParameterError


class SpotOrder:
    """現貨交易接口"""
    
    def __init__(
        self,
        api_key: str,
        secret_key: str,
        base_url: str = "https://api.coinw.com",
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        初始化現貨交易接口
        
        Args:
            api_key: API金鑰
            secret_key: 密鑰
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
    
    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str = "limit",
        amount: Optional[float] = None,
        price: Optional[float] = None,
        funds: Optional[float] = None,
        client_order_id: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        現貨下單
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            side: 買賣方向，"buy" 或 "sell"
            order_type: 訂單類型，"limit" 或 "market"
            amount: 交易數量 (限價單必填，市價賣單必填)
            price: 價格 (限價單必填)
            funds: 交易金額 (市價買單使用)
            client_order_id: 自定義訂單ID
            **kwargs: 其他參數
            
        Returns:
            訂單信息
        """
        # 參數驗證
        if side not in ["buy", "sell"]:
            raise InvalidParameterError("side必須是 'buy' 或 'sell'")
        
        if order_type not in ["limit", "market"]:
            raise InvalidParameterError("order_type必須是 'limit' 或 'market'")
        
        # 基礎參數
        data = {
            'command': 'doTrade',
            'symbol': symbol,
            'type': '0' if side == "buy" else '1',  # 修正：使用字符串
            'isMarket': 'true' if order_type == "market" else 'false'  # 添加 isMarket 參數
        }
        
        # 限價單參數
        if order_type == "limit":
            if not amount or not price:
                raise InvalidParameterError("限價單必須提供 amount 和 rate")
            data['amount'] = str(amount)
            data['rate'] = str(price)
        
        # 市價單參數
        elif order_type == "market":
            if side == "buy":
                if not funds:
                    raise InvalidParameterError("市價買單必須提供 funds")
                data['funds'] = str(funds)
            else:  # sell
                if not amount:
                    raise InvalidParameterError("市價賣單必須提供 amount")
                data['amount'] = str(amount)
        
        # 自定義訂單ID
        if client_order_id:
            data['out_trade_no'] = client_order_id
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """
        取消訂單
        
        Args:
            order_id: 訂單ID
            
        Returns:
            取消結果
        """
        data = {
            'command': 'cancelOrder',
            'orderNumber': order_id
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def cancel_all_orders(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """
        取消所有訂單
        
        Args:
            symbol: 交易對，如果不指定則取消所有
            
        Returns:
            取消結果
        """
        data = {'command': 'cancelAllOrder'}
        if symbol:
            data['currencyPair'] = symbol
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_order(self, order_id: str) -> Dict[str, Any]:
        """
        獲取訂單詳情
        
        Args:
            order_id: 訂單ID
            
        Returns:
            訂單詳情
        """
        data = {
            'command': 'returnOrderTrades',
            'orderNumber': order_id
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_order_status(self, order_id: str) -> Dict[str, Any]:
        """
        獲取訂單狀態
        
        Args:
            order_id: 訂單ID
            
        Returns:
            訂單狀態
        """
        data = {
            'command': 'returnOrderStatus',
            'orderNumber': order_id
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_open_orders(self, symbol: Optional[str] = None, start_at: Optional[int] = None, end_at: Optional[int] = None) -> Dict[str, Any]:
        """
        獲取未完成訂單
        
        Args:
            symbol: 交易對，必填
            start_at: 開始時間戳（可選）
            end_at: 結束時間戳（可選）
            
        Returns:
            未完成訂單列表
        """
        if not symbol:
            raise InvalidParameterError("symbol 參數是必填的")
            
        data = {
            'command': 'returnOpenOrders',
            'currencyPair': symbol
        }
        
        # 添加時間範圍參數（如果提供）
        if start_at:
            data['startAt'] = str(start_at)
        if end_at:
            data['endAt'] = str(end_at)
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_trade_history(self, symbol: str, start_at: Optional[str] = None, end_at: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取交易歷史
        
        Args:
            symbol: 交易對，必填
            start_at: 開始時間戳（可選）
            end_at: 結束時間戳（可選）
            
        Returns:
            交易歷史
        """
        data = {
            'command': 'returnUTradeHistory',
            'currencyPair': symbol
        }
        
        # 添加時間範圍參數（如果提供）
        if start_at:
            data['startAt'] = start_at
        if end_at:
            data['endAt'] = end_at
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_order_history(self, symbol: Optional[str] = None, start_at: Optional[int] = None, end_at: Optional[int] = None, limit: int = 100, before: Optional[str] = None, after: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取歷史訂單
        
        Args:
            symbol: 交易對（可選）
            start_at: 開始時間戳（可選）
            end_at: 結束時間戳（可選）
            limit: 查詢數量，0 < limit <= 100
            before: 上一頁的分頁參數（可選）
            after: 下一頁的分頁參數（可選）
            
        Returns:
            歷史訂單
        """
        data = {'command': 'getUserTrades'}
        
        if symbol:
            data['symbol'] = symbol
        if start_at:
            data['startAt'] = str(start_at)
        if end_at:
            data['endAt'] = str(end_at)
        if limit and 0 < limit <= 100:
            data['limit'] = limit
        if before:
            data['before'] = before
        if after:
            data['after'] = after
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    # 簡化下單方法
    def buy_limit(self, symbol: str, amount: float, price: float, **kwargs) -> Dict[str, Any]:
        """限價買入"""
        return self.place_order(symbol=symbol, side="buy", order_type="limit", amount=amount, price=price, **kwargs)
    
    def sell_limit(self, symbol: str, amount: float, price: float, **kwargs) -> Dict[str, Any]:
        """限價賣出"""
        return self.place_order(symbol=symbol, side="sell", order_type="limit", amount=amount, price=price, **kwargs)
    
    def buy_market(self, symbol: str, funds: float, **kwargs) -> Dict[str, Any]:
        """市價買入"""
        return self.place_order(symbol=symbol, side="buy", order_type="market", funds=funds, **kwargs)
    
    def sell_market(self, symbol: str, amount: float, **kwargs) -> Dict[str, Any]:
        """市價賣出"""
        return self.place_order(symbol=symbol, side="sell", order_type="market", amount=amount, **kwargs) 