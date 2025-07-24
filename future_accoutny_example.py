from coinwapi.future import FutureClient
client = FutureClient(api_key="", secret_key="")

def get_max_transferable_balance():
    """獲取最大可轉帳餘額"""
    re = client.get_max_transferable_balance()
    print(re)

def get_trade_details_3_days(instrument, page=None, page_size=None, origin_type=None, position_model=None):
    """獲取交易詳情（3天）
    
    參數說明：
    - instrument (必填): 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫
    - page (可選): 當前頁碼
    - page_size (可選): 每頁響應數量  
    - origin_type (可選): 初始訂單類型
      * execute: 市價單
      * plan: 用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單、帶SL/TP的觸發限價單、觸發市價單、帶SL/TP的觸發市價單
      * planTrigger: 計劃觸發訂單
    - position_model (可選): 持倉模式，0：逐倉，1：全倉
    """
    re = client.get_trade_details_3_days(instrument=instrument, page=page, page_size=page_size, origin_type=origin_type, position_model=position_model)
    print(re)

def get_trade_details_3_months(instrument, page=None, page_size=None, origin_type=None, position_model=None):
    """獲取交易詳情（3個月）
    
    參數說明：
    - instrument (必填): 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫。注意：對於以數字開頭的交易品種（例如1000PEPE），大寫和小寫格式都有效
    - page (可選): 當前頁碼
    - page_size (可選): 每頁響應數量  
    - origin_type (可選): 初始訂單類型
      * execute: 市價單
      * plan: 用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單、帶SL/TP的觸發限價單、觸發市價單、帶SL/TP的觸發市價單
      * planTrigger: 計劃觸發訂單
    - position_model (可選): 持倉模式，0：逐倉，1：全倉
    """
    re = client.get_trade_details_3_months(instrument=instrument, page=page, page_size=page_size, origin_type=origin_type, position_model=position_model)
    print(re)

def get_user_assets():
    """獲取合約帳戶資產"""
    re = client.get_user_assets()
    print(re)

def get_account_fees():
    """獲取合約帳戶費用"""
    re = client.get_account_fees()
    print(re)

def get_almighty_gold_info(gold_type, start_time=None, end_time=None):
    """獲取萬能金餘額
    
    參數說明：
    - gold_type (必填): 萬能金狀態
      * 0：待生效
      * 1：未使用
      * 2：已使用
      * 3：已過期
      * 4：發放失敗
    - start_time (可選): 有效期開始時間（時間戳）
    - end_time (可選): 有效期截止時間（時間戳）
    """
    re = client.get_almighty_gold_info(gold_type=gold_type, start_time=start_time, end_time=end_time)
    print(re)

def convert_units(convert_type, face_value, deal_piece=None, base_size=None):
    """單位轉換
    
    參數說明：
    - convert_type (必填): 轉換類型
      * 1：將合約單位（張數）轉換為幣
      * 2：將幣轉換為合約單位（張數）
    - face_value (必填): 每手最小價值
    - deal_piece (可選): 合約數量（當convert_type=1時必需）
    - base_size (可選): 面值*份數（幣的數量）（當convert_type=2時必需）
    
    注意：
    - 當convert_type=1時，deal_piece參數是必需的
    - 當convert_type=2時，base_size參數是必需的
    """
    re = client.convert_units(convert_type=convert_type, face_value=face_value, deal_piece=deal_piece, base_size=base_size)
    print(re)

def get_margin_mode():
    """獲取保證金模式"""
    re = client.get_margin_mode()
    print(re)

def set_margin_mode(position_model, layout):
    """設置保證金模式
    
    參數說明：
    - position_model (必填): 持倉保證金模式
      * 0：逐倉保證金
      * 1：全倉保證金
    - layout (必填): 持倉布局
      * "0"：合併持倉（相同方向的持倉將被合併）
      * "1"：分開持倉（相同方向的持倉將保持分離）
    
    注意：
    - 要將持倉保證金模式從逐倉更改為全倉或反之，用戶必須確保沒有未成交訂單
    - 要將持倉布局從合併持倉更改為分開持倉或反之，用戶必須確保沒有未成交訂單
    """
    re = client.set_margin_mode(position_model=position_model, layout=layout)
    print(re)

def toggle_almighty_gold(status):
    """啟用/禁用萬能金
    
    參數說明：
    - status (必填): 萬能金狀態
      * "1"：開啟
      * "0"：關閉
    """
    re = client.toggle_almighty_gold(status=status)
    print(re)

def get_user_max_order_size(instrument):
    """獲取用戶最大合約規模
    
    參數說明：
    - instrument (必填): 交易品種的基礎貨幣（例如，BTC或btc）。此參數不區分大小寫
    """
    re = client.get_user_max_order_size(instrument=instrument)
    print(re)

