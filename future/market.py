"""
CoinW 期貨市場數據模組

專門處理期貨/合約市場數據 API
端點格式: /v1/perpum/... 和 /v1/perpumPublic/...
"""

from typing import Dict, Any, Optional
from .http_manager import _ContractHTTPManager


class FutureMarket(_ContractHTTPManager):
    """期貨市場數據接口"""
    
    def get_instruments(self, name: Optional[str] = None) -> Dict[str, Any]:
        """
        獲取合約產品信息
        
        Args:
            name: 交易品種的基礎貨幣，如 "BTC"。不區分大小寫。
                 對於以數字開頭的交易品種(如"1000PEPE")，大小寫格式均有效。
                 如果不指定，則返回所有交易品種數據。
             
        Returns:
            Dict[str, Any]: 包含以下字段:
                - base (str): 交易品種的基礎貨幣，如BTC、ETH
                - defaultLeverage (int): 默認槓桿率
                - defaultStopLossRate (float): 默認止損率
                - defaultStopProfitRate (float): 默認止盈率
                - indexId (int): 索引ID
                - leverage (list): 可用槓桿選項
                - makerFee (float): maker費用
                - maxLeverage (int): 允許的最大槓桿率
                - minLeverage (int): 允許的最小槓桿率
                - maxPosition (float): 允許的最大持倉量
                - minSize (float): 最小訂單大小
                - name (str): 基礎貨幣名稱
                - oneLotMargin (float): 每手所需保證金
                - oneMaxPosition (float): 每手最大持倉量
                - pricePrecision (int): 價格精度小數位數
                - quote (str): 合約報價貨幣
                - status (str): 合約當前狀態
                - takerFee (float): taker費用
                等其他字段
        """
        query = {}
        if name:
            query['name'] = name
             
        return self._submit_request(
            method="GET",
            path="/v1/perpum/instruments",
            query=query,
            auth=False
        )
    
    def get_ticker(self, instrument: str) -> Dict[str, Any]:
        """
        獲取合約最新交易摘要
        
        Args:
            instrument: 交易品種的基礎貨幣，如 "BTC"。不區分大小寫。
                       對於以數字開頭的交易品種(如"1000PEPE")，大小寫格式均有效。
            
        Returns:
            Dict[str, Any]: 包含以下字段:
                - contract_id (int): 合約類型 1=U本位永續合約
                - name (str): 合約名稱，如 BTCUSDT
                - base_coin (str): 合約基礎貨幣，如 btc
                - quote_coin (str): 合約報價貨幣，如 usdt
                - price_coin (str): 合約基礎貨幣，如 btc
                - max_leverage (int): 允許的最大槓桿率
                - contract_size (float): 可交易的最小合約大小
                - last_price (float): 合約最新成交價格
                - high (float): 最新交易摘要中的最高價格
                - low (float): 最新交易摘要中的最低價格
                - rise_fall_rate (float): 價格變化
                - total_volume (float): 合約總交易量
                - fair_price (float): 合約指數價格
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpumPublic/ticker",
            query={
                'instrument': instrument
            },
            auth=False
        )
    
    def get_tickers(self) -> Dict[str, Any]:
        """
        獲取所有合約的最新交易摘要
        
        Returns:
            Dict[str, Any]: 包含所有合約的ticker數據列表
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpumPublic/ticker",
            query={},
            auth=False
        )

    
    def get_klines(
        self,
        currency_code: str,
        granularity: str = "2",
        limit: Optional[int] = 100
    ) -> Dict[str, Any]:
        """
        獲取K線數據
        
        Args:
            currency_code: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
            granularity: K線時間間隔，可選值:
                "0": 1分鐘
                "1": 5分鐘  
                "2": 15分鐘
                "3": 1小時
                "4": 4小時
                "5": 1天
                "6": 1週
                "7": 3分鐘
                "8": 30分鐘
                "9": 1個月
            limit: 返回記錄數量，範圍1-1500，預設100
             
        Returns:
            K線數據，包含:
            - 時間戳
            - 最高價格
            - 開盤價格 
            - 最低價格
            - 收盤價格
            - 交易量
        """
        query = {
            'currencyCode': currency_code,
            'granularity': granularity
        }
        
        if limit:
            # 檢查limit參數是否在合法範圍內(1-1500)
            # 如果超出範圍則使用預設值100
            if not 1 <= limit <= 1500:
                limit = 100
            query['limit'] = limit
            
        return self._submit_request(
            method="GET",
            path="/v1/perpumPublic/klines",
            query=query,
            auth=False
        ) 
    
    def get_last_funding_rate(self, instrument: str) -> Dict[str, Any]:
        """
        獲取最近一次結算資金費率
        
        Args:
            instrument: 交易品種的基礎貨幣，如 "BTC"，區分大小寫
            
        Returns:
            Dict[str, Any]: 包含以下字段:
                - code: 狀態碼
                - data: 包含資金費率的字典
                - msg: 錯誤訊息(如有)
                
        Note:
            - 此接口返回的是最近一次結算時點的資金費率
            - 調用頻率限制為每個IP和用戶ID每秒最多8次
            - 對於不存在的合約將返回錯誤碼9001
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/fundingRate",
            query={
                'instrument': instrument
            },
            auth=False
        )
    def get_orderbook(self, base: str) -> Dict[str, Any]:
        """
        獲取合約訂單簿
        
        Args:
            base: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
            
        Returns:
            Dict[str, Any]: 包含以下字段:
                - code (int): 狀態碼
                - data (dict): 包含以下字段:
                    - asks (list): 賣方深度，包含20個賣單，每項包含:
                        - m (float): 基礎貨幣數量
                        - p (float): 基礎貨幣價格
                    - bids (list): 買方深度，包含20個買單，每項包含:
                        - m (float): 基礎貨幣數量
                        - p (float): 基礎貨幣價格
                    - n (str): 合約的基礎貨幣，例如BTC
                - msg (str): 錯誤訊息(如有)
                
        Note:
            - 調用頻率限制為每個IP和用戶ID每2秒最多10次
            - 默認返回20個級別的買賣單深度
            - 不提供時間戳信息
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpumPublic/depth",
            query={
                'base': base
            },
            auth=False
        )


    def get_trades(self, base: str) -> Dict[str, Any]:
        """
        獲取合約交易數據
        
        Args:
            base: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
            
        Returns:
            Dict[str, Any]: 包含以下字段:
                - code (int): 狀態碼
                - data (list): 交易數據列表，每項包含:
                    - createdDate (int): 交易時間戳
                    - piece (str): 合約數量
                    - direction (str): 交易方向：做多(long)，做空(short)
                    - price (str): 已執行的交易價格
                    - quantity (str): 交易量（幣數量）
                    - id (int): 交易ID
                - msg (str): 錯誤訊息(如有)
                
        Note:
            - 默認返回最近20筆交易數據
            - 此接口不允許指定返回的交易數量
            - 此接口不支持指定時間間隔查詢
            - 調用頻率限制為每個IP和用戶ID每2秒最多10次
            - 這是一個公共接口，不需要認證
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpumPublic/trades",
            query={
                'base': base
            },
            auth=False
        )
    
    def get_ladders(self) -> Dict[str, Any]:
        """
        獲取所有合約的保證金要求
        
        Returns:
            Dict[str, Any]: 包含以下字段:
                - code (int): 狀態碼
                - data (dict): 保證金配置數據，包含:
                    - ladderConfig (list): 保證金級別配置列表，每項包含:
                        - name (str): 交易品種名稱，如 "BTC"
                        - ladderList (list): 該品種的級別列表，每項包含:
                            - id (str): 保證金級別的唯一ID
                            - instrument (str): 交易品種的基礎貨幣
                            - ladder (int): 級別，如 1、2、3等
                            - lastLadder (bool): 是否為最終級別
                            - marginKeepRate (float): 維持保證金率
                            - maxLeverage (int): 允許的最大槓桿率
                            - marginStartRate (float): 開倉所需的初始保證金率
                            - maxPiece (int): 最大合約大小
                - msg (str): 錯誤訊息(如有)
                
        Note:
            - 此接口提供所有交易對的分層保證金要求
            - 包括初始保證金、維持保證金和最大槓桿率
            - 調用頻率限制為每個IP和用戶ID每2秒最多10次
            - 這是一個私有接口，需要認證
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/ladders",
            auth=True
        )
    

    def get_traders_history(self, instrument: str, page: int = 1, pageSize: int = 100) -> Dict[str, Any]:
        """
        獲取歷史公開交易
        
        Args:
            instrument (str): 交易品種的基礎貨幣（例如 BTC 或 btc）
                - 此參數不區分大小寫
                - 對於以數字開頭的交易品種（例如 1000PEPE），大寫和小寫格式均有效
            page (int, optional): 當前頁，默認為 1
            pageSize (int, optional): 每頁數量，默認為 100
                - 默認返回 100 筆交易
                - 返回的最大交易數最多為 500
        
        Returns:
            Dict[str, Any]: 包含以下字段:
                - code (int): 狀態碼
                - data (dict): 交易數據，包含:
                    - nextId (int): 下一頁ID
                    - prevId (int): 上一頁ID
                    - rows (list): 交易記錄列表，每項包含:
                        - closedPiece (int): 已平倉合約數量
                        - createdDate (int): 交易時間（時間戳）
                        - dealPrice (float): 以報價貨幣計的交易價格（例如 USDT）
                        - direction (str): 交易方向（long、short）
                        - id (int): 成交ID
                    - total (int): 總記錄數
                - msg (str): 錯誤訊息(如有)
                
        Note:
            - 歷史公開交易數據只能通過 Restful API 獲取
            - 此接口提供公共市場信息，但仍需要認證
            - 調用頻率限制為每個IP和用戶ID每秒最多5次
            - 這是一個私有接口，需要認證
        """
        return self._submit_request(
            method="GET",
            path="/v1/perpum/orders/trades",
            query={
                'instrument': instrument,
                'page': page,
                'pageSize': pageSize
            },
            auth=True
        )
