"""
CoinW 期貨 WebSocket API 使用示例
基於官方 ws.md 文檔的完整實現

本文件包含所有 WebSocket 接口的使用示例：
- 公共接口：24小時交易摘要、訂單簿、交易數據、K線、指數價格、標記價格、資金費率
- 私有接口：當前訂單、持倉、持倉變更、資產、萬能金、保證金模式
"""

import json
import time
from coinwapi.future.ws_client import CoinWFutureWebSocketClient, FuturesWebsocketPublic, FuturesWebsocketPrivate


def example_ticker_subscription():
    """
    示例：訂閱24小時交易摘要
    對應文檔: ## 订阅24小时交易摘要
    """
    print("\n=== 訂閱24小時交易摘要示例 ===")
    
    def message_handler(data):
        print(f"📊 收到24小時交易摘要: {json.dumps(data, indent=2, ensure_ascii=False)}")
    
    # 方法1：使用文檔中的函數方式
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "ticker_swap"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 使用函數方式連接...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=message_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_depth_subscription():
    """
    示例：訂閱訂單簿
    對應文檔: ## 订阅订单簿
    """
    print("\n=== 訂閱訂單簿示例 ===")
    
    def depth_handler(data):
        if "data" in data and "asks" in data["data"]:
            asks = data["data"]["asks"][:3]  # 只顯示前3個賣單
            bids = data["data"]["bids"][:3]  # 只顯示前3個買單
            print(f"📖 訂單簿更新 - 賣盤前3: {asks}")
            print(f"📖 訂單簿更新 - 買盤前3: {bids}")
        else:
            print(f"📖 訂單簿: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "depth"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC訂單簿...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=depth_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_fills_subscription():
    """
    示例：訂閱交易數據
    對應文檔: ## 订阅交易数据
    """
    print("\n=== 訂閱交易數據示例 ===")
    
    def fills_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for trade in data["data"]:
                print(f"💹 新交易: 價格={trade.get('price')}, 數量={trade.get('quantity')}, "
                      f"方向={trade.get('direction')}, 時間={trade.get('createdDate')}")
        else:
            print(f"💹 交易數據: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "fills"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC交易數據...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=fills_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_candles_utc8_subscription():
    """
    示例：訂閱K線（UTC+8）數據
    對應文檔: ## 订阅K线（UTC+8）数据
    """
    print("\n=== 訂閱K線（UTC+8）數據示例 ===")
    
    def candles_handler(data):
        if "data" in data and isinstance(data["data"], list) and len(data["data"]) >= 6:
            candle = data["data"]
            print(f"📈 K線更新 (UTC+8): 時間={candle[0]}, 開={candle[1]}, "
                  f"高={candle[2]}, 低={candle[3]}, 收={candle[4]}, 量={candle[5]}")
        else:
            print(f"📈 K線數據: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "btc",
            "type": "candles_swap",
            "interval": "1"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC 1分鐘K線（UTC+8）...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=candles_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_candles_utc0_subscription():
    """
    示例：訂閱K線（UTC+0）數據
    對應文檔: # 订阅K线（UTC+0）数据
    """
    print("\n=== 訂閱K線（UTC+0）數據示例 ===")
    
    def candles_utc_handler(data):
        if "data" in data and isinstance(data["data"], list) and len(data["data"]) >= 6:
            candle = data["data"]
            print(f"📈 K線更新 (UTC+0): 時間={candle[0]}, 開={candle[1]}, "
                  f"高={candle[2]}, 低={candle[3]}, 收={candle[4]}, 量={candle[5]}")
        else:
            print(f"📈 K線數據: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "interval": "1",
            "pairCode": "BTC",
            "type": "candles_swap_utc"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC 1分鐘K線（UTC+0）...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=candles_utc_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_index_price_subscription():
    """
    示例：訂閱指數價格
    對應文檔: # 订阅指数价格
    """
    print("\n=== 訂閱指數價格示例 ===")
    
    def index_price_handler(data):
        if "data" in data and "p" in data["data"]:
            price = data["data"]["p"]
            currency = data["data"]["n"]
            print(f"📊 指數價格更新: {currency.upper()} = {price}")
        else:
            print(f"📊 指數價格: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "index_price"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC指數價格...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=index_price_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_mark_price_subscription():
    """
    示例：訂閱標記價格
    對應文檔: # 订阅标记价格
    """
    print("\n=== 訂閱標記價格示例 ===")
    
    def mark_price_handler(data):
        if "data" in data and "p" in data["data"]:
            price = data["data"]["p"]
            currency = data["data"]["n"]
            print(f"🎯 標記價格更新: {currency.upper()} = {price}")
        else:
            print(f"🎯 標記價格: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "mark_price"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC標記價格...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=mark_price_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_funding_rate_subscription():
    """
    示例：訂閱資金費率
    對應文檔: # 订阅资金费率
    """
    print("\n=== 訂閱資金費率示例 ===")
    
    def funding_rate_handler(data):
        if "data" in data and "r" in data["data"]:
            rate = data["data"]["r"]
            timestamp = data["data"]["nt"]
            currency = data["data"]["n"]
            print(f"💰 資金費率更新: {currency.upper()} = {rate}, 時間={timestamp}")
        else:
            print(f"💰 資金費率: {data}")
    
    subscription_params = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "pairCode": "BTC",
            "type": "funding_rate"
        }
    }
    
    url = "wss://ws.futurescw.com/perpum"
    
    print("🔗 訂閱BTC資金費率...")
    try:
        FuturesWebsocketPublic(url, subscription_params, on_message=funding_rate_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_orders_subscription():
    """
    示例：訂閱當前訂單（私有接口）
    對應文檔: # 订阅当前订单
    """
    print("\n=== 訂閱當前訂單示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def orders_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for order in data["data"]:
                print(f"📋 訂單更新: ID={order.get('id')}, "
                      f"合約={order.get('instrument')}, "
                      f"方向={order.get('direction')}, "
                      f"狀態={order.get('orderStatus')}, "
                      f"價格={order.get('orderPrice')}")
        else:
            print(f"📋 訂單數據: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "order"
        }
    }
    
    print("🔗 訂閱當前訂單...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=orders_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_positions_subscription():
    """
    示例：訂閱持倉（私有接口）
    對應文檔: # 订阅持仓
    """
    print("\n=== 訂閱持倉示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def positions_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for position in data["data"]:
                print(f"💼 持倉更新: 合約={position.get('instrument')}, "
                      f"方向={position.get('direction')}, "
                      f"數量={position.get('currentPiece')}, "
                      f"開倉價={position.get('openPrice')}, "
                      f"槓桿={position.get('leverage')}")
        else:
            print(f"💼 持倉數據: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "position"
        }
    }
    
    print("🔗 訂閱持倉...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=positions_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_position_changes_subscription():
    """
    示例：訂閱持倉變更（私有接口）
    對應文檔: # 订阅持仓变更
    """
    print("\n=== 訂閱持倉變更示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def position_changes_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for change in data["data"]:
                print(f"🔄 持倉變更: 合約={change.get('instrument')}, "
                      f"方向={change.get('direction')}, "
                      f"淨盈虧={change.get('netProfit')}, "
                      f"成交價={change.get('realPrice')}, "
                      f"手續費={change.get('fee')}")
        else:
            print(f"🔄 持倉變更: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "position_change"
        }
    }
    
    print("🔗 訂閱持倉變更...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=position_changes_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_assets_subscription():
    """
    示例：訂閱資產（私有接口）
    對應文檔: # 订阅资产
    """
    print("\n=== 訂閱資產示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def assets_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for asset in data["data"]:
                print(f"💰 資產更新: 幣種={asset.get('currency').upper()}, "
                      f"可用={asset.get('available')}, "
                      f"保證金={asset.get('margin')}, "
                      f"未實現盈虧={asset.get('profitUnreal')}, "
                      f"凍結={asset.get('freeze')}")
        else:
            print(f"💰 資產: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "assets"
        }
    }
    
    print("🔗 訂閱資產...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=assets_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_mega_coupon_subscription():
    """
    示例：訂閱萬能金（私有接口）
    對應文檔: # 订阅万能金
    """
    print("\n=== 訂閱萬能金示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def mega_coupon_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for coupon in data["data"]:
                print(f"🎫 萬能金更新: ID={coupon.get('agRecordId')}, "
                      f"總額={coupon.get('totalAmount')}, "
                      f"剩餘={coupon.get('currentAmount')}, "
                      f"狀態={coupon.get('status')}, "
                      f"過期時間={coupon.get('endTime')}")
        else:
            print(f"🎫 萬能金: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "assets_ag"
        }
    }
    
    print("🔗 訂閱萬能金...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=mega_coupon_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_user_settings_subscription():
    """
    示例：訂閱保證金模式（私有接口）
    對應文檔: # 订阅保证金模式
    """
    print("\n=== 訂閱保證金模式示例（需要API密鑰）===")
    
    # 請設置您的API密鑰
    API_KEY = "your_api_key"
    SEC_KEY = "your_sec_key"
    
    if API_KEY == "your_api_key":
        print("⚠️ 請先設置您的API密鑰")
        print("請修改 API_KEY 和 SEC_KEY 變量")
        return
    
    def user_settings_handler(data):
        if "data" in data and isinstance(data["data"], list):
            for setting in data["data"]:
                layout = "分開持倉" if setting.get('layout') == 1 else "合併持倉"
                margin_mode = "全倉保證金" if setting.get('positionModel') == 1 else "逐倉保證金"
                print(f"⚙️ 用戶設置更新: 持倉布局={layout}, 保證金模式={margin_mode}")
        else:
            print(f"⚙️ 用戶設置: {data}")
    
    url = "wss://ws.futurescw.com/perpum"
    subscription_payload = {
        "event": "sub",
        "params": {
            "biz": "futures",
            "type": "user_setting"
        }
    }
    
    print("🔗 訂閱保證金模式...")
    try:
        FuturesWebsocketPrivate(url, subscription_payload, API_KEY, SEC_KEY, on_message=user_settings_handler)
    except KeyboardInterrupt:
        print("⏹️ 用戶停止連接")


def example_class_based_usage():
    """
    示例：使用類的方式進行多重訂閱
    """
    print("\n=== 類方式多重訂閱示例 ===")
    
    def message_handler(data):
        msg_type = data.get("type", "unknown")
        pair_code = data.get("pairCode", "unknown")
        print(f"📡 收到消息: {msg_type} - {pair_code}")
        
        if msg_type == "ticker_swap":
            if "data" in data and isinstance(data["data"], dict):
                ticker = data["data"]
                print(f"  💹 價格: {ticker.get('last')}, 漲跌: {ticker.get('changeRate')}")
        elif msg_type == "depth":
            if "data" in data and "asks" in data["data"]:
                print(f"  📖 訂單簿已更新")
    
    # 創建客戶端
    client = CoinWFutureWebSocketClient(on_message=message_handler)
    
    try:
        # 連接
        if client.connect():
            print("✅ WebSocket連接成功")
            
            # 訂閱多個頻道
            client.subscribe({
                "event": "sub",
                "params": {
                    "biz": "futures",
                    "pairCode": "BTC",
                    "type": "ticker_swap"
                }
            })
            
            client.subscribe({
                "event": "sub",
                "params": {
                    "biz": "futures",
                    "pairCode": "BTC",
                    "type": "depth"
                }
            })
            
            # 運行一段時間
            print("🔄 運行30秒...")
            time.sleep(30)
        
        else:
            print("❌ WebSocket連接失敗")
        
    except KeyboardInterrupt:
        print("⏹️ 用戶中斷")
    finally:
        client.close()
        print("🔐 連接已關閉")


def main():
    """
    主函數：演示所有WebSocket功能
    """
    print("🚀 CoinW 期貨 WebSocket API 使用示例")
    print("=" * 60)
    
    print("\n📖 可用的示例：")
    print("1. 24小時交易摘要")
    print("2. 訂單簿")
    print("3. 交易數據")
    print("4. K線（UTC+8）")
    print("5. K線（UTC+0）")
    print("6. 指數價格")
    print("7. 標記價格")
    print("8. 資金費率")
    print("9. 當前訂單（需要API密鑰）")
    print("10. 持倉（需要API密鑰）")
    print("11. 持倉變更（需要API密鑰）")
    print("12. 資產（需要API密鑰）")
    print("13. 萬能金（需要API密鑰）")
    print("14. 保證金模式（需要API密鑰）")
    print("15. 類方式多重訂閱")
    
    try:
        choice = input("\n請選擇示例 (1-15): ").strip()
        
        examples = {
            "1": example_ticker_subscription,
            "2": example_depth_subscription,
            "3": example_fills_subscription,
            "4": example_candles_utc8_subscription,
            "5": example_candles_utc0_subscription,
            "6": example_index_price_subscription,
            "7": example_mark_price_subscription,
            "8": example_funding_rate_subscription,
            "9": example_orders_subscription,
            "10": example_positions_subscription,
            "11": example_position_changes_subscription,
            "12": example_assets_subscription,
            "13": example_mega_coupon_subscription,
            "14": example_user_settings_subscription,
            "15": example_class_based_usage
        }
        
        if choice in examples:
            examples[choice]()
        else:
            print("❌ 無效選擇，運行24小時交易摘要示例...")
            example_ticker_subscription()
            
    except KeyboardInterrupt:
        print("\n⏹️ 程序已停止")
    except Exception as e:
        print(f"\n❌ 錯誤: {e}")


if __name__ == "__main__":
    main() 