"""
CoinW 期貨倉位模組

專門處理期貨/合約倉位相關 API
端點格式: /v1/perpum/...
認證方式: HMAC SHA256 簽名
"""

from typing import Dict, Any, Optional, List
from .http_manager import _ContractHTTPManager
from ..exceptions import InvalidParameterError


class FuturePosition(_ContractHTTPManager):
    """期貨倉位接口"""
    
    def get_positions(
        self, 
        instrument: str, 
        open_ids: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取當前持倉信息
        
        此接口允許用戶通過指定合約查詢當前開倉持倉（已成交訂單）的信息。
        用戶還可以通過提供一個或多個持倉ID來檢索特定持倉的詳情。
        
        Args:
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。
            open_ids: 一個或多個以逗號(,)分隔的持倉ID。例如：'positionId1,positionId2,positionId3'
                注意：持倉ID數量不能超過20個。（可選）
        
        Returns:
            當前持倉信息，包含：
            - id: 持倉ID
            - base: 合約基礎貨幣
            - baseSize: 合約面值
            - createdDate: 持倉創建時間戳
            - currentPiece: 當前持倉張數
            - direction: 交易方向（long/short）
            - fee: 資金費
            - fundingSettle: 已結算資金費
            - indexPrice: 觸發時的指數價格
            - instrument: 交易品種的基礎貨幣
            - leverage: 持倉槓桿率
            - margin: 持倉使用的保證金
            - openPrice: 持倉開倉價格
            - positionMargin: 持倉保證金
            - positionModel: 倉位模式（0：逐倉，1：全倉）
            - quantity: 訂單數量
            - quantityUnit: 數量計量單位
            - status: 狀態（open/close）
            - totalPiece: 合約總張數
            - profitUnreal: 未實現盈虧
            等等...
        """
        query = {'instrument': instrument}
        
        if open_ids:
            query['openIds'] = open_ids
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions",
            query=query,
            auth=True
        )
    
    def get_positions_history(
        self, 
        instrument: Optional[str] = None,
        position_model: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取歷史持倉信息
        
        此接口允許查詢所有歷史持倉（已成交訂單）。
        用戶可以指定合約的基礎貨幣和持倉保證金來檢索更具體的詳情。
        
        Args:
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。（可選）
            position_model: 保證金模式（可選）
                0：逐倉保證金
                1：全倉保證金
        
        Returns:
            歷史持倉信息，包含：
            - avgOpenPrice: 平均開倉價格
            - completeUsdt: 交易金額（USDT）
            - direction: 交易方向（long/short）
            - entrustUsdt: USDT訂單規模
            - fee: 費用
            - havShortfall: 表示用戶是否有清算風險
            - indexPrice: 觸發時的指數價格
            - instrument: 交易品種的基礎貨幣
            - leverage: 持倉槓桿率
            - liquidateBy: 持倉平倉原因（manual：手動平倉，stopProfit：止盈，stopLoss：止損等）
            - margin: 持倉使用的保證金金額
            - openId: 持倉ID
            - positionModel: 持倉保證金模式
            - status: 狀態（open/close）
            - totalPiece: 合約總數量
            - tradePiece: 已成交合約
            - tradeStartDate: 創建日期（時間戳）
            等等...
        """
        query = {}
        
        if instrument:
            query['instrument'] = instrument
        
        if position_model is not None:
            if position_model not in [0, 1]:
                raise InvalidParameterError("position_model必須是 0（逐倉保證金）或 1（全倉保證金）")
            query['positionModel'] = position_model
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions/history",
            query=query,
            auth=True
        )
    
    def get_position_margin_rate(self, position_id: Optional[int] = None) -> Dict[str, Any]:
        """
        獲取持倉保證金率
        
        此接口允許通過指定持倉ID查詢應用於持倉（已成交訂單）的保證金率。
        
        Args:
            position_id: 持倉ID（可選）
                注意：查詢逐倉保證金持倉的保證金率時，此參數是必需的。
                對於全倉保證金持倉，應省略此參數。
        
        Returns:
            持倉保證金率信息，包含：
            - data: 持倉保證金率值
        """
        query = {}
        
        if position_id is not None:
            query['positionId'] = position_id
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions/marginRate",
            query=query,
            auth=True
        )
    
    def get_max_order_size(
        self,
        leverage: int,
        instrument: str,
        position_model: int,
        order_price: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        獲取最大合約規模
        
        此接口允許根據指定的合約、槓桿率和持倉模式查詢最大可用合約規模（對於做多和做空持倉）。
        用戶可以選擇指定開倉價格。
        
        注意：此接口提供公共市場信息，與用戶帳戶無關。
        
        Args:
            leverage: 持倉槓桿率（必填）
            instrument: 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。
                注意：對於以數字開頭的交易品種（例如1000PEPE），大小寫格式都有效。
            position_model: 持倉保證金模式（必填）
                0：逐倉保證金
                1：全倉保證金
            order_price: 用戶指定的訂單價格（可選）
        
        Returns:
            最大合約規模信息，包含：
            - maxBuy: 最大可用合約規模（買入）
            - maxSell: 最大可用合約規模（賣出）
        """
        if position_model not in [0, 1]:
            raise InvalidParameterError("position_model必須是 0（逐倉保證金）或 1（全倉保證金）")
        
        query = {
            'leverage': leverage,
            'instrument': instrument,
            'positionModel': position_model
        }
        
        if order_price is not None:
            query['orderPrice'] = order_price
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/maxSize",
            query=query,
            auth=True
        )
    
    def get_all_positions(self) -> Dict[str, Any]:
        """
        獲取所有當前持倉
        
        此接口允許用戶查詢所有當前開倉持倉（已成交訂單）。
        
        注意：該接口與"市價平倉"接口在URL結構上較為相似，
        用戶應仔細區分以確保採用正確的請求方法，避免因混淆導致非預期操作或數據異常。
        
        Returns:
            所有當前持倉信息，包含與 get_positions 相同的欄位：
            - id: 持倉ID
            - base: 合約基礎貨幣
            - baseSize: 合約面值
            - createdDate: 持倉創建時間戳
            - currentPiece: 當前持倉張數
            - closedPiece: 已平倉合約數量
            - direction: 交易方向（long/short）
            - fee: 資金費
            - fundingSettle: 已結算資金費
            - indexPrice: 觸發時的指數價格
            - instrument: 交易品種的基礎貨幣
            - leverage: 持倉槓桿率
            - margin: 持倉使用的保證金
            - openPrice: 持倉開倉價格
            - positionMargin: 持倉保證金
            - positionModel: 倉位模式（0：逐倉，1：全倉）
            - quantity: 訂單數量
            - quantityUnit: 數量計量單位
            - status: 狀態（open/close）
            - totalPiece: 合約總張數
            - profitUnreal: 未實現盈虧
            等等...
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions/all",
            query={},
            auth=True
        )
    
    def get_leverage_info(
        self,
        position_id: Optional[int] = None,
        order_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        獲取槓桿信息
        
        此接口提供已成交（使用持倉ID檢索）和未成交（使用訂單ID檢索）訂單的槓桿詳情。
        請注意，槓桿信息一次只能獲取一個訂單（已成交或未成交）。
        
        Args:
            position_id: 持倉ID（可選）
                查詢已成交訂單的槓桿時需要。
            order_id: 訂單ID（可選） 
                查詢未成交訂單的槓桿時需要。
        
        Note:
            position_id 和 order_id 必須提供其中一個，但不能同時提供兩個。
        
        Returns:
            槓桿信息，包含：
            - data: 持倉槓桿率值
        
        Raises:
            InvalidParameterError: 當參數不正確時拋出異常
        """
        # 參數驗證
        if position_id is None and order_id is None:
            raise InvalidParameterError("必須提供 position_id 或 order_id 其中一個")
        
        if position_id is not None and order_id is not None:
            raise InvalidParameterError("position_id 和 order_id 不能同時提供，只能選擇其中一個")
        
        query = {}
        
        if position_id is not None:
            query['positionId'] = position_id
        
        if order_id is not None:
            query['orderId'] = order_id
        
        return self._submit_request(
            method="GET",
            path="/v1/perpum/positions/leverage",
            query=query,
            auth=True
        )
    
    # 便利方法
    def get_position_by_id(self, instrument: str, position_id: str) -> Dict[str, Any]:
        """
        根據持倉ID獲取特定持倉信息
        
        Args:
            instrument: 交易品種的基礎貨幣
            position_id: 持倉ID
            
        Returns:
            特定持倉信息
        """
        return self.get_positions(instrument=instrument, open_ids=position_id)
    
    def get_positions_by_instrument(self, instrument: str) -> Dict[str, Any]:
        """
        獲取指定合約的所有持倉信息
        
        Args:
            instrument: 交易品種的基礎貨幣
            
        Returns:
            指定合約的所有持倉信息
        """
        return self.get_positions(instrument=instrument)
    
    def get_cross_margin_positions_history(self) -> Dict[str, Any]:
        """
        獲取全倉保證金模式的歷史持倉信息
        
        Returns:
            全倉保證金歷史持倉信息
        """
        return self.get_positions_history(position_model=1)
    
    def get_isolated_margin_positions_history(self) -> Dict[str, Any]:
        """
        獲取逐倉保證金模式的歷史持倉信息
        
        Returns:
            逐倉保證金歷史持倉信息
        """
        return self.get_positions_history(position_model=0)
    
    def get_cross_margin_rate(self) -> Dict[str, Any]:
        """
        獲取全倉保證金率
        
        Returns:
            全倉保證金率
        """
        return self.get_position_margin_rate()
    
    def get_isolated_margin_rate(self, position_id: int) -> Dict[str, Any]:
        """
        獲取逐倉保證金率
        
        Args:
            position_id: 持倉ID（逐倉保證金必填）
            
        Returns:
            逐倉保證金率
        """
        return self.get_position_margin_rate(position_id=position_id)
    
    def get_position_leverage(self, position_id: int) -> Dict[str, Any]:
        """
        獲取已成交訂單（持倉）的槓桿信息
        
        Args:
            position_id: 持倉ID
            
        Returns:
            持倉槓桿信息
        """
        return self.get_leverage_info(position_id=position_id)
    
    def get_order_leverage(self, order_id: int) -> Dict[str, Any]:
        """
        獲取未成交訂單的槓桿信息
        
        Args:
            order_id: 訂單ID
            
        Returns:
            訂單槓桿信息
        """
        return self.get_leverage_info(order_id=order_id) 