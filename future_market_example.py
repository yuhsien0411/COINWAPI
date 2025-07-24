from coinwapi.future import FutureClient
client = FutureClient(api_key="", secret_key="")

def get_instruments():
    """獲取合約產品信息
        Args:
            name: 合約名稱(可選)
        Returns:
            Dict[str, Any]: 包含合約產品信息字典
    """
    re = client.get_instruments()
    print(re)


def get_ticker(instrument):
    """獲取合約ticker數據
        Args:
            instrument: 合約名稱
        Returns:
            Dict[str, Any]: 包含ticker數據的字典
    """
    re = client.get_ticker(instrument="BTC")
    print(re)

def get_tickers():
    """獲取所有合約ticker數據"""
    re = client.get_tickers()
    print(re)

def get_klines(symbol, interval, start_time=None, end_time=None, limit=500):
    """獲取K線數據
        Args:
            symbol: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
            interval: K線時間間隔，可選值:
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
            start_time: 起始時間戳（毫秒）(可選)
            end_time: 結束時間戳（毫秒）(可選)
            limit: 返回記錄數量，範圍1-1500，預設100(可選)
        Returns:
            Dict[str, Any]: K線數據，包含時間戳、最高價格、開盤價格、最低價格、收盤價格、交易量
    """
    re = client.get_klines(symbol=symbol, interval=interval, start_time=start_time, end_time=end_time, limit=limit)
    print(re)

def get_last_funding_rate(symbol):
    """獲取資金費率
        Args:
            symbol: 交易品種的基礎貨幣，如 "BTC"，區分大小寫
        Returns:
            Dict[str, Any]: 包含資金費率數據的字典
    """
    re = client.get_last_funding_rate(symbol=symbol)
    print(re)


def get_orderbook(base):
    """獲取深度數據
        Args:
            base: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
        Returns:
            Dict[str, Any]: 包含深度數據的字典
    """
    re = client.get_orderbook(base=base)
    print(re)

def get_trades(base):
    """獲取最新成交
        Args:
            base: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫
        Returns:
            Dict[str, Any]: 包含最新成交數據的字典
    """
    re = client.get_trades(base=base)
    print(re)


##########需要api驗證##########

def get_ladders():
    """獲取保證金要求"""
    re = client.get_ladders()
    print(re)

def get_traders_history(instrument, page=1, pageSize=100):
    """獲取交易者歷史
    
    Args:
        instrument: 交易品種的基礎貨幣，如 "BTC"，不區分大小寫。
                   對於以數字開頭的交易品種(如"1000PEPE")，大小寫格式均有效。
        page: 當前頁數，預設為1
        pageSize: 每頁數量，預設為100，最大為500
        
    Returns:
        Dict[str, Any]: 包含交易者歷史數據的字典
    """
    re = client.get_traders_history(instrument=instrument, page=page, pageSize=pageSize)
    print(re)






