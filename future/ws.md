## 订阅24小时交易摘要
API说明
此websocket允许查询指定合约的实时24小时交易摘要，包括最高价格、最低价格、最大杠杆率、总交易量、最新价格和合约大小。

注意：24小时交易摘要数据只能通过 Websocket API 获取。

注意事项
无

认证
这是一个公共websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每秒3个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	请求参数对象，包括：
-biz	true	String	指定频道，例如"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如"ticker_swap"。注意：建议使用小写。
-pairCode	true	String	合约的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的合约（例如1000PEPE），大写和小写格式都有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"
type	String	定义功能类型，例如"ticker_swap"
result	boolean	表示订阅或取消订阅是否成功：true，false
channel	String	指定执行的操作：subscribe或unsubscribe
pairCode	String	合约的基础货币，例如BTC
data	Json	数据对象，包含以下字段：
-high	String	过去24小时内的最高价格
-vol	String	过去24小时内以基础货币计价的交易量
-volUsdt	String	过去24小时内以USDT计价的交易量
-last	String	过去24小时内的最新交易价格
-low	String	过去24小时内的最低价格
-changeRate	String	过去24小时内的价格变化
-currencyCode	String	货币代码，即btc
-open	String	过去24小时内的开盘价格
订阅示例
以下Python代码展示了如何订阅BTC的24小时交易摘要。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "ticker_swap"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)     #function FuturesWebsocketPublic() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Public Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket订阅将实时更新24小时交易摘要。为简洁起见，以下仅提供Python订阅的初始响应：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'ticker_swap'}

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'high': '96721.6',
  'vol': '184464.598',
  'volUsdt': '17546484639.42',
  'last': '96192.6',
  'low': '93321.4',
  'changeRate': '-0.000020',
  'currencyCode': 'btc',
  'open': '96194.5'},
 'type': 'ticker_swap'}..............

## 订阅订单簿
API说明
此Websocket API提供指定合约的实时订单簿深度数据，包括买单和卖单。

注意：合约订单簿数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
此Websocket返回指定交易品种的深度信息。
此Websocket不允许用户指定买单/卖单数量。默认情况下，它在响应中返回100个买单和卖单。
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每2秒10个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	请求参数对象，包括：
-biz	true	String	指定频道，例如"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如"depth"。注意：建议使用小写。
-pairCode	true	String	合约的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的合约（例如1000PEPE），大写和小写格式都有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"
type	String	功能类型，例如"depth"
result	boolean	表示订阅或取消订阅是否成功：true，false
channel	String	指定执行的操作：subscribe或unsubscribe
pairCode	String	合约的基础货币，即BTC
data	Json	数据对象，包含以下字段：
-ask	List	卖方深度，包含100个
-bids	List	买方深度，包含100个
--p	BigDecimal	价格
--m	BigDecimal	数量
n	String	合约的基础货币，即btc
订阅示例
以下Python代码展示了如何订阅BTC的订单簿。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "depth"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)   # function FuturesWebsocketPublic() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Public Interface.)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket将实时更新BTC的订单簿。为简洁起见，以下仅显示Python订阅的8个级别的卖单和买单：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'depth'}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'asks': [{'p': '95640.3', 'm': '0.807'},
   {'p': '95640.5', 'm': '0.201'},
   {'p': '95640.6', 'm': '0.317'},
   {'p': '95640.7', 'm': '0.08'},
   {'p': '95640.8', 'm': '0.234'},
   {'p': '95640.9', 'm': '0.39'},
   {'p': '95641', 'm': '0.454'},
   ..........................................
   {'p': '96202.8', 'm': '5.819'}],
  'bids': [{'p': '95640.2', 'm': '0.068'},
   {'p': '95639.9', 'm': '1.381'},
   {'p': '95639.8', 'm': '0.099'},
   {'p': '95639.7', 'm': '0.655'},
   {'p': '95639.5', 'm': '0.441'},
   {'p': '95639.4', 'm': '0.187'},
   {'p': '95639.2', 'm': '1.104'},
   ..........................................
   {'p': '95095.8', 'm': '0.02'}]......},
  'n': 'btc'},
 'type': 'depth'}

## 订阅交易数据
API说明
此Websocket API提供指定合约的交易数据，包括合约大小、方向、交易ID、时间戳和价格。

注意：交易数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
无

认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每2秒50个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	请求参数对象，包括：
-biz	true	String	指定频道，例如"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如"fills"。注意：建议使用小写。
-pairCode	true	String	合约的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的合约（例如1000PEPE），大写和小写格式都有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"
type	String	功能类型，例如"fills"
result	boolean	表示订阅或取消订阅是否成功：true，false
channel	String	指定执行的操作：subscribe或unsubscribe
pairCode	String	合约的基础货币，即BTC
data	Json	数据对象，包含以下字段：
-createdDate	Long	交易发生的时间戳
-quantity	BigDecimal	基础货币的订单大小
-piece	BigDecimal	合约数量
-price	BigDecimal	已执行的交易价格
-id	Long	ID
-direction	String	交易方向：做多(long)，做空(short)
订阅示例
以下Python代码展示了如何订阅交易数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "fills"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)  # function FuturesWebsocketPublic() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Public Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket将实时更新交易数据。为简洁起见，以下仅显示Python订阅的一笔交易：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'fills'}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': [{'createdDate': 1740386094525,
   'quantity': 0.007,
   'piece': 7,
   'price': 95449,
   'id': 20742103698619397,
   'direction': 'long'}],
 'type': 'fills'},...........

## 订阅K线（UTC+8）数据
API说明
此Websocket API提供指定交易品种的K线数据，包括时间戳、最高价格、最低价格、开盘价格、收盘价格和交易量。每个蜡烛图根据UTC+8时区进行时间戳标记。

注意：K线（UTC+8）数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
每个蜡烛图根据UTC+8时区进行时间戳标记。
Websocket API不支持指定时间跨度来查询K线数据。
它提供实时K线数据，但不明确指示何时间隔已结束。用户必须监控开盘价的变化以确定新间隔的开始。
此外，时间戳在每个间隔结束时更新，作为前一间隔已结束的指示。
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每2秒20个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	请求参数对象，包括：
-biz	true	String	指定频道，例如"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如"candles_swap"。注意：建议使用小写。
-pairCode	true	String	合约的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的合约（例如1000PEPE），大写和小写格式都有效。
-interval	true	String	K线间隔，表示为："1"（1分钟）、"3"（3分钟）、"5"（5分钟）、"15"（15分钟）、"30"（30分钟）、"1H"（1小时）、"4H"（4小时）、"1D"（1天）、"1W"（1周）、"1M"（1月）。注意：此参数不区分大小写。1H和1h都有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"
type	String	定义功能类型，例如"candles_swap"
result	boolean	表示订阅或取消订阅是否成功：true，false
channel	String	指定执行的操作：subscribe或unsubscribe
pairCode	String	合约的基础货币，即BTC
data	Json	数据对象，包含以下字段：
-	BigDecimal	创建时间（时间戳）
-	BigDecimal	区间开盘价格
-	BigDecimal	区间内最高价格
-	BigDecimal	区间内最低价格
-	BigDecimal	区间收盘价格
-	BigDecimal	区间交易量（以基础货币计）
interval	String	K线时间间隔，表示为："1"（1分钟），"3"（3分钟），"5"（5分钟），"15"（15分钟），"30"（30分钟），"1H"（1小时），"4H"（4小时），"1D"（1天），"1W"（1周），"1M"（1个月）
订阅示例
以下Python代码展示了如何订阅K线数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  {
              "event": "sub",
              "params": {
                  "biz": "futures",
                  "pairCode": "btc",
                  "type": "candles_swap",
                  "interval":"1"
              }}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)  # function FuturesWebsocketPublic() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Public Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket将实时更新BTC的1分钟K线数据。为简洁起见，以下仅显示Python订阅的一条K线：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'interval': '1',
 'type': 'candles_swap'}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': ['1740333420000',
  '95585.5',
  '95616.1',
  '95583.3',
  '95583.5',
  '32.661'],
 'interval': '1',
 'type': 'candles_swap'},........

# 订阅K线（UTC+0）数据
API说明
此Websocket API提供指定交易品种的K线数据，包括时间戳、最高价格、最低价格、开盘价格、收盘价格和交易量。每个蜡烛图根据UTC+0时区进行时间戳标记。

注意：K线（UTC+0）数据只能通过 Websocket API 获取。

注意事项
每个蜡烛图根据UTC+0时区进行时间戳标记。
认证
这是一个公共websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"candles_swap_utc"。注意：建议使用小写。
-pairCode	true	String	交易品种的基础货币。（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如，1000PEPE），大写和小写格式均有效。
-interval	true	String	K线间隔，表示为："1"（1分钟）、"3"（3分钟）、"5"（5分钟）、"15"（15分钟）、"30"（30分钟）、"1H"（1小时）、"4H"（4小时）、"1D"（1天）、"1W"（1周）、"1M"（1月）。注意：此参数不区分大小写。1H和1h都有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如，"futures"。
type	String	定义功能类型，例如，"candles_swap_utc"。
result	boolean	指示订阅或取消订阅是否成功：true, false
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，即BTC。
data	Json	数据对象，包含以下字段：
-	BigDecimal	创建时间（时间戳）
-	BigDecimal	区间开盘价。
-	BigDecimal	区间内最高价。
-	BigDecimal	区间内最低价。
-	BigDecimal	区间收盘价。
-	BigDecimal	交易量（以基础货币计）
interval	String	K线间隔，表示为："1"（1分钟）、"3"（3分钟）、"5"（5分钟）、"15"（15分钟）、"30"（30分钟）、"1H"（1小时）、"4H"（4小时）、"1D"（1天）、"1W"（1周）、"1M"（1月）。
订阅示例
以下Python代码展示了如何订阅"BTC"的K线（UTC+0）数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "interval":"1",
                        "pairCode": "BTC",
                        "type": "candles_swap_utc"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)     #函数FuturesWebsocketPublic()在章节(简介 > 认证和代码示例 > 合约 > Websocket公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket订阅将实时更新K线（UTC+0）数据。为简洁起见，以下仅提供Python订阅的初始响应：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'candles_swap_utc'}

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': ['1745495580000',
  '92548.7',
  '92548.7',
  '92540.1',
  '92544.6',
  '21.729'],
 'interval': '1',
 'type': 'candles_swap_utc'},....
# 订阅指数价格
API说明
此websocket允许查询指定交易品种的指数价格。

注意：指数价格数据只能通过 Websocket API 获取。

注意事项
无

认证
这是一个公共websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"index_price"。注意：建议使用小写。
-pairCode	true	String	交易品种的基础货币。（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如，1000PEPE），大写和小写格式均有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如，"futures"
type	String	定义功能类型，例如，"index_price"
result	boolean	指示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，例如，BTC。
data	Json	数据对象，包含以下字段：
-p	Big Decimal	指数价格。
-n	String	交易品种的基础货币，例如，btc
订阅示例
以下Python代码展示了如何订阅"BTC"的指数价格。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "index_price"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)     #函数FuturesWebsocketPublic()在章节(简介 > 认证和代码示例 > 合约 > Websocket公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket订阅将实时更新指数价格。为简洁起见，以下仅提供Python订阅的初始响应：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'index_price'}
{'biz': 'futures',
 'pairCode': 'btc',
 'data': {'p': 92383.3, 'n': 'btc'},
 'type': 'index_price'},....

 # 订阅标记价格
API说明
此websocket允许查询指定交易品种的实时标记价格。

注意：标记价格数据只能通过 Websocket API 获取。

注意事项
无

认证
这是一个公共websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"mark_price"。注意：建议使用小写。
-pairCode	true	String	交易品种的基础货币。（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如，1000PEPE），大写和小写格式均有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如，"futures"
type	String	定义功能类型，例如，"mark_price"
result	boolean	指示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，例如，BTC。
data	Json	数据对象，包含以下字段：
-p	Big Decimal	指数价格。
-n	String	交易品种的基础货币，例如，btc
订阅示例
以下Python代码展示了如何订阅"BTC"的标记价格。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "mark_price"}}
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)     #函数FuturesWebsocketPublic()在章节(简介 > 认证和代码示例 > 合约 > Websocket公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket订阅将实时更新标记价格。为简洁起见，以下仅提供Python订阅的初始响应：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'mark_price'}

{'biz': 'futures',
 'pairCode': 'btc',
 'data': {'p': 92396.9, 'n': 'btc'},
 'type': 'mark_price'},....

# 订阅资金费率
API说明
此websocket允许查询指定交易品种的实时资金费率。

注意：资金费率数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
Restful API 提供最近一次结算时的资金费率信息，WebSocket API 和webpage 提供实时资金费率数据的获取。
认证
这是一个公共websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"futures"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"funding_rate"。注意：建议使用小写。
-pairCode	true	String	交易品种的基础货币。（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如，1000PEPE），大写和小写格式均有效。
响应参数
参数	类型	描述
biz	String	指定频道，例如，'futures"。
type	String	定义功能类型，例如，"funding_rate"
result	boolean	指示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，例如，BTC。
data	Json	数据对象，包含以下字段：
-r	big Decimal	资金费率
-nt	Long	时间戳（unix）
-n	string	交易品种的基础货币，例如，btc
订阅示例
以下Python代码展示了如何订阅"BTC"的资金费率。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

subscription_params =  { "event": "sub",
                        "params": {
                        "biz": "futures",
                        "pairCode": "BTC",
                        "type": "funding_rate"}}
 
url = "wss://ws.futurescw.com/perpum"
FuturesWebsocketPublic(url, subscription_params)     #函数FuturesWebsocketPublic()在章节(简介 > 认证和代码示例 > 合约 > Websocket公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket公共接口。

响应示例
Websocket订阅将实时更新资金费率。为简洁起见，以下仅提供Python订阅的初始响应：

{'biz': 'futures',
 'pairCode': 'BTC',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'funding_rate'}
{'biz': 'futures',
 'pairCode': 'btc',
 'data': {'r': 4.926e-05, 'nt': 1745490090000, 'n': 'btc'},
 'type': 'funding_rate'},.....

# 订阅当前订单
API说明
此Websocket订阅提供所有合约上所有未成交/已成交订单的实时更新。响应包括合约、方向、数量、数量单位、保证金、杠杆、maker费用、taker费用、时间戳等详情。

注意：当前订单数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
除非在建立连接后下达新订单，否则Websocket连接不会返回任何响应。如果未下达订单，将不会收到更新。用户应确保有活跃的交易活动才能接收实时订单更新。
此Websocket提供所有合约上所有未成交/已成交订单的实时更新。
认证
这是一个私有Websocket，需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每2秒30个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如"futures"。
-type	true	String	定义功能类型，例如"order"。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"。
type	String	定义功能类型，例如"order"。
result	boolean	表示订阅或取消订阅是否成功：true，false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	合约的基础货币，即BTC
data	Json	数据对象，包含以下字段：
-currentPiece	String	当前合约数量
-leverage	Integer	持仓杠杆率
-originalType	String	原始订单类型
-contractType	String	合约类型：1：永续合约
-frozenFee	String	冻结订单费用
-orderStatus	String	订单状态：unFinish：未成交，part：部分成交，Finish：完全成交，Cancel：已取消
-instrument	String	合约的基础货币，即BTC
-quantityUnit	Integer	用于指定订单数量的计量单位：
0：以计价货币计价（例如，BTC-USDT 合约中的 USDT）；
1：以合约张数计价；
2：以基础货币计价（例如，BTC-USDT 合约中的 BTC）。
-source	String	来源：api/web
-updatedDate	Long	最后订单更新的时间戳
-positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
-posType	String	持仓类型：plan/planTrigger/execute
-baseSize	String	基础货币订单规模
-liquidateBy	String	开仓和平仓事件类型
-makerFee	String	maker费用
-totalPiece	String	合约总数量
-orderPrice	String	用户指定的订单价格
-id	String	订单ID
-direction	String	交易方向：做多(long)/做空(short)
-margin	String	持仓使用的保证金
-indexPrice	String	最新指数价格
-quantity	String	基于quantityUnit 指定订单数量：
当 quantityUnit = 0 时，数量以计价货币计量（例如，BTC-USDT 中的 USDT）；
当 quantityUnit = 1 时，数量以合约张数计量；
当 quantityUnit = 2 时，数量以基础货币计量（例如，BTC-USDT 中的 BTC）。
-takerFee	String	taker费用
-userId	String	合约账户用户ID
-createdDate	Long	订单创建时间戳
-positionMargin	String	持仓保证金
-status	String	状态：open/close/cancel
订阅示例
以下Python代码展示了如何订阅当前订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

url= "wss://ws.futurescw.com/perpum"

subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "order"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"

FuturesWebsocketPrivate(url, subscription_payload, api_key, sec_key) # function FuturesWebsocketPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

响应示例
Websocket订阅将持续实时更新当前订单。为简洁起见，以下仅提供上述Python订阅的初始响应：

{"biz":"futures","data":{"result":true},"channel":"subscribe","type":"order"}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': [{'currentPiece': '1',
   'leverage': '1',
   'originalType': 'plan',
   'contractType': 1,
   'fee': '0',
   'frozenFee': '0.00954',
   'orderStatus': 'unFinish',
   'instrument': 'BTC',
   'quantityUnit': 0,
   'source': 'api',
   'updatedDate': 1739955929000,
   'positionModel': 0,
   'posType': 'plan',
   'baseSize': '0.001',
   'liquidateBy': 'manual',
   'makerFee': '0.0001',
   'totalPiece': '1',
   'orderPrice': '95400',
   'id': '33308740320587027',
   'direction': 'long',
   'margin': '95.4',
   'indexPrice': '95670.9',
   'quantity': '100',
   'takerFee': '0.0006',
   'userId': '1162061',
   'createdDate': 1739955929000,
   'positionMargin': '95.4',
   'status': 'open'}],
 'type': 'order'}.....

# 订阅持仓
API说明
此Websocket提供所有合约的所有当前持仓（已成交订单）的实时信息。

注意：当前持仓数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
此Websocket连接提供所有合约的持仓实时更新。
用户必须首先建立连接。连接后，所有合约的所有新开仓和平仓持仓将实时流式传输。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每2秒10个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	包含以下字段的数据对象：
-type	true	String	定义功能类型，例如"position"。
-biz	true	String	指定频道，例如"futures"。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"。
type	String	功能类型，例如"position"。
result	boolean	表示订阅或取消订阅是否成功：true/false
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	合约的基础货币，即BTC
data	Json	包含以下字段的数据对象：
-baseSize	String	合约中的手数
-closedPiece	String	已平仓合约数量
-closedQuantity	String	已平仓数量
-contractType	String	合约类型：1：永续合约
-createdDate	Long	创建时间戳
-currentPiece	String	当前合约数量
-direction	String	交易方向：做多(long)/做空(short)
-distId	String	分销商ID
-fee	String	费用
-fundingSettle	String	资金费率结算金额
-hedgeId	String	对冲订单ID
-id	String	持仓ID
-indexPrice	String	触发时的指数价格
-instrument	String	交易品种的基础货币，例如BTC
-isProfession	Integer	专业订单：0-否，1-是
-leaderId	String	交易员ID
-leverage	Integer	持仓杠杆率
-margin	String	持仓保证金
-openPrice	String	开仓价格（订单成交时的价格）
-orderPrice	String	用户指定的订单价格
-originalType	String	订单的原始类型：例如，plan/planTrigger/execute
-parentId	String	注册用户（被邀请者）ID：0：活跃注册用户，1：未注册用户
-partnerId	String	合作伙伴ID
-posType	String	持仓类型，例如plan/planTrigger/execute
-positionMargin	String	持仓保证金
-positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
-processStatus	Integer	处理状态：0：正常状态，1：处理中
-quantity	String	基于quantityUnit 指定订单数量：
当 quantityUnit = 0 时，数量以计价货币计量（例如，BTC-USDT 中的 USDT）；
当 quantityUnit = 1 时，数量以合约张数计量；
当 quantityUnit = 2 时，数量以基础货币计量（例如，BTC-USDT 中的 BTC）。
-quantityUnit	Integer	用于指定订单数量的计量单位：
0：以计价货币计价（例如，BTC-USDT 合约中的 USDT）；
1：以合约张数计价；
2：以基础货币计价（例如，BTC-USDT 合约中的 BTC）。
-remainCurrentPiece	String	剩余合约数量
-salesId	String	销售ID
-settlementId	String	结算ID
-source	String	来源：api/web
-status	Integer	状态：0：开仓，1：平仓，2：取消
-totalPiece	String	合约总数量
-updatedDate	Long	更新时间戳
-userId	String	用户ID
订阅示例
以下Python代码展示了如何使用Websocket订阅当前持仓（已成交订单）信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

url = "wss://ws.futurescw.com/perpum"
subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "position"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"

FuturesWebsocketPrivate(url, api_key, sec_key, subscription_payload) # function FuturesWebsocketPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
Websocket将实时更新当前持仓数据。为简洁起见，以下仅显示上述Python订阅的一个持仓信息：

{'biz': 'futures',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'position'}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': [{'currentPiece': '1',
   'isProfession': 0,
   'leverage': '1',
   'distId': '0',
   'originalType': 'execute',
   'processStatus': 0,
   'contractType': 1,
   'fee': '0.05328162',
   'openPrice': '88802.7',
   'instrument': 'BTC',
   'quantityUnit': 0,
   'source': 'api',
   'updatedDate': 1740569719634,
   'positionModel': 0,
   'posType': 'execute',
   'leaderId': '1162061',
   'baseSize': '0.001',
   'closedQuantity': '0',
   'salesId': '0',
   'totalPiece': '1',
   'orderPrice': '0',
   'id': '2435521222631981320',
   'fundingSettle': '0',
   'direction': 'short',
   'margin': '88.8027',
   'indexPrice': '88802.8',
   'quantity': '88.8027',
   'userId': '1162061',
   'parentId': '0',
   'closedPiece': '0',
   'createdDate': 1740569719634,
   'hedgeId': '20766171808644102',
   'partnerId': '0',
   'positionMargin': '88.8027',
   'remainCurrentPiece': '1',
   'status': 'open'}],
 'type': 'position'},.......

# 订阅持仓变更
API说明
此Websocket提供所有交易品种的持仓变更（已成交订单）的实时更新。此websocket还提供已实现净盈亏的更新。

注意：持仓变更数据只能通过 Restful API 获取。

注意事项
用户必须先建立连接。一旦连接，所有交易品种的持仓变更将实时推送。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅：sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	包含以下字段的数据对象：
-type	true	String	定义功能类型，例如，"position_change"。
-biz	true	String	指定频道，例如，"futures"。
响应参数
参数	类型	描述
biz	String	指定频道，例如，"futures"。
type	String	功能类型，例如，"position_change"。
result	boolean	指示订阅或取消订阅是否成功：true/false
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，即BTC
data	Json	包含以下字段的数据对象：
-currentPiece	String	当前合约数量
-isProfession	Integer	表示匹配服务器处理状态
-leverage	String	应用于持仓的杠杆率。
-originalType	String	订单的原始类型，例如，"execute"。
-orderId	String	订单ID。
-contractType	Integer	合约类型：1：永续合约。
-openId	String	开仓位置的唯一ID。
-fee	String	手续费
-openPrice	String	开仓价格（订单成交价格）
-orderStatus	String	订单状态，例如，"finish"。
-instrument	String	交易品种的基础货币，例如，"BTC"。
-quantityUnit	Integer	用于指定订单数量的计量单位：
0：以计价货币计价（例如，BTC-USDT 合约中的 USDT）；
1：以合约张数计价；
2：以基础货币计价（例如，BTC-USDT 合约中的 BTC）。
-source	String	来源：api/web
-updatedDate	Long	更新时间戳（毫秒）。
-positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
-feeRate	String	计算费用的费率。
-netProfit	String	已实现净盈亏。
-baseSize	String	基础货币计的订单大小
-liquidateBy	String	持仓平仓事件，例如，"manual"。
-totalPiece	String	合约总数量。
-orderPrice	String	用户指定的订单价格。
-id	String	交易条目的唯一标识符。
-fundingSettle	String	此持仓结算的资金费用金额。
-direction	String	交易方向：long/short
-margin	String	用于持仓的保证金。
-takerMaker	Integer	taker为1，maker为2。
-indexPrice	String	指数价格
-quantity	String	基于quantityUnit 指定订单数量：
当 quantityUnit = 0 时，数量以计价货币计量（例如，BTC-USDT 中的 USDT）；
当 quantityUnit = 1 时，数量以合约张数计量；
当 quantityUnit = 2 时，数量以基础货币计量（例如，BTC-USDT 中的 BTC）。
-userId	String	用户ID
-closedPiece	String	已平仓的合约数量。
-createdDate	Long	创建时间戳
-hedgeId	String	对冲ID。
-closePrice	String	持仓平仓价格
-positionMargin	String	分配给持仓的保证金。
-realPrice	String	订单的执行价格。
-status	String	状态：0：开仓，1：平仓，2：取消
订阅示例
以下Python代码展示了如何订阅持仓变更。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

url = "wss://ws.futurescw.com/perpum"
subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "position_change"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"
FuturesWebsocketPrivate(url, api_key, sec_key, subscription_payload) # 函数FuturesWebsocketPrivate()在章节(简介 > 认证和代码示例 > 合约 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
Websocket将实时更新持仓变更。为简洁起见，以下仅显示上述Python订阅的一个持仓变更：

{'biz': 'futures',
 'data': {'result': true},
 'channel': 'subscribe',
 'type': 'position_change'}
{'biz': 'futures',
 'pairCode': 'BTC',
 'data': [{'currentPiece': '1',
   'isProfession': 0,
   'leverage': '5',
   'originalType': 'execute',
   'orderId': '33308809187064313',
   'contractType': 1,
   'openId': '2435521222633466843',
   'fee': '0.055707',
   'openPrice': '92845',
   'orderStatus': 'finish',
   'instrument': 'BTC',
   'quantityUnit': 1,
   'source': 'api',
   'updatedDate': 1745501769376,
   'positionModel': 0,
   'feeRate': '0.0006',
   'netProfit': '0',
   'baseSize': '0.001',
   'liquidateBy': 'manual',
   'totalPiece': '1',
   'orderPrice': '2147483647',
   'id': '21412625432427527',
   'fundingSettle': '0',
   'direction': 'long',
   'margin': '18.513293',
   'takerMaker': 1,
   'indexPrice': '92844.9',
   'quantity': '18.569',
   'userId': '1162061',
   'closedPiece': '0',
   'createdDate': 1745501769376,
   'hedgeId': '21412625432427528',
   'closePrice': '0',
   'positionMargin': '18.569',
   'realPrice': '92845',
   'status': 'open'}],
 'type': 'position_change'},.....

# 订阅资产
API说明
此Websocket接口允许用户检索合约账户资产信息，包括可用保证金、USDT余额和冻结资产等。

注意：资产数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
除非资产发生变化，否则Websocket连接不会返回任何响应。如果没有变化发生，Websocket将不提供更新。用户应确保有活跃的交易活动以接收实时资产更新。
认证
这是一个私有Websocket，需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每用户ID每2秒10个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	数据对象，包含以下字段：
-biz	true	String	指定频道，例如"futures"。
-type	true	String	定义功能类型，例如"assets"。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"。
type	String	功能类型，例如"assets"
result	boolean	表示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，即BTC
data	Json	包含以下字段的数据对象：
-margin	BigDecimal	为持仓分配的保证金金额
-profitUnreal	BigDecimal	持仓的未实现盈亏
-freeze	BigDecimal	由于未成交订单或其他限制而冻结的资金金额
-size	BigDecimal	持有的合约总规模或资产数量
-available	BigDecimal	可用于交易或提款的USDT余额
-currency	String	报价货币（例如，USDT）
-type	Integer	账户类型或分类（用户可忽略）
-almightyGold	BigDecimal	万能金余额
-transferAvailable	BigDecimal	可用于转账的金额
-userId	Long	合约账户用户ID
-availableMargin	BigDecimal	可用保证金
-hold	BigDecimal	当前在订单/持仓中持有的金额
订阅示例
以下Python代码展示了如何使用Websocket订阅资产。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

url = "wss://ws.futurescw.com/perpum"
subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "assets"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"

FuturesWebsocketPrivate(url, api_key, sec_key, subscription_payload) # function FuturesWebsocketPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

响应示例
以下是上述Python订阅返回的示例响应，它会实时更新：

{'biz': 'futures',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'assets'}
{'biz': 'futures',
 'pairCode': 'USDT',
 'data': [{'margin': 0.0,
   'profitUnreal': 0,
   'freeze': 0.0,
   'size': 0,
   'available': 488.53777423,
   'currency': 'usdt',
   'type': 7,
   'almightyGold': 0,
   'transferAvailable': 488.53777423,
   'userId': 1162061,
   'availableMargin': 488.53777423,
   'hold': 0.0},
  {'margin': 0.0,
   'profitUnreal': 0,
   'freeze': 0.0,
   'size': 0,
   'available': 488.53777423,
   'currency': 'usdt',
   'type': 7,
   'almightyGold': 0,
   'transferAvailable': 488.53777423,
   'userId': 1162061,
   'availableMargin': 488.53777423,
   'hold': 0.0}],
 'type': 'assets'},.........

# 订阅万能金
API说明
此Websocket提供万能金的实时更新，仅在万能金发放或接近过期时推送信息。它提供余额、状态、有效期以及是否需要高级KYC验证等关键详情，有助于高效的资产管理。

有关万能金的更多详情，请参考 https://coinw.zendesk.com/hc/en-us/articles/23111150445977-Introduction-to-Futures-Mega-Coupon

注意：资产数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
此Websocket仅在万能金发放或接近过期时推送更新。
认证
这是一个私有Websocket，需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每用户ID每2秒1个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	包含以下字段的数据对象：
-biz	true	String	指定频道，例如"futures"。
-type	true	String	定义功能类型，例如"assets_ag"。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"。
type	String	功能类型，例如"assets_ag"。
result	boolean	表示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
pairCode	String	交易品种的基础货币，即BTC
data	Json	包含以下字段的数据对象：
-agRecordId	Long	万能金ID
-updateDate	Long	更新时间（时间戳）
-backAmount	BigDecimal	逾期金额
-currentAmount	BigDecimal	剩余金额
-remark	String	备注
-userId	Long	用户ID
-totalAmount	BigDecimal	万能金总额
-createdDate	Long	创建时间（时间戳）
-kyc	Integer	高级KYC要求：1：是，0：否
-assetsOut	BigDecimal	转出的资产是否无效：1：是，0：否
-startTime	Long	有效期开始时间（时间戳）
-endTime	Long	有效期截止日期（时间戳）
-status	Integer	状态：0：待生效，1：未使用，2：已使用，3：已过期，4：发放失败
订阅示例
以下Python代码展示了如何使用Websocket订阅万能金。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

url = "wss://ws.futurescw.com/perpum"
subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "assets_ag"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"
 
FuturesWebsocketPrivate(url, api_key, sec_key, subscription_payload) # function FuturesWebsocketPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

响应示例
以下是上述Python订阅返回的示例响应，它会实时更新：

{'event': 'sub', 'params': {'biz': 'futures', 'type': 'assets_ag'}}
{'biz': 'futures',
 'data': [{'agRecordId': 475,
   'updateDate': 1713192123887,
   'backAmount': 0,
   'currentAmount': 11,
   'remark': '',
   'userId': 600001274,
   'totalAmount': 11,
   'createdDate': 1713192123887,
   'kyc': 1,
   'assetsOut': 1,
   'startTime': 1713192110000,
   'endTime': 1713278512000,
   'status': 1}],
 'type': 'assets_ag'}.........

# 订阅保证金模式
API说明
此Websocket提供保证金模式（逐仓或全仓保证金）和持仓布局（合并或分开持仓）的实时更新，使用户能够有效管理其交易策略。

注意：保证金模式可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
除非在建立连接后保证金模式或持仓布局发生变化，否则Websocket不会返回数据。如果没有变化发生，将不会发送更新。
认证
这是一个私有Websocket，需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com/perpum

频率限制
此订阅的频率限制为每IP每秒3个请求。

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	包含以下内容的数据对象：
-biz	true	String	指定频道，例如"futures"。
-type	true	String	定义功能类型，例如"user_setting"。
响应参数
参数	类型	描述
biz	String	指定频道，例如"futures"。
type	String	定义功能类型，例如"user_setting"。
result	boolean	表示订阅或取消订阅是否成功：true, false。
channel	String	指定执行的操作：subscribe或unsubscribe。
-layout	Integer	持仓布局：0：合并持仓，1：分开持仓
-positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
-userId	Long	合约账户用户ID
订阅示例
以下Python代码展示了如何检查持仓布局和持仓保证金模式。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

url = "wss://ws.futurescw.com/perpum"
subscription_payload = {"event": "sub",
                         "params": {"biz": "futures",
                                    "type": "user_setting"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"

FuturesWebsocketPrivate(url, api_key, sec_key, subscription_payload) # function FuturesWebsocketPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Websocket Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Websocket私有接口。

响应示例
以下是上述Python订阅返回的示例响应，它会实时更新：

{'biz': 'futures',
 'data': {'result': True},
 'channel': 'subscribe',
 'type': 'user_setting'}
{'biz': 'futures',
 'data': [{'layout': 1, 'positionModel': 1, 'userId': 600001359}],
 'type': 'user_setting'}.....
 