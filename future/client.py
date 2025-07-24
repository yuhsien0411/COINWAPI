"""
CoinW 期貨統一客戶端

整合所有期貨功能到一個客戶端中
API 基礎: https://api.coinw.com/v1/perpum/
認證方式: HMAC SHA256 簽名
"""

from typing import Optional, List, Dict, Any, Union
from .http_manager import _ContractHTTPManager, ContractHTTPConfig
from .market import FutureMarket
from .order import FutureOrder
from .account import FutureAccount
from .position import FuturePosition


class FutureClient(_ContractHTTPManager):
    """
    CoinW 期貨統一客戶端
    
    整合期貨市場數據、交易和帳戶功能
    """
    
    def __init__(
        self,
        api_key: str,
        secret_key: str,
        config: Optional[ContractHTTPConfig] = None,
        **kwargs
    ):
        """
        初始化期貨客戶端
        
        Args:
            api_key: API密鑰
            secret_key: Secret密鑰
            config: HTTP配置
            **kwargs: 其他參數 (timeout, max_retries等)
        """
        if config is None:
            config = ContractHTTPConfig(
                base_url="https://api.coinw.com",
                timeout=kwargs.get('timeout', 30),
                max_retries=kwargs.get('max_retries', 3)
            )
        
        super().__init__(
            api_key=api_key,
            secret_key=secret_key,
            config=config
        )
        
        # 初始化功能模組
        self._market = FutureMarket(api_key, secret_key, config)
        self._order = FutureOrder(api_key, secret_key, config)
        self._account = FutureAccount(api_key, secret_key, config)
        self._position = FuturePosition(api_key, secret_key, config)
    
    # ==================== 公開市場數據代理 ====================
    
    def get_instruments(self, name: Optional[str] = None):
        """獲取合約產品信息"""
        return self._market.get_instruments(name)
    
    def get_ticker(self, instrument: str):
        """獲取合約ticker數據"""
        return self._market.get_ticker(instrument)
    
    def get_tickers(self):
        """獲取所有合約ticker數據"""
        return self._market.get_tickers()
    
    def get_klines(self, currency_code: str, granularity: str = "2", limit: Optional[int] = 100):
        """獲取合約K線數據"""
        return self._market.get_klines(currency_code, granularity, limit)

    def get_last_funding_rate(self, instrument: str):
        """獲取合約最新資金費率"""
        return self._market.get_last_funding_rate(instrument)

    def get_last_funding_rate(self, instrument: str):
        """獲取合約資金費率"""
        return self._market.get_last_funding_rate(instrument)

    def get_orderbook(self, instrument: str):
        """獲取合約訂單簿"""
        return self._market.get_orderbook(instrument)
    
    def get_trades(self, base: str):
        """獲取合約成交記錄"""
        return self._market.get_trades(base)
    
    # ==================== 私有市場數據代理 ====================
    
    def get_ladders(self):
        "取得所有合約的保證金要求"
        return self._market.get_ladders()
    
    def get_traders_history(self, instrument: str, page: int = 1, pageSize: int = 100):
        """獲取合約交易者歷史"""
        return self._market.get_traders_history(instrument, page, pageSize)
    

    # ==================== 交易代理 ====================
    
    def place_order(self, **kwargs):
        """期貨下單（根據CoinW官方API文檔）"""
        return self._order.place_order(**kwargs)
    
    def modify_order(self, order_id: str, **kwargs):
        """修改訂單"""
        return self._order.modify_order(order_id, **kwargs)
    
    def place_batch_orders(self, orders: List[Dict[str, Any]]):
        """批量下單"""
        return self._order.place_batch_orders(orders)
    
    def cancel_order(self, order_id: str):
        """取消合約訂單"""
        return self._order.cancel_order(order_id)
    
    def cancel_batch_orders(self, order_ids: List[str], pos_type: Optional[str] = None):
        """批量取消訂單"""
        return self._order.cancel_batch_orders(order_ids, pos_type)
    
    def get_order(self, position_type: str, **kwargs):
        """獲取訂單信息"""
        return self._order.get_order(position_type, **kwargs)
    
    def get_open_orders(
        self, 
        instrument: str, 
        position_type: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None
    ):
        """獲取當前訂單"""
        return self._order.get_open_orders(instrument, position_type, page, page_size)
    
    def get_pending_order_count(self):
        """獲取待處理訂單數量"""
        return self._order.get_pending_order_count()
    
    def get_order_history(
        self, 
        instrument: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None
    ):
        """獲取歷史訂單（7天）"""
        return self._order.get_order_history(instrument, page, page_size, origin_type)
    
    def get_order_archive(
        self, 
        instrument: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None
    ):
        """獲取歷史訂單（3個月）"""
        return self._order.get_order_archive(instrument, page, page_size, origin_type)
    
    # ==================== 平倉代理 ====================
    
    def close_position(self, position_id: str, **kwargs):
        """平倉"""
        return self._order.close_position(position_id, **kwargs)
    
    def close_all_positions(self, instrument: str):
        """市價平倉所有持倉"""
        return self._order.close_all_positions(instrument)
    
    def close_batch_positions(self, third_order_ids: List[str]):
        """批量平倉"""
        return self._order.close_batch_positions(third_order_ids)
    
    def reverse_position(self, position_id: str):
        """反向持倉"""
        return self._order.reverse_position(position_id)
    
    # ==================== 保證金管理代理 ====================
    
    def adjust_margin(
        self,
        position_id: str,
        add_margin: Optional[float] = None,
        reduce_margin: Optional[float] = None,
        type_: str = "all"
    ):
        """調整保證金"""
        return self._order.adjust_margin(position_id, add_margin, reduce_margin, type_)
    
    # ==================== 止損止盈代理 ====================
    
    def set_stop_loss_take_profit(
        self,
        order_or_position_id: str,
        **kwargs
    ):
        """設置止損/止盈"""
        return self._order.set_stop_loss_take_profit(order_or_position_id, **kwargs)
    
    def set_trailing_stop(
        self,
        position_id: str,
        callback_rate: float,
        quantity: float,
        **kwargs
    ):
        """設置追蹤止損/止盈"""
        return self._order.set_trailing_stop(position_id, callback_rate, quantity, **kwargs)
    
    def get_trailing_stop_info(self):
        """獲取追蹤止損/止盈信息"""
        return self._order.get_trailing_stop_info()
    
    def batch_set_stop_loss_take_profit(
        self,
        order_position_or_plan_id: str,
        stop_from: int,
        **kwargs
    ):
        """批量設置止損/止盈"""
        return self._order.batch_set_stop_loss_take_profit(order_position_or_plan_id, stop_from, **kwargs)
    
    def batch_modify_stop_loss_take_profit(
        self,
        order_position_or_plan_id: str,
        stop_from: int,
        **kwargs
    ):
        """批量修改止損/止盈"""
        return self._order.batch_modify_stop_loss_take_profit(order_position_or_plan_id, stop_from, **kwargs)
    
    def get_stop_loss_take_profit_info(
        self,
        stop_from: int,
        **kwargs
    ):
        """獲取止損/止盈信息"""
        return self._order.get_stop_loss_take_profit_info(stop_from, **kwargs)
    
    # ==================== 便利交易方法 ====================
    
    def buy_market(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨市價做多"""
        return self._order.buy_market(
            instrument, quantity, leverage, quantity_unit, position_model, **kwargs
        )
    
    def sell_market(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨市價做空"""
        return self._order.sell_market(
            instrument, quantity, leverage, quantity_unit, position_model, **kwargs
        )
    
    def buy_limit(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        price: float,
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨限價做多"""
        return self._order.buy_limit(
            instrument, quantity, price, leverage, quantity_unit, position_model, **kwargs
        )
    
    def sell_limit(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        price: float,
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨限價做空"""
        return self._order.sell_limit(
            instrument, quantity, price, leverage, quantity_unit, position_model, **kwargs
        )
    
    def buy_with_sl_tp(
        self,
        instrument: str,
        quantity: Union[float, str],
        price: float,
        leverage: int,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨限價做多（帶止損止盈）"""
        return self._order.buy_with_sl_tp(
            instrument, quantity, price, leverage, 
            stop_loss_price, stop_profit_price, quantity_unit, position_model, **kwargs
        )
    
    def sell_with_sl_tp(
        self,
        instrument: str,
        quantity: Union[float, str],
        price: float,
        leverage: int,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ):
        """期貨限價做空（帶止損止盈）"""
        return self._order.sell_with_sl_tp(
            instrument, quantity, price, leverage, 
            stop_loss_price, stop_profit_price, quantity_unit, position_model, **kwargs
        )
    
    # ==================== 帳戶代理 ====================
    
    def get_max_transferable_balance(self):
        """獲取最大可轉帳餘額"""
        return self._account.get_max_transferable_balance()
    
    def get_trade_details_3_days(
        self, 
        instrument: str, 
        page: Optional[int] = None, 
        page_size: Optional[int] = None, 
        origin_type: Optional[str] = None, 
        position_model: Optional[int] = None
    ):
        """獲取交易詳情（3天）"""
        return self._account.get_trade_details_3_days(instrument, page, page_size, origin_type, position_model)
    
    def get_trade_details_3_months(
        self, 
        instrument: str, 
        page: Optional[int] = None, 
        page_size: Optional[int] = None, 
        origin_type: Optional[str] = None, 
        position_model: Optional[int] = None
    ):
        """獲取交易詳情（3個月）"""
        return self._account.get_trade_details_3_months(instrument, page, page_size, origin_type, position_model)
    
    def get_user_assets(self):
        """獲取合約帳戶資產"""
        return self._account.get_user_assets()
    
    def get_account_fees(self):
        """獲取合約帳戶費用"""
        return self._account.get_account_fees()
    
    def get_almighty_gold_info(self, gold_type: int, start_time: Optional[int] = None, end_time: Optional[int] = None):
        """獲取萬能金餘額"""
        return self._account.get_almighty_gold_info(gold_type, start_time, end_time)
    
    def convert_units(
        self, 
        convert_type: int, 
        face_value: float, 
        deal_piece: Optional[float] = None, 
        base_size: Optional[float] = None
    ):
        """單位轉換"""
        return self._account.convert_units(convert_type, face_value, deal_piece, base_size)
    
    def get_margin_mode(self):
        """獲取保證金模式"""
        return self._account.get_margin_mode()
    
    def set_margin_mode(self, position_model: int, layout: str):
        """設置保證金模式"""
        return self._account.set_margin_mode(position_model, layout)
    
    def toggle_almighty_gold(self, status: str):
        """啟用/禁用萬能金"""
        return self._account.toggle_almighty_gold(status)
    
    def get_user_max_order_size(self, instrument: str):
        """獲取用戶最大合約規模"""
        return self._account.get_user_max_order_size(instrument)
    
    # ==================== 帳戶便利方法代理 ====================
    
    def get_unused_almighty_gold(self):
        """獲取未使用的萬能金"""
        return self._account.get_unused_almighty_gold()
    
    def get_expired_almighty_gold(self):
        """獲取已過期的萬能金"""
        return self._account.get_expired_almighty_gold()
    
    def enable_almighty_gold(self):
        """啟用萬能金"""
        return self._account.enable_almighty_gold()
    
    def disable_almighty_gold(self):
        """禁用萬能金"""
        return self._account.disable_almighty_gold()
    
    def convert_contracts_to_coins(self, deal_piece: float, face_value: float):
        """將合約張數轉換為幣數量"""
        return self._account.convert_contracts_to_coins(deal_piece, face_value)
    
    def convert_coins_to_contracts(self, base_size: float, face_value: float):
        """將幣數量轉換為合約張數"""
        return self._account.convert_coins_to_contracts(base_size, face_value)
    
    def set_cross_margin_mode(self, merge_positions: bool = True):
        """設置全倉保證金模式"""
        return self._account.set_cross_margin_mode(merge_positions)
    
    def set_isolated_margin_mode(self, merge_positions: bool = True):
        """設置逐倉保證金模式"""
        return self._account.set_isolated_margin_mode(merge_positions)
    
    def get_recent_trades_summary(self, instrument: str, days: int = 3):
        """獲取最近交易摘要"""
        return self._account.get_recent_trades_summary(instrument, days)
    
    def get_account_summary(self):
        """獲取帳戶摘要信息"""
        return self._account.get_account_summary()
    
    # ==================== 倉位代理 ====================
    
    def get_positions(self, instrument: str, open_ids: Optional[str] = None):
        """獲取當前持倉信息"""
        return self._position.get_positions(instrument, open_ids)
    
    def get_positions_history(self, instrument: Optional[str] = None, position_model: Optional[int] = None):
        """獲取歷史持倉信息"""
        return self._position.get_positions_history(instrument, position_model)
    
    def get_position_margin_rate(self, position_id: Optional[int] = None):
        """獲取持倉保證金率"""
        return self._position.get_position_margin_rate(position_id)
    
    def get_max_order_size(self, leverage: int, instrument: str, position_model: int, order_price: Optional[float] = None):
        """獲取最大合約規模"""
        return self._position.get_max_order_size(leverage, instrument, position_model, order_price)
    
    def get_all_positions(self):
        """獲取所有當前持倉"""
        return self._position.get_all_positions()
    
    def get_leverage_info(self, position_id: Optional[int] = None, order_id: Optional[int] = None):
        """獲取槓桿信息"""
        return self._position.get_leverage_info(position_id, order_id)

    # ==================== 便利持倉代理 ====================
    
    def get_position_by_id(self, instrument: str, position_id: str):
        """根據持倉ID獲取特定持倉信息"""
        return self._position.get_position_by_id(instrument, position_id)
    
    def get_positions_by_instrument(self, instrument: str):
        """獲取指定合約的所有持倉信息"""
        return self._position.get_positions_by_instrument(instrument)
    
    def get_cross_margin_positions_history(self):
        """獲取全倉保證金模式的歷史持倉信息"""
        return self._position.get_cross_margin_positions_history()
    
    def get_isolated_margin_positions_history(self):
        """獲取逐倉保證金模式的歷史持倉信息"""
        return self._position.get_isolated_margin_positions_history()
    
    def get_cross_margin_rate(self):
        """獲取全倉保證金率"""
        return self._position.get_cross_margin_rate()
    
    def get_isolated_margin_rate(self, position_id: int):
        """獲取逐倉保證金率"""
        return self._position.get_isolated_margin_rate(position_id)
    
    def get_leverage_info(self, position_id: Optional[int] = None, order_id: Optional[int] = None):
        """獲取槓桿信息"""
        return self._position.get_leverage_info(position_id, order_id)
    
    def get_position_leverage(self, position_id: int):
        """獲取已成交訂單（持倉）的槓桿信息"""
        return self._position.get_position_leverage(position_id)
    
    def get_order_leverage(self, order_id: int):
        """獲取未成交訂單的槓桿信息"""
        return self._position.get_order_leverage(order_id)
    
    def __repr__(self):
        return "CoinW Future API Client" 