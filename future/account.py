"""
CoinW 期貨帳戶模組

專門處理期貨/合約帳戶 API
端點格式: /v1/perpum/...
認證方式: HMAC SHA256 簽名
"""

from typing import Dict, Any, Optional
from .http_manager import _ContractHTTPManager
from ..exceptions import InvalidParameterError


class FutureAccount(_ContractHTTPManager):
    """期貨帳戶接口"""

    def get_max_transferable_balance(self) -> Dict[str, Any]:
        """
        獲取最大可轉帳餘額
        
        此接口允許查詢用戶合約帳戶中的最大可轉帳餘額。
        
        Returns:
            最大可轉帳餘額信息，包含：
            - data: 最大可轉帳金額
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/account/available",
            query={},
            auth=True
        )
    
    def get_trade_details_3_days(
        self,
        instrument: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None,
        position_model: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取交易詳情（3天）
        
        此接口允許查詢過去三天的全面交易詳情摘要，包括訂單狀態、持倉詳情、
        費用、盈虧、槓桿、保證金等關鍵交易指標。
        
        Args:
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。
            page: 當前頁碼（可選）
            page_size: 每頁響應數量（可選）
            origin_type: 初始訂單類型（可選）
                execute：市價單
                plan：用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單等
                planTrigger：計劃觸發訂單
            position_model: 持倉保證金模式（可選）
                0：逐倉保證金
                1：全倉保證金
        
        Returns:
            過去3天的交易詳情，包含詳細的訂單和持倉信息
        """
        query = {'instrument': instrument}
        
        if page is not None:
            query['page'] = page
        if page_size is not None:
            query['pageSize'] = page_size
        if origin_type:
            query['originType'] = origin_type
        if position_model is not None:
            if position_model not in [0, 1]:
                raise InvalidParameterError("position_model必須是 0（逐倉保證金）或 1（全倉保證金）")
            query['positionModel'] = position_model
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/deals",
            query=query,
            auth=True
        )
    
    def get_trade_details_3_months(
        self,
        instrument: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        origin_type: Optional[str] = None,
        position_model: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取交易詳情（3個月）
        
        此接口允許查詢過去三個月的全面交易詳情摘要，包括訂單狀態、持倉詳情、
        費用、盈虧、槓桿和保證金等關鍵交易指標。
        
        Args:
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。
            page: 當前頁碼（可選）
            page_size: 每頁響應數量（可選）
            origin_type: 初始訂單類型（可選）
                execute：市價單
                plan：用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單等
                planTrigger：計劃觸發訂單
            position_model: 持倉保證金模式（可選）
                0：逐倉保證金
                1：全倉保證金
        
        Returns:
            過去3個月的交易詳情，包含詳細的訂單和持倉信息
        """
        query = {'instrument': instrument}
        
        if page is not None:
            query['page'] = page
        if page_size is not None:
            query['pageSize'] = page_size
        if origin_type:
            query['originType'] = origin_type
        if position_model is not None:
            if position_model not in [0, 1]:
                raise InvalidParameterError("position_model必須是 0（逐倉保證金）或 1（全倉保證金）")
            query['positionModel'] = position_model
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/deals/history",
            query=query,
            auth=True
        )
    
    def get_user_assets(self) -> Dict[str, Any]:
        """
        獲取合約帳戶資產
        
        此接口允許用戶查詢合約帳戶資產信息，包括可用保證金、USDT餘額和凍結資產等。
        
        Returns:
            合約帳戶資產信息，包含：
            - availableMargin: 可用保證金餘額（包括萬能金）
            - userId: 合約帳戶用戶ID
            - almightyGold: 可用萬能金餘額
            - availableUsdt: 可用USDT餘額
            - alMargin: 持有資產（用於已成交訂單）
            - alFreeze: 凍結資產（用於未成交訂單）
            - time: 檢索響應數據的時間戳
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/account/getUserAssets",
            query={},
            auth=True
        )
    
    def get_account_fees(self) -> Dict[str, Any]:
        """
        獲取合約帳戶費用
        
        此接口允許查詢用戶的合約帳戶手續費率，包括maker和taker費用。
        
        Returns:
            合約帳戶費用信息，包含：
            - makerFee: maker費用
            - takerFee: taker費用
            - userId: 合約用戶ID
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/account/fees",
            query={},
            auth=True
        )
    
    def get_almighty_gold_info(
        self,
        gold_type: int,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取萬能金餘額
        
        此接口提供萬能金餘額信息，允許用戶根據時間範圍和狀態篩選數據。
        它提供萬能金餘額、狀態和有效期等關鍵詳情，實現高效的資產管理。
        
        Args:
            gold_type: 萬能金狀態（必填）
                0：待生效
                1：未使用
                2：已使用
                3：已過期
                4：發放失敗
            start_time: 有效期開始時間（可選）
            end_time: 有效期截止時間（可選）
        
        Returns:
            萬能金餘額信息，包含詳細的萬能金狀態和金額信息
        """
        query = {'type': gold_type}
        
        if start_time is not None:
            query['startTime'] = start_time
        if end_time is not None:
            query['endTime'] = end_time
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/account/almightyGoldInfo",
            query=query,
            auth=True
        )
    
    def convert_units(
        self,
        convert_type: int,
        face_value: float,
        deal_piece: Optional[float] = None,
        base_size: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        單位轉換
        
        此接口允許在合約交易中進行合約單位（張數）和加密貨幣（幣）之間的轉換。
        
        Args:
            convert_type: 轉換類型（必填）
                1：將合約單位（張數）轉換為幣
                2：將幣轉換為合約單位（張數）
            face_value: 每手最小價值（必填）
            deal_piece: 合約數量（convert_type=1時必需）
            base_size: 面值*份數（幣的數量）（convert_type=2時必需）
        
        Returns:
            轉換結果，包含：
            - value: 合約或幣的值
        """
        if convert_type not in [1, 2]:
            raise InvalidParameterError("convert_type必須是 1（張數轉幣）或 2（幣轉張數）")
        
        query = {
            'convertType': convert_type,
            'faceValue': face_value
        }
        
        if convert_type == 1:
            if deal_piece is None:
                raise InvalidParameterError("convert_type=1時，deal_piece是必需的")
            query['dealPiece'] = deal_piece
        elif convert_type == 2:
            if base_size is None:
                raise InvalidParameterError("convert_type=2時，base_size是必需的")
            query['baseSize'] = base_size
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/pieceConvert",
            query=query,
            auth=True
        )
    
    def get_margin_mode(self) -> Dict[str, Any]:
        """
        獲取保證金模式
        
        此接口允許查詢持倉保證金模式（逐倉或全倉）和持倉布局（合併或分開持倉），
        使用戶能夠有效管理其交易策略。
        
        Returns:
            保證金模式信息，包含：
            - layout: 持倉布局
                0：合併持倉（相同方向的持倉將被合併）
                1：分開持倉（相同方向的持倉將保持分離）
            - positionModel: 持倉保證金模式
                0：逐倉保證金
                1：全倉保證金
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions/type",
            query={},
            auth=True
        )
    
    def set_margin_mode(self, position_model: int, layout: str) -> Dict[str, Any]:
        """
        設置保證金模式
        
        此接口允許用戶將其持倉保證金模式配置為逐倉或全倉保證金，
        並通過選擇合併持倉（合併相同方向的新持倉）或分開持倉（保持新持倉分離）來設置持倉布局。
        
        注意：
        - 要將持倉保證金模式從逐倉更改為全倉或反之，用戶必須確保沒有未成交訂單
        - 要將持倉布局從合併持倉更改為分開持倉或反之，用戶必須確保沒有未成交訂單
        
        Args:
            position_model: 持倉保證金模式（必填）
                0：逐倉保證金
                1：全倉保證金
            layout: 持倉布局（必填）
                "0"：合併持倉（相同方向的持倉將被合併）
                "1"：分開持倉（相同方向的持倉將保持分離）
        
        Returns:
            設置結果，成功時返回 "TRANSACTION_SUCCESS"
        """
        if position_model not in [0, 1]:
            raise InvalidParameterError("position_model必須是 0（逐倉保證金）或 1（全倉保證金）")
        
        if layout not in ["0", "1"]:
            raise InvalidParameterError("layout必須是 '0'（合併持倉）或 '1'（分開持倉）")
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/positions/type",
            query={
                'positionModel': position_model,
                'layout': layout
            },
            auth=True
        )
    
    def toggle_almighty_gold(self, status: str) -> Dict[str, Any]:
        """
        啟用/禁用萬能金
        
        此接口允許用戶激活和停用萬能金。萬能金可用作合約交易中的保證金，
        抵消交易費用、虧損和資金成本。
        
        Args:
            status: 狀態（必填）
                "1"：開啟
                "0"：關閉
        
        Returns:
            操作結果，成功時返回 code: 0
        """
        if status not in ["0", "1"]:
            raise InvalidParameterError("status必須是 '1'（開啟）或 '0'（關閉）")
        
        return self._submit_request(
            method="POST",
            path="/v1/perpum/account/almightyGoldInfo",
            query={'status': status},
            auth=True
        )
    
    def get_user_max_order_size(self, instrument: str) -> Dict[str, Any]:
        """
        獲取用戶最大合約規模
        
        此接口允許用戶檢索其合約帳戶中已成交訂單的最大可用合約規模。
        用戶必須指定合約，響應將包括做多和做空持倉的最大合約規模。
        
        Args:
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。
        
        Returns:
            用戶最大合約規模信息，包含：
            - availBuy: 用戶可以平倉的做多方向的最大合約數量
            - availSell: 用戶可以平倉的做空方向的最大合約數量
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/availSize",
            query={'instrument': instrument},
            auth=True
        )
    
    # ==================== 便利方法 ====================
    
    def get_unused_almighty_gold(self) -> Dict[str, Any]:
        """
        獲取未使用的萬能金
        
        Returns:
            未使用的萬能金信息
        """
        return self.get_almighty_gold_info(gold_type=1)
    
    def get_expired_almighty_gold(self) -> Dict[str, Any]:
        """
        獲取已過期的萬能金
        
        Returns:
            已過期的萬能金信息
        """
        return self.get_almighty_gold_info(gold_type=3)
    
    def enable_almighty_gold(self) -> Dict[str, Any]:
        """
        啟用萬能金
        
        Returns:
            啟用結果
        """
        return self.toggle_almighty_gold(status="1")
    
    def disable_almighty_gold(self) -> Dict[str, Any]:
        """
        禁用萬能金
        
        Returns:
            禁用結果
        """
        return self.toggle_almighty_gold(status="0")
    
    def convert_contracts_to_coins(self, deal_piece: float, face_value: float) -> Dict[str, Any]:
        """
        將合約張數轉換為幣數量
        
        Args:
            deal_piece: 合約數量（張）
            face_value: 每張合約的面值
            
        Returns:
            轉換結果，包含幣的數量
        """
        return self.convert_units(
            convert_type=1,
            deal_piece=deal_piece,
            face_value=face_value
        )
    
    def convert_coins_to_contracts(self, base_size: float, face_value: float) -> Dict[str, Any]:
        """
        將幣數量轉換為合約張數
        
        Args:
            base_size: 幣的數量
            face_value: 每張合約的面值
            
        Returns:
            轉換結果，包含合約張數
        """
        return self.convert_units(
            convert_type=2,
            base_size=base_size,
            face_value=face_value
        )
    
    def set_cross_margin_mode(self, merge_positions: bool = True) -> Dict[str, Any]:
        """
        設置全倉保證金模式
        
        Args:
            merge_positions: 是否合併持倉，默認True
                True: 合併相同方向的持倉
                False: 分開持倉
        
        Returns:
            設置結果
        """
        layout = "0" if merge_positions else "1"
        return self.set_margin_mode(position_model=1, layout=layout)
    
    def set_isolated_margin_mode(self, merge_positions: bool = True) -> Dict[str, Any]:
        """
        設置逐倉保證金模式
        
        Args:
            merge_positions: 是否合併持倉，默認True
                True: 合併相同方向的持倉
                False: 分開持倉
        
        Returns:
            設置結果
        """
        layout = "0" if merge_positions else "1"
        return self.set_margin_mode(position_model=0, layout=layout)
    
    def get_recent_trades_summary(self, instrument: str, days: int = 3) -> Dict[str, Any]:
        """
        獲取最近交易摘要
        
        Args:
            instrument: 交易品種
            days: 天數，3或90（對應3天或3個月）
            
        Returns:
            交易摘要信息
        """
        if days <= 3:
            return self.get_trade_details_3_days(instrument, page=1, page_size=10)
        else:
            return self.get_trade_details_3_months(instrument, page=1, page_size=10)
    
    def get_account_summary(self) -> Dict[str, Any]:
        """
        獲取帳戶摘要信息
        
        整合多個接口，提供帳戶的完整概覽
        
        Returns:
            帳戶摘要，包含資產、費率、保證金模式等信息
        """
        try:
            summary = {}
            
            # 獲取帳戶資產
            assets = self.get_user_assets()
            if assets.get('code') == 0:
                summary['assets'] = assets['data']
            
            # 獲取手續費率
            fees = self.get_account_fees()
            if fees.get('code') == 0:
                summary['fees'] = fees['data']
            
            # 獲取保證金模式
            margin_mode = self.get_margin_mode()
            if margin_mode.get('code') == 0:
                summary['margin_mode'] = margin_mode['data']
            
            # 獲取最大可轉帳餘額
            max_transfer = self.get_max_transferable_balance()
            if max_transfer.get('code') == 0:
                summary['max_transferable'] = max_transfer['data']
            
            return {
                'code': 0,
                'data': summary,
                'msg': 'Account summary retrieved successfully'
            }
            
        except Exception as e:
            return {
                'code': -1,
                'data': None,
                'msg': f'Failed to get account summary: {str(e)}'
            } 