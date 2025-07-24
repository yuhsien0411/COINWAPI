from coinwapi.future import FutureClient
client = FutureClient(api_key="", secret_key="")
#需要api_key和secret_key

def place_order(instrument, side, order_type, quantity, price=None, time_in_force='GTC', reduce_only=False, new_client_order_id=None, stop_price=None, close_position=False, activation_price=None, callback_rate=None):
    """
    下期貨訂單
    Args:
        instrument: 交易品種基礎貨幣（例如，BTC或btc）。此參數不區分大小寫
        side: 交易方向：做多(long)，做空(short)
        order_type: 訂單類型：
            execute：市價單
            plan：用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單、
                  帶SL/TP的觸發限價單、觸發市價單、帶SL/TP的觸發市價單
            planTrigger：計劃觸發訂單
        quantity: 基於quantity_unit指定訂單數量：
            當quantity_unit=0時，數量以計價貨幣計量（例如，BTC-USDT中的USDT）
            當quantity_unit=1時，數量以合約張數計量
            當quantity_unit=2時，數量以基礎貨幣計量（例如，BTC-USDT中的BTC）
        price: 指定訂單價格（計劃訂單必填）
        time_in_force: 訂單時效性，預設為'GTC'
        reduce_only: 是否僅減倉，預設為False
        new_client_order_id: 用戶分配的自定義訂單ID，用於唯一區分不同持倉
            最大長度：50個字符；僅允許拉丁字母、數字、連字符(-)和下劃線(_)
        stop_price: 止損價格（止損訂單必填）
        close_position: 是否平倉
        activation_price: 計劃訂單的觸發價格
        callback_rate: 指定觸發價格滿足時的訂單類型：0：限價單，1：市價單
    Returns:
        dict: API回應結果
    """
    re = client.place_order(instrument=instrument, side=side, order_type=order_type, quantity=quantity, price=price, time_in_force=time_in_force, reduce_only=reduce_only, new_client_order_id=new_client_order_id, stop_price=stop_price, close_position=close_position, activation_price=activation_price, callback_rate=callback_rate)
    print(re)

def place_batch_orders(orders):
    """批量下單        
    Args:
        orders: 訂單列表，每個訂單包含以下字段：
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
    Returns:
        dict: API回應結果
    """
    re = client.place_batch_orders(orders=orders)
    print(re)

def cancel_order(order_id):
    """取消合約訂單"""
    re = client.cancel_order(order_id=order_id)
    print(re)

def cancel_batch_orders(order_ids, pos_type=None):
    """批量取消訂單"""
    re = client.cancel_batch_orders(order_ids=order_ids, pos_type=pos_type)
    print(re)

def modify_order(order_id, **kwargs):
    """
    修改訂單
    Args:
        order_id: 訂單ID
        **kwargs: 修改參數，包括：
            instrument: 交易品種基礎貨幣（例如，BTC或btc）
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
    Returns:
        dict: API回應結果
    """
    re = client.modify_order(order_id=order_id, **kwargs)
    print(re)

def close_position(position_id, **kwargs):
    """平倉
        注意事項：
        - positionType: 平倉訂單類型
            plan: 以指定價格平倉  
            execute: 以市價平倉（默認）
        - closeNum: 要平倉的合約數量（與closeRate互斥，必須提供其中之一）
        - closeRate: 平倉比例，範圍0-1，例如0.5表示平倉50%（與closeNum互斥）
        - orderPrice: 指定平倉價格（如果指定，positionType必須設為plan）
    Args:
        position_id: 持倉ID
        **kwargs: 其他參數
    
    Returns:
        dict: API回應結果
    """
    re = client.close_position(position_id=position_id, **kwargs)
    print(re)
    
def close_batch_positions(third_order_ids):
    """批量平倉
    此接口允許用戶通過指定thirdOrderId（用戶下單時定義的自定義ID）批量以市價平倉多個持倉。
    
    注意事項：
        - 只能使用市價平倉
        - 需要使用下單時的thirdOrderId
        - 會平倉所有指定的持倉
    
    Args:
        third_order_ids: 用戶分配的自定義訂單ID列表
    
    Returns:
        dict: API回應結果
    """
    re = client.close_batch_positions(third_order_ids=third_order_ids)
    print(re)

def close_all_positions(instrument):
    """市價平倉所有持倉
    這個接口將以市價單的方式平倉指定合約的所有持倉。
    
    注意事項：
        - 會平倉該合約的所有持倉
        - 使用市價單執行
        - 不區分大小寫
        - 對於以數字開頭的合約（例如1000PEPE），大寫和小寫格式都有效
    Args:
        instrument: 合約的基礎貨幣（例如，BTC或btc）
    
    Returns:
        dict: API回應結果
    """
    re = client.close_all_positions(instrument=instrument)
    print(re)


def reverse_position(position_id):
    """反向持倉
    此接口允許用戶反轉指定的持倉，即將多頭持倉轉換為空頭持倉，或將空頭持倉轉換為多頭持倉。
    
    注意事項：
        - 會先平掉原有持倉，然後開立相反方向的新持倉
        - 新持倉的數量與原持倉相同
        - 使用市價執行
        - 需要有足夠的保證金來開立新持倉
        - 原持倉的盈虧會被結算
    Args:
        position_id: 持倉ID
    
    Returns:
        dict: API回應結果
    """
    re = client.reverse_position(position_id=position_id)
    print(re)

def adjust_margin(position_id, add_margin=None, reduce_margin=None, type_="all"):
    """調整保證金
    此接口允許用戶調整現有持倉的保證金金額。可以增加或減少保證金，
    但不能同時進行兩種操作。
    
    注意事項：
        - add_margin 和 reduce_margin 互斥，只能提供其中一個
        - 保證金金額必須大於0
        - 減少保證金時，要確保剩餘保證金足夠維持持倉
        - type_ 參數決定使用哪種資金來源進行調整
    Args:
        position_id: 持倉ID
        add_margin: 要增加的保證金金額（必須大於0）
        reduce_margin: 要減少的保證金金額（必須大於0）
        type_: 指定余額查詢範圍。可能的值：
            all：包括余額和萬能金
            almightyGold：僅萬能金
            balance：僅余額
    """
    re = client.adjust_margin(position_id=position_id, add_margin=add_margin, reduce_margin=reduce_margin, type_=type_)
    print(re)

def set_stop_loss_take_profit(order_or_position_id, **kwargs):
    """設置止損/止盈
    此接口允許用戶為已成交和未成交訂單設置止盈(TP)和止損(SL)。
    
    注意事項：
        - 要為已成交訂單設置SL/TP，請提供持倉ID
        - 要為未成交訂單設置SL/TP，請提供訂單ID
        - 設置止損/止盈僅通過Restful API可用
        - 可以設置止損/止盈價格或止損/止盈率
        - 止損限價和止盈限價為可選參數
        - 頻率限制：每個IP和用戶ID每2秒最多請求10次
    
    Args:
        order_or_position_id: 訂單ID（對於未成交訂單）或持倉ID（對於已成交訂單）
        **kwargs: 其他參數，包括：
            - instrument: 交易品種基礎貨幣（例如，BTC或btc），此參數不區分大小寫
            - stop_loss_order_price: 止損限價
            - stop_profit_order_price: 止盈限價
            - stop_loss_price: 止損價格
            - stop_profit_price: 止盈價格
            - stop_loss_rate: 止損率
            - stop_profit_rate: 止盈率
    
    Returns:
        dict: API回應結果
    """
    re = client.set_stop_loss_take_profit(order_or_position_id=order_or_position_id, **kwargs)
    print(re)

def set_trailing_stop(position_id, callback_rate, quantity, **kwargs):
    """設置追蹤止損/止盈
    此接口允許用戶設置追蹤止損/止盈功能，當價格朝有利方向移動時，
    止損/止盈價格會自動跟隨調整。
    
    注意事項：
        - position_id (openId): 持倉ID，必填
        - callback_rate (callbackRate): 回調率，必填，有效範圍從0到1（例如：0.5表示50%的回調率）
        - quantity: 合約/USDT數量，必填
        - trigger_price (triggerPrice): 激活價格，可選
        - quantity_unit (quantityUnit): 指定數量單位，可選
            0: 以USDT計價
            1: 以合約計價（預設值）
        - 追蹤止損會隨著價格有利變動而調整止損價位
        - 當價格反向回調到設定比例時會自動觸發平倉
        - 適合用於保護已有利潤
    
    Args:
        position_id: 持倉ID
        callback_rate: 回調率（百分比）
        quantity: 止損/止盈數量
        **kwargs: 其他參數
    
    Returns:
        dict: API回應結果
    """
    re = client.set_trailing_stop(position_id=position_id, callback_rate=callback_rate, quantity=quantity, **kwargs)
    print(re)


def batch_set_stop_loss_take_profit(order_position_or_plan_id, stop_from, **kwargs):
    """批量設置止損/止盈
    此接口允許用戶批量設置多個訂單或持倉的止損/止盈。
    
    Args:
        order_position_or_plan_id: 訂單ID/持倉ID/計劃ID（必填）
        stop_from: 止盈/止損觸發後的訂單類型（必填）
            1: 限價單（在order_position_or_plan_id參數中提供訂單ID）
            2: 市價單（在order_position_or_plan_id參數中提供持倉ID）
            3: 條件單（在order_position_or_plan_id參數中提供計劃ID）
        **kwargs: 其他參數，包括：
            - instrument: 交易品種基礎貨幣（例如，BTC或btc），此參數不區分大小寫
            - stop_loss_order_price: 止損限價
            - stop_profit_order_price: 止盈限價
            - stop_loss_price: 止損價格
            - stop_profit_price: 止盈價格
            - stop_loss_rate: 止損率
            - stop_profit_rate: 止盈率
            - price_type: 止盈和止損觸發價格類型
                1: 指數價格
                2: 最新價格
                3: 標記價格
            - stop_type: 止損/止盈類型
                1: 批量止盈/止損（僅適用於未成交訂單）
                2: 整個持倉止盈/止損（僅適用於已成交訂單）
            - close_piece: 止盈和止損合約數量（批量止盈/止損必填）
    
    Returns:
        dict: API回應結果
    """
    re = client.batch_set_stop_loss_take_profit(order_position_or_plan_id=order_position_or_plan_id, stop_from=stop_from, **kwargs)
    print(re)

def batch_modify_stop_loss_take_profit(order_position_or_plan_id, stop_from, **kwargs):
    """批量修改止損/止盈
    此接口允許用戶批量修改現有的止損/止盈設置。
    
    Args:
        order_position_or_plan_id: 訂單ID/持倉ID/計劃ID（必填）
        stop_from: 止盈/止損觸發後的訂單類型（必填）
            1: 限價單
            2: 市價單 
            3: 條件單
        **kwargs: 其他參數，包括：
            - instrument: 交易品種基礎貨幣（例如，BTC或btc），此參數不區分大小寫
            - stop_profit_order_price: 止盈限價
            - stop_loss_price: 止損價格
            - stop_profit_price: 止盈價格
            - stop_loss_rate: 止損率
            - stop_profit_rate: 止盈率
            - price_type: 止盈和止損觸發價格類型
                1: 指數價格
                2: 最新價格
                3: 標記價格
            - stop_type: 止損/止盈類型
                1: 批量止盈/止損
                2: 整個持倉止盈/止損
            - close_piece: 止盈/止損合約數量（批量止盈/止損必填）
    
    Returns:
        dict: API回應結果
    """
    re = client.batch_modify_stop_loss_take_profit(order_position_or_plan_id=order_position_or_plan_id, stop_from=stop_from, **kwargs)
    print(re)


def get_open_orders(instrument, position_type, page=None, page_size=None):
    """獲取當前訂單
    此接口用於查詢當前所有未成交的訂單信息。
    
    Args:
        instrument: 交易品種的基礎貨幣（例如，BTC或btc），此參數不區分大小寫。
                   注意：對於以數字開頭的交易品種（例如1000PEPE），大寫和小寫格式都有效。
        position_type: 訂單類型：
            plan：計劃訂單
            execute：市價單
            planTrigger：計劃觸發訂單
            moveStopProfitLoss：追蹤止損/止盈
        page: 當前頁碼（可選）
        page_size: 每頁記錄數（可選）
    
    Returns:
        dict: API回應結果，包含當前訂單列表
    """
    re = client.get_open_orders(instrument=instrument, position_type=position_type, page=page, page_size=page_size)
    print(re)


def get_pending_order_count():
    """獲取待處理訂單數量"""
    re = client.get_pending_order_count()
    print(re)

def get_stop_loss_take_profit_info(stop_from, **kwargs):
    """獲取止損/止盈信息
    此接口用於查詢特定的止損/止盈設置信息。
    
    Args:
        stop_from: 止損來源類型
        **kwargs: 其他查詢參數
    
    Returns:
        dict: API回應結果，包含止損/止盈詳細信息
    """
    re = client.get_stop_loss_take_profit_info(stop_from=stop_from, **kwargs)
    print(re)

def get_trailing_stop_info():
    """獲取追蹤止損/止盈信息
    此接口用於查詢當前所有追蹤止損/止盈的設置信息。
    
    Returns:
        dict: API回應結果，包含所有追蹤止損/止盈信息
    """
    re = client.get_trailing_stop_info()
    print(re)

def get_order_history(instrument=None, page=None, page_size=None, origin_type=None):
    """獲取歷史訂單（7天）
    此接口用於查詢過去七天內的歷史訂單信息。
    
    Args:
        instrument: 交易品種的基礎貨幣（例如，BTC或btc），此參數不區分大小寫。
                   注意：對於以數字開頭的交易品種（例如1000PEPE），大寫和小寫格式都有效。
        page: 當前頁碼（可選）
        page_size: 每頁記錄數（可選）。注意：如果未指定，接口將返回過去七天內最近10個訂單的信息。
        origin_type: 初始訂單類型（可選）：
            execute：市價單
            plan：用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單、
                  帶SL/TP的觸發限價單、觸發市價單、帶SL/TP的觸發市價單
            planTrigger：計劃觸發訂單
    
    Returns:
        dict: API回應結果，包含歷史訂單列表
    """
    re = client.get_order_history(instrument=instrument, page=page, page_size=page_size, origin_type=origin_type)
    print(re)

def get_order_archive(instrument=None, page=None, page_size=None, origin_type=None):
    """獲取歷史訂單（3個月）
    此接口用於查詢過去三個月內的歷史訂單信息。
    
    Args:
        instrument: 交易品種的基礎貨幣（例如，BTC或btc），此參數不區分大小寫。
                   注意：對於以數字開頭的交易品種（例如1000PEPE），大寫和小寫格式都有效。
        page: 當前頁碼（可選）
        page_size: 每頁記錄數（可選）。注意：如果未指定，接口將返回過去三個月內最近10個訂單的信息。
        origin_type: 初始訂單類型（可選）：
            execute：市價單
            plan：用於不同計劃訂單，包括限價單、觸發限價單、帶SL/TP的限價單、
                  帶SL/TP的觸發限價單、觸發市價單、帶SL/TP的觸發市價單
            planTrigger：計劃觸發訂單
    
    Returns:
        dict: API回應結果，包含歷史訂單列表
    """
    re = client.get_order_archive(instrument=instrument, page=page, page_size=page_size, origin_type=origin_type)
    print(re)
def get_order(position_type, **kwargs):
    """獲取訂單信息
    此接口用於查詢指定類型的訂單詳細信息。
    
    Args:
        position_type: 訂單類型（必填）：
            execute：市價單
            plan：計劃單
            moveStop：追蹤止損和止盈
            stopProfitLoss：止損和止盈
        **kwargs: 其他參數，包括：
            source_ids: 以逗號(,)分隔的訂單ID列表（例如："orderId1,orderId2,orderId3"）
                       注意：訂單ID數量不能超過20個
            instrument: 交易品種的基礎貨幣（例如，BTC或btc），此參數不區分大小寫。
                       注意：對於以數字開頭的交易品種（例如1000PEPE），大寫和小寫格式都有效
    
    Returns:
        dict: API回應結果，包含訂單詳細信息
    """
    re = client.get_order(position_type=position_type, **kwargs)
    print(re)