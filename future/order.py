"""
CoinW 期貨交易模組

專門處理期貨/合約交易 API
端點格式: /v1/perpum/...
認證方式: HMAC SHA256 簽名
"""

from typing import Dict, Any, Optional, List, Union
from .http_manager import _ContractHTTPManager
from ..exceptions import InvalidParameterError


class FutureOrder(_ContractHTTPManager):
    """期貨交易接口"""
    
    def place_order(
        self,
        instrument: str,
        direction: str,
        leverage: int,
        quantity_unit: int,
        quantity: Union[float, str],
        position_model: int,
        position_type: str,
        open_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        trigger_price: Optional[float] = None,
        trigger_type: Optional[int] = None,
        third_order_id: Optional[str] = None,
        use_almighty_gold: Optional[bool] = None,
        gold_id: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        期貨下單 (根據CoinW官方API文檔)
        
        Args:
            instrument: 合約的基礎貨幣（例如，BTC或btc）
            direction: 交易方向：做多(long)，做空(short)
            leverage: 持倉槓桿率
            quantity_unit: 訂單數量的計量單位：
                0：以計價貨幣計價（例如，BTC-USDT 合約中的 USDT）
                1：以合約張數計價
                2：以基礎貨幣計價（例如，BTC-USDT 合約中的 BTC）
            quantity: 基於quantity_unit指定訂單數量
            position_model: 持倉保證金模式：0：逐倉保證金，1：全倉保證金
            position_type: 訂單類型：
                execute：市價單
                plan：計劃訂單（限價單、觸發限價單、帶SL/TP的限價單等）
                planTrigger：計劃觸發訂單
            open_price: 指定訂單價格（計劃訂單必填）
            stop_loss_price: 止損價格（止損訂單必填）
            stop_profit_price: 止盈價格（止盈訂單必填）
            trigger_price: 計劃訂單的觸發價格
            trigger_type: 觸發價格滿足時的訂單類型：0：限價單，1：市價單
            third_order_id: 用戶分配的自定義訂單ID
            use_almighty_gold: 是否使用萬能金
            gold_id: 黃金ID
            **kwargs: 其他參數
            
        Returns:
            訂單信息
        """
        # 參數驗證
        if direction not in ["long", "short"]:
            raise InvalidParameterError("direction必須是 'long' 或 'short'")
        
        if quantity_unit not in [0, 1, 2]:
            raise InvalidParameterError("quantity_unit必須是 0, 1 或 2")
        
        if position_model not in [0, 1]:
            raise InvalidParameterError("position_model必須是 0（逐倉）或 1（全倉）")
        
        valid_position_types = ["execute", "plan", "planTrigger"]
        if position_type not in valid_position_types:
            raise InvalidParameterError(f"position_type必須是 {valid_position_types} 之一")
        
        # 構建請求參數
        data = {
            'instrument': instrument,
            'direction': direction,
            'leverage': leverage,
            'quantityUnit': quantity_unit,
            'quantity': str(quantity),
            'positionModel': position_model,
            'positionType': position_type
        }
        
        # 可選參數
        if open_price is not None:
            data['openPrice'] = open_price
            
        if stop_loss_price is not None:
            data['stopLossPrice'] = stop_loss_price
            
        if stop_profit_price is not None:
            data['stopProfitPrice'] = stop_profit_price
            
        if trigger_price is not None:
            data['triggerPrice'] = trigger_price
            
        if trigger_type is not None:
            data['triggerType'] = trigger_type
            
        if third_order_id:
            data['thirdOrderId'] = third_order_id
            
        if use_almighty_gold is not None:
            data['useAlmightyGold'] = use_almighty_gold
            
        if gold_id is not None:
            data['goldId'] = gold_id
        
        # 添加其他參數
        data.update(kwargs)
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/order",
            query=data,
            auth=True
        )
    
    def modify_order(
        self,
        order_id: str,
        instrument: str,
        direction: str,
        leverage: int,
        quantity_unit: int,
        quantity: Union[float, str],
        position_model: int,
        position_type: str,
        open_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        trigger_price: Optional[float] = None,
        trigger_type: Optional[int] = None,
        third_order_id: Optional[str] = None,
        use_almighty_gold: Optional[bool] = None,
        gold_id: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        修改訂單
        
        Args:
            order_id: 要修改的訂單ID
            其他參數與place_order相同
            
        Returns:
            修改結果，包含原始訂單ID和新訂單ID
        """
        # 參數驗證
        if direction not in ["long", "short"]:
            raise InvalidParameterError("direction必須是 'long' 或 'short'")
        
        if quantity_unit not in [0, 1, 2]:
            raise InvalidParameterError("quantity_unit必須是 0, 1 或 2")
        
        if position_model not in [0, 1]:
            raise InvalidParameterError("position_model必須是 0（逐倉）或 1（全倉）")
        
        valid_position_types = ["execute", "plan", "planTrigger"]
        if position_type not in valid_position_types:
            raise InvalidParameterError(f"position_type必須是 {valid_position_types} 之一")
        
        # 構建請求參數
        data = {
            'id': order_id,
            'instrument': instrument,
            'direction': direction,
            'leverage': leverage,
            'quantityUnit': quantity_unit,
            'quantity': str(quantity),
            'positionModel': position_model,
            'positionType': position_type
        }
        
        # 可選參數
        if open_price is not None:
            data['openPrice'] = open_price
            
        if stop_loss_price is not None:
            data['stopLossPrice'] = stop_loss_price
            
        if stop_profit_price is not None:
            data['stopProfitPrice'] = stop_profit_price
            
        if trigger_price is not None:
            data['triggerPrice'] = trigger_price
            
        if trigger_type is not None:
            data['triggerType'] = trigger_type
            
        if third_order_id:
            data['thirdOrderId'] = third_order_id
            
        if use_almighty_gold is not None:
            data['useAlmightyGold'] = use_almighty_gold
            
        if gold_id is not None:
            data['goldId'] = gold_id
        
        # 添加其他參數
        data.update(kwargs)
        
        return self._submit_request(
            method="PUT",
            path="/v1/perpum/order",
            query=data,
            auth=True
        )
    
    def place_batch_orders(self, orders: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        批量下單
        
        Args:
            orders: 訂單列表，每個訂單包含必要參數
            
        Returns:
            批量下單結果
        """
        return self._submit_request(
            method="POST",
            path="/v1/perpum/batchOrders",
            query=orders,
            auth=True
        )
    
    def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """
        取消合約訂單
        
        Args:
            order_id: 訂單ID
            
        Returns:
            取消結果
        """
        data = {'id': order_id}
        
        return self._submit_request(
            method="DELETE",
            path="/v1/perpum/order",
            query=data,
            auth=True
        )
    
    def cancel_batch_orders(self, order_ids: List[str], pos_type: Optional[str] = None) -> Dict[str, Any]:
        """
        批量取消訂單
        
        Args:
            order_ids: 訂單ID列表
            pos_type: 持倉類型（可選）
                execute: 市價單
                plan: 限價單
                moveStop: 移動止損和止盈訂單
                stopProfitLoss: 止損和止盈訂單
            
        Returns:
            批量取消結果
        """
        data = {'sourceIds': order_ids}
        
        if pos_type:
            data['posType'] = pos_type
        
        return self._submit_request(
            method="DELETE",
            path="/v1/perpum/batchOrders",
            query=data,
            auth=True
        )
    
    def get_order(
        self, 
        position_type: str,
        source_ids: Optional[str] = None,
        instrument: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取訂單信息
        
        根據trade2.md文檔，此接口提供當前未成交訂單的信息。
        用戶可以指定訂單ID列表來查詢特定訂單。
        
        Args:
            position_type: 訂單類型（必填）
                execute: 市價單
                plan: 計劃單
                moveStop: 追蹤止損和止盈
                stopProfitLoss: 止損和止盈
            source_ids: 以逗號分隔的訂單ID列表（例如："orderId1,orderId2,orderId3"）
                注意：訂單ID數量不能超過20個
            instrument: 合約代碼（可選）
            
        Returns:
            訂單詳情
        """
        query = {'positionType': position_type}
        
        if source_ids:
            query['sourceIds'] = source_ids
        if instrument:
            query['instrument'] = instrument
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/order",
            query=query,
            auth=True
        )
    
    def get_open_orders(
        self, 
        instrument: str,
        position_type: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取當前訂單
        
        此接口允許查詢指定合約和訂單類型的未成交訂單詳情，
        包括合約、方向、數量、數量單位、保證金、槓桿、maker費用、taker費用和時間戳。
        
        Args:
            instrument: 合約代碼（必填）
            position_type: 訂單類型（必填）
                plan: 計劃訂單
                execute: 市價單
                planTrigger: 計劃觸發訂單
                moveStopProfitLoss: 追蹤止損/止盈
            page: 當前頁碼（可選）
            page_size: 每頁記錄數（可選）
            
        Returns:
            未完成訂單列表
        """
        query = {
            'instrument': instrument,
            'positionType': position_type
        }
        
        if page is not None:
            query['page'] = page
        
        if page_size is not None:
            query['pageSize'] = page_size
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/open",
            query=query,
            auth=True
        )
    
    def get_pending_order_count(self) -> Dict[str, Any]:
        """
        獲取待處理訂單數量
        
        此接口允許查詢未成交訂單的總數，即待處理訂單。
        
        Returns:
            待處理訂單數量
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/openQuantity",
            query={},
            auth=True
        )
    
    def get_order_history(
        self, 
        instrument: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取歷史訂單（7天）
        
        此接口提供過去七天的歷史訂單記錄。用戶可以使用頁碼、頁面大小、
        訂單類型和交易合約等參數篩選結果。
        
        Args:
            instrument: 合約代碼（可選）
            page: 當前頁碼（可選）
            page_size: 每頁結果數（可選）
                注意：如果未指定，接口將返回過去七天內最近10個訂單的信息
            origin_type: 初始訂單類型（可選）
                plan: 用於不同計劃訂單
                planTrigger: 計劃觸發訂單
                execute: 市價單
            
        Returns:
            歷史訂單列表
        """
        query = {}
        
        if instrument:
            query['instrument'] = instrument
        
        if page is not None:
            query['page'] = page
        
        if page_size is not None:
            query['pageSize'] = page_size
        
        if origin_type:
            query['originType'] = origin_type
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/history",
            query=query,
            auth=True
        )
    
    def get_order_archive(
        self, 
        instrument: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取歷史訂單（3個月）
        
        此接口提供過去三個月的歷史訂單記錄。用戶可以使用頁碼、頁面大小、
        訂單類型和交易合約等參數篩選結果。
        
        Args:
            instrument: 合約代碼（可選）
            page: 當前頁碼（可選）
            page_size: 每頁結果數（可選）
                注意：如果未指定，接口將返回過去三個月內最近10個訂單的信息
            origin_type: 初始訂單類型（可選）
                plan: 用於不同計劃訂單
                planTrigger: 計劃觸發訂單
                execute: 市價單
            
        Returns:
            歷史訂單列表
        """
        query = {}
        
        if instrument:
            query['instrument'] = instrument
        
        if page is not None:
            query['page'] = page
        
        if page_size is not None:
            query['pageSize'] = page_size
        
        if origin_type:
            query['originType'] = origin_type
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/archive",
            query=query,
            auth=True
        )
    
    def close_position(
        self,
        position_id: str,
        position_type: str = "execute",
        close_rate: Optional[float] = None,
        close_num: Optional[float] = None,
        order_price: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        平倉
        
        Args:
            position_id: 持倉ID 系統回傳 or 用戶自定義
            position_type: 指定平倉訂單類型
                plan: 以指定價格平倉
                execute: 以市價平倉（默認）
            close_rate: 平倉比例，有效範圍從0到1（與close_num互斥）
            close_num: 要平倉的合約數量（與close_rate互斥）
            order_price: 指定平倉價格（如果指定，position_type必須設為plan）
            
        Returns:
            平倉結果
        """
        if close_rate is None and close_num is None:
            raise InvalidParameterError("必須提供 close_rate 或 close_num")
        
        if close_rate is not None and close_num is not None:
            raise InvalidParameterError("close_rate 和 close_num 互斥，只能提供其中一個")
        
        data = {
            'id': position_id,
            'positionType': position_type
        }
        
        if close_rate is not None:
            data['closeRate'] = close_rate
        
        if close_num is not None:
            data['closeNum'] = close_num
            
        if order_price is not None:
            if position_type != "plan":
                raise InvalidParameterError("如果指定order_price，position_type必須設為plan")
            data['orderPrice'] = order_price
        
        return self._submit_request(
            method="DELETE",
            path="/v1/perpum/positions",
            query=data,
            auth=True
        )
    
    def close_all_positions(self, instrument: str) -> Dict[str, Any]:
        """
        市價平倉所有持倉
        
        Args:
            instrument: 合約代碼
            
        Returns:
            平倉結果
        """
        data = {'instrument': instrument}
        
        return self._submit_request(
            method="DELETE",
            path="/v1/perpum/allpositions",
            query=data,
            auth=True
        )
    
    def close_batch_positions(self, third_order_ids: List[str]) -> Dict[str, Any]:
        """
        批量平倉
        
        Args:
            third_order_ids: 自定義訂單ID列表
            
        Returns:
            批量平倉結果
        """
        orders = [{"thirdOrderId": third_order_id} for third_order_id in third_order_ids]
        
        return self._submit_request(
            method="DELETE",
            path="/v1/perpum/batchClose",
            query=orders,
            auth=True
        )
    
    def reverse_position(self, position_id: str) -> Dict[str, Any]:
        """
        反向持倉
        
        此接口允許用戶即時反轉現有永續合約持倉。通過指定持倉ID，
        系統將平倉當前持倉，並以相同持倉大小在相反方向開設新持倉。
        
        Args:
            position_id: 持倉ID
            
        Returns:
            反向持倉結果，包含新訂單ID
        """
        data = {'id': position_id}
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/positions/reverse",
            query=data,
            auth=True
        )
    
    def adjust_margin(
        self,
        position_id: str,
        add_margin: Optional[float] = None,
        reduce_margin: Optional[float] = None,
        type_: str = "all"
    ) -> Dict[str, Any]:
        """
        調整保證金
        
        Args:
            position_id: 持倉ID
            add_margin: 要增加的保證金金額（必須大於0）
            reduce_margin: 要減少的保證金金額（必須大於0）
            type_: 指定余額查詢範圍
                all: 包括余額和萬能金
                almightyGold: 僅萬能金
                balance: 僅余額
            
        Returns:
            調整結果
        """
        if add_margin is None and reduce_margin is None:
            raise InvalidParameterError("必須提供 add_margin 或 reduce_margin")
        
        if add_margin is not None and reduce_margin is not None:
            raise InvalidParameterError("add_margin 和 reduce_margin 互斥，只能提供其中一個")
        
        data = {
            'id': position_id,
            'type': type_
        }
        
        if add_margin is not None:
            if add_margin <= 0:
                raise InvalidParameterError("add_margin 必須大於0")
            data['addMargin'] = add_margin
        
        if reduce_margin is not None:
            if reduce_margin <= 0:
                raise InvalidParameterError("reduce_margin 必須大於0")
            data['reduceMargin'] = reduce_margin
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/positions/margin",
            query=data,
            auth=True
        )
    
    def set_stop_loss_take_profit(
        self,
        order_or_position_id: str,
        instrument: Optional[str] = None,
        stop_loss_order_price: Optional[float] = None,
        stop_profit_order_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        stop_loss_rate: Optional[float] = None,
        stop_profit_rate: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        設置止損/止盈
        
        此接口允許用戶為已成交和未成交訂單設置止盈(TP)和止損(SL)。
        
        Args:
            order_or_position_id: 訂單ID（對於未成交訂單）或持倉ID（對於已成交訂單）
            instrument: 合約代碼
            stop_loss_order_price: 止損限價
            stop_profit_order_price: 止盈限價
            stop_loss_price: 止損價格
            stop_profit_price: 止盈價格
            stop_loss_rate: 止損率
            stop_profit_rate: 止盈率
            
        Returns:
            設置結果
        """
        data = {'id': order_or_position_id}
        
        if instrument:
            data['instrument'] = instrument
        
        if stop_loss_order_price is not None:
            data['stopLossOrderPrice'] = stop_loss_order_price
        
        if stop_profit_order_price is not None:
            data['stopProfitOrderPrice'] = stop_profit_order_price
        
        if stop_loss_price is not None:
            data['stopLossPrice'] = stop_loss_price
        
        if stop_profit_price is not None:
            data['stopProfitPrice'] = stop_profit_price
        
        if stop_loss_rate is not None:
            data['stopLossRate'] = stop_loss_rate
        
        if stop_profit_rate is not None:
            data['stopProfitRate'] = stop_profit_rate
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/TPSL",
            query=data,
            auth=True
        )
    
    def set_trailing_stop(
        self,
        position_id: str,
        callback_rate: float,
        quantity: float,
        trigger_price: Optional[float] = None,
        quantity_unit: int = 1
    ) -> Dict[str, Any]:
        """
        設置追蹤止損/止盈
        
        此接口允許用戶根據指定的回調率配置追蹤止損(SL)和止盈(TP)機制，
        僅適用於已成交訂單。
        
        Args:
            position_id: 持倉ID
            callback_rate: 回調率，有效範圍從0到1（例如：0.5表示50%的回調率）
            quantity: 合約/USDT數量
            trigger_price: 激活價格（可選）
            quantity_unit: 指定數量單位
                0: 以USDT計價
                1: 以合約計價（默認）
            
        Returns:
            設置結果
        """
        if not (0 <= callback_rate <= 1):
            raise InvalidParameterError("callback_rate必須在0到1之間")
        
        data = {
            'openId': position_id,
            'callbackRate': str(callback_rate),
            'quantity': quantity,
            'quantityUnit': quantity_unit
        }
        
        if trigger_price is not None:
            data['triggerPrice'] = trigger_price
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/moveTPSL",
            query=data,
            auth=True
        )
    
    def get_trailing_stop_info(self) -> Dict[str, Any]:
        """
        獲取追蹤止損/止盈信息
        
        此接口允許查詢合約交易的追蹤止損和止盈詳情。
        
        Returns:
            追蹤止損/止盈信息
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/moveTPSL",
            query={},
            auth=True
        )
    
    def batch_set_stop_loss_take_profit(
        self,
        order_position_or_plan_id: str,
        stop_from: int,
        instrument: Optional[str] = None,
        stop_loss_order_price: Optional[float] = None,
        stop_profit_order_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        stop_loss_rate: Optional[float] = None,
        stop_profit_rate: Optional[float] = None,
        price_type: int = 3,
        stop_type: int = 2,
        close_piece: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        批量設置止損/止盈
        
        Args:
            order_position_or_plan_id: 訂單ID/持倉ID/計劃ID
            stop_from: 止盈/止損觸發後的訂單類型
                1: 限價單（在id參數中提供訂單ID）
                2: 市價單（在id參數中提供持倉ID）
                3: 條件單（在id參數中提供計劃ID）
            instrument: 合約代碼
            stop_loss_order_price: 止損限價
            stop_profit_order_price: 止盈限價
            stop_loss_price: 止損價格
            stop_profit_price: 止盈價格
            stop_loss_rate: 止損率
            stop_profit_rate: 止盈率
            price_type: 止盈和止損觸發價格類型
                1: 指數價格
                2: 最新價格
                3: 標記價格（默認）
            stop_type: 止損/止盈類型
                1: 批量止盈/止損（僅適用於未成交訂單）
                2: 整個持倉止盈/止損（僅適用於已成交訂單，默認）
            close_piece: 止盈和止損合約數量（批量止盈/止損必填）
            
        Returns:
            設置結果
        """
        data = {
            'id': order_position_or_plan_id,
            'stopFrom': stop_from,
            'priceType': price_type,
            'stopType': stop_type
        }
        
        if instrument:
            data['instrument'] = instrument
        
        if stop_loss_order_price is not None:
            data['stopLossOrderPrice'] = stop_loss_order_price
        
        if stop_profit_order_price is not None:
            data['stopProfitOrderPrice'] = stop_profit_order_price
        
        if stop_loss_price is not None:
            data['stopLossPrice'] = stop_loss_price
        
        if stop_profit_price is not None:
            data['stopProfitPrice'] = stop_profit_price
        
        if stop_loss_rate is not None:
            data['stopLossRate'] = stop_loss_rate
        
        if stop_profit_rate is not None:
            data['stopProfitRate'] = stop_profit_rate
        
        if close_piece is not None:
            data['closePiece'] = close_piece
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/addTpsl",
            query=data,
            auth=True
        )
    
    def batch_modify_stop_loss_take_profit(
        self,
        order_position_or_plan_id: str,
        stop_from: int,
        instrument: Optional[str] = None,
        stop_profit_order_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
        stop_profit_price: Optional[float] = None,
        stop_loss_rate: Optional[float] = None,
        stop_profit_rate: Optional[float] = None,
        price_type: int = 3,
        stop_type: int = 2,
        close_piece: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        批量修改止損/止盈
        
        Args:
            order_position_or_plan_id: 訂單ID/持倉ID/計劃ID
            stop_from: 止盈/止損觸發後的訂單類型
                1: 限價單
                2: 市價單
                3: 條件單
            instrument: 合約代碼
            stop_profit_order_price: 止盈限價
            stop_loss_price: 止損價格
            stop_profit_price: 止盈價格
            stop_loss_rate: 止損率
            stop_profit_rate: 止盈率
            price_type: 止盈和止損觸發價格類型
                1: 指數價格
                2: 最新價格
                3: 標記價格（默認）
            stop_type: 止損/止盈類型
                1: 批量止盈/止損
                2: 整個持倉止盈/止損（默認）
            close_piece: 止盈/止損合約數量（批量止盈/止損必填）
            
        Returns:
            修改結果
        """
        data = {
            'id': order_position_or_plan_id,
            'stopFrom': stop_from,
            'priceType': price_type,
            'stopType': stop_type
        }
        
        if instrument:
            data['instrument'] = instrument
        
        if stop_profit_order_price is not None:
            data['stopProfitOrderPrice'] = stop_profit_order_price
        
        if stop_loss_price is not None:
            data['stopLossPrice'] = stop_loss_price
        
        if stop_profit_price is not None:
            data['stopProfitPrice'] = stop_profit_price
        
        if stop_loss_rate is not None:
            data['stopLossRate'] = stop_loss_rate
        
        if stop_profit_rate is not None:
            data['stopProfitRate'] = stop_profit_rate
        
        if close_piece is not None:
            data['closePiece'] = close_piece
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/updateTpsl",
            query=data,
            auth=True
        )
    
    def get_stop_loss_take_profit_info(
        self,
        stop_from: int,
        instrument: Optional[str] = None,
        order_id: Optional[str] = None,
        position_id: Optional[str] = None,
        plan_order_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取止損/止盈信息
        
        此接口允許查詢合約交易中已成交和未成交訂單的止損(SL)和止盈(TP)信息。
        
        Args:
            stop_from: 止損和止盈訂單類型（必填）
                1: 需要"plan"訂單的訂單ID
                2: 需要"execute"市場的倉位ID
                3: 需要"planTrigger"訂單的計劃訂單ID
                注意: 根據訂單類型，必須指定相應的ID
            instrument: 合約代碼（可選）
            order_id: 訂單ID（可選）
            position_id: 持倉ID（可選）
            plan_order_id: 計劃訂單ID（可選）
            
        Returns:
            止損/止盈信息
        """
        query = {'stopFrom': stop_from}
        
        if instrument:
            query['instrument'] = instrument
        
        if order_id:
            query['orderId'] = order_id
        
        if position_id:
            query['openId'] = position_id
        
        if plan_order_id:
            query['planOrderId'] = plan_order_id
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/TPSL",
            query=query,
            auth=True
        )
    
    # 便利方法
    def buy_market(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ) -> Dict[str, Any]:
        """期貨市價做多"""
        return self.place_order(
            instrument=instrument,
            direction="long",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="execute",
            **kwargs
        )
    
    def sell_market(
        self, 
        instrument: str, 
        quantity: Union[float, str],
        leverage: int,
        quantity_unit: int = 0,
        position_model: int = 1,
        **kwargs
    ) -> Dict[str, Any]:
        """期貨市價做空"""
        return self.place_order(
            instrument=instrument,
            direction="short",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="execute",
            **kwargs
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
    ) -> Dict[str, Any]:
        """期貨限價做多"""
        return self.place_order(
            instrument=instrument,
            direction="long",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="plan",
            open_price=price,
            **kwargs
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
    ) -> Dict[str, Any]:
        """期貨限價做空"""
        return self.place_order(
            instrument=instrument,
            direction="short",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="plan",
            open_price=price,
            **kwargs
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
    ) -> Dict[str, Any]:
        """期貨限價做多（帶止損止盈）"""
        return self.place_order(
            instrument=instrument,
            direction="long",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="plan",
            open_price=price,
            stop_loss_price=stop_loss_price,
            stop_profit_price=stop_profit_price,
            **kwargs
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
    ) -> Dict[str, Any]:
        """期貨限價做空（帶止損止盈）"""
        return self.place_order(
            instrument=instrument,
            direction="short",
            leverage=leverage,
            quantity_unit=quantity_unit,
            quantity=quantity,
            position_model=position_model,
            position_type="plan",
            open_price=price,
            stop_loss_price=stop_loss_price,
            stop_profit_price=stop_profit_price,
            **kwargs
        ) 