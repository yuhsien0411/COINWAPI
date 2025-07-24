"""
CoinW 現貨統一客戶端

整合所有現貨功能到一個客戶端中
API 基礎: https://api.coinw.com/api/v1/
認證方式: MD5 簽名
"""

from typing import Optional
from .market import SpotMarket
from .order import SpotOrder
from .account import SpotAccount


class SpotClient:
    """
    CoinW 現貨統一客戶端
    
    整合現貨市場數據、交易和帳戶功能
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        base_url: str = "https://api.coinw.com",
        timeout: int = 30,
        max_retries: int = 3,
        **kwargs
    ):
        """
        初始化現貨客戶端
        
        Args:
            api_key: API密鑰
            secret_key: Secret密鑰
            base_url: API基礎URL
            timeout: 請求超時時間
            max_retries: 最大重試次數
            **kwargs: 其他參數
        """
        # 初始化功能模組
        self._market = SpotMarket(
            api_key=api_key,
            secret_key=secret_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries
        )
        
        # 交易和帳戶模組需要認證
        if api_key and secret_key:
            self._order = SpotOrder(
                api_key=api_key,
                secret_key=secret_key,
                base_url=base_url,
                timeout=timeout,
                max_retries=max_retries
            )
            self._account = SpotAccount(
                api_key=api_key,
                secret_key=secret_key,
                base_url=base_url,
                timeout=timeout,
                max_retries=max_retries
            )
        else:
            self._order = None
            self._account = None
    
    # ==================== 市場數據代理 ====================
    
    def get_ticker(self, symbol: Optional[str] = None):
        """獲取現貨ticker數據"""
        return self._market.get_ticker(symbol)
    
    def get_orderbook(self, symbol: str, size: int = 5):
        """
        獲取現貨訂單簿
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            size: 深度級別，只支援 5 或 20，預設 5
        """
        return self._market.get_orderbook(symbol, size)
    
    def get_orders(self, symbol: str, start: Optional[str] = None, end: Optional[str] = None):
        """
        獲取現貨成交記錄
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            start: 開始時間戳（可選）
            end: 結束時間戳（可選）
        """
        return self._market.get_orders(symbol, start, end)
    
    def get_symbols(self):
        """獲取現貨交易對信息"""
        return self._market.get_symbols()
    
    def get_currencies(self):
        """獲取幣種信息"""
        return self._market.get_currencies()
    
    def get_24hr_volume(self):
        """獲取24小時成交量統計"""
        return self._market.get_24hr_volume()
    
    def get_kline(self, symbol: str, period: int, start: Optional[str] = None, end: Optional[str] = None):
        """
        獲取K線數據
        
        Args:
            symbol: 交易對，如 "BTC_USDT"
            period: 時間週期（秒），如 300=5分鐘, 900=15分鐘, 1800=30分鐘
            start: 開始時間戳（Unix 毫秒級，可選）
            end: 結束時間戳（Unix 毫秒級，可選）
        """
        return self._market.get_kline(symbol, period, start, end)
    
    def get_server_time(self):
        """獲取服務器時間"""
        return self._market.get_server_time()
    
    # ==================== 交易代理 ====================
    
    def place_order(self, **kwargs):
        """現貨下單"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.place_order(**kwargs)
    
    def cancel_order(self, order_id: str):
        """取消現貨訂單"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.cancel_order(order_id)
    
    def cancel_all_orders(self, symbol: Optional[str] = None):
        """取消所有訂單"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.cancel_all_orders(symbol)
    
    def get_order(self, order_id: str):
        """獲取現貨訂單詳情"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.get_order(order_id)
    
    def get_order_status(self, order_id: str):
        """獲取訂單狀態"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.get_order_status(order_id)
    
    def get_open_orders(self, symbol: str, **kwargs):
        """
        獲取現貨未完成訂單
        
        Args:
            symbol: 交易對，必填
            **kwargs: 其他參數如 start_at, end_at
        """
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.get_open_orders(symbol, **kwargs)
    
    def get_order_history(self, symbol: str, **kwargs):
        """
        獲取交易歷史
        
        Args:
            symbol: 交易對，必填
            **kwargs: 其他參數如 start_at, end_at
        """
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.get_order_history(symbol, **kwargs)
    
    def get_order_history(self, **kwargs):
        """
        獲取現貨訂單歷史
        
        Args:
            **kwargs: 參數如 symbol, start_at, end_at, limit, before, after
        """
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.get_order_history(**kwargs)
    
    def buy_limit(self, symbol: str, amount: float, price: float, **kwargs):
        """現貨限價買入"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.buy_limit(symbol, amount, price, **kwargs)
    
    def sell_limit(self, symbol: str, amount: float, price: float, **kwargs):
        """現貨限價賣出"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.sell_limit(symbol, amount, price, **kwargs)
    
    def buy_market(self, symbol: str, funds: float, **kwargs):
        """現貨市價買入"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.buy_market(symbol, funds, **kwargs)
    
    def sell_market(self, symbol: str, amount: float, **kwargs):
        """現貨市價賣出"""
        if not self._order:
            raise ValueError("交易功能需要設置 api_key 和 secret_key")
        return self._order.sell_market(symbol, amount, **kwargs)
    
    # ==================== 帳戶代理 ====================
    
    def get_balance(self):
        """獲取現貨帳戶餘額"""
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.get_balance()
    
    def get_full_balance(self):
        """獲取完整帳戶餘額"""
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.get_full_balance()
    
    def get_deposit_address(self, symbol_id: str, chain: str):
        """
        獲取充值地址
        
        Args:
            symbol_id: 幣種ID，如 BTC 的 ID 是 "50"
            chain: 區塊鏈名稱，如 "BTC"
        """
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.get_deposit_address(symbol_id, chain)
    
    def get_deposit_history(self, symbol: str, **kwargs):
        """
        獲取充值和提現歷史
        
        Args:
            symbol: 交易品種的基礎貨幣，如 "BTC"
            **kwargs: 其他參數如 deposit_number
        """
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.get_deposit_history(symbol, **kwargs)
    
    def withdraw(self, currency: str, amount: float, address: str, chain: str, **kwargs):
        """
        發起提現
        
        Args:
            currency: 幣種名稱
            amount: 提現數量
            address: 提現地址
            chain: 區塊鏈名稱
            **kwargs: 其他參數如 memo, withdraw_type, inner_to_type
        """
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.withdraw(currency, amount, address, chain, **kwargs)
    
    def cancel_withdraw(self, withdraw_id: str):
        """取消提現"""
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.cancel_withdraw(withdraw_id)
    
    def transfer(self, account_type: str, target_account_type: str, biz_type: str, coin_code: str, amount: float):
        """
        資產轉賬
        
        Args:
            account_type: 源帳戶類型（WEALTH=資金帳戶, SPOT=現貨帳戶）
            target_account_type: 目標帳戶類型（WEALTH=資金帳戶, SPOT=現貨帳戶）
            biz_type: 轉賬方向（WEALTH_TO_SPOT 或 SPOT_TO_WEALTH）
            coin_code: 幣種代碼，如 "BTC"
            amount: 轉賬數量
        """
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.transfer(account_type, target_account_type, biz_type, coin_code, amount)
    
    def internal_transfer(self, currency: str, amount: float, address: str, **kwargs):
        """
        內部轉賬
        
        Args:
            currency: 幣種
            amount: 數量
            address: 目標用戶郵箱或ID
            **kwargs: 其他參數如 chain, inner_to_type
        """
        if not self._account:
            raise ValueError("帳戶功能需要設置 api_key 和 secret_key")
        return self._account.internal_transfer(currency, amount, address, **kwargs) 