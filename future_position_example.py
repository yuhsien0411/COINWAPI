from coinwapi.future import FutureClient
client = FutureClient(api_key="", secret_key="")

def get_positions(instrument, open_ids=None):
    """獲取當前持倉信息"""
    re = client.get_positions(instrument=instrument, open_ids=open_ids)
    print(re)

def get_positions_history(instrument=None, position_model=None):
    """獲取歷史持倉信息"""
    re = client.get_positions_history(instrument=instrument, position_model=position_model)
    print(re)

def get_position_margin_rate(position_id=None):
    """獲取持倉保證金率"""
    re = client.get_position_margin_rate(position_id=position_id)
    print(re)

def get_max_order_size(leverage, instrument, position_model, order_price=None):
    """獲取最大合約規模"""
    re = client.get_max_order_size(leverage=leverage, instrument=instrument, position_model=position_model, order_price=order_price)
    print(re)

def get_all_positions():
    """獲取所有當前持倉"""
    re = client.get_all_positions()
    print(re)

def get_leverage_info(position_id=None, order_id=None):
    """獲取槓桿信息"""
    re = client.get_leverage_info(position_id=position_id, order_id=order_id)
    print(re)











