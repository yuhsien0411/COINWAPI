# 订阅24小时交易摘要
API说明
此Websocket提供交易所指定交易品种的 24 小时实时交易摘要。它包括关键市场指标，如最新交易价格、最高买入价、最低卖出价、24小时交易量等。

注意：24小时交易摘要数据只能通过 Websocket API 获取。

注意事项
目前有两种方法可用于24小时交易摘要订阅。用户在创建连接时应谨慎操作。
方法1
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

Websocket URL
wss://ws.futurescw.info?token={your_token}

频率限制
无

订阅参数
| 参数  | 必填 |   类型    | 描述                                                         |
| :---- | :--- | :-------: | ------------------------------------------------------------ |
| event | true | Subscribe | 订阅                                                         |
| args  | true |  String   | 格式："spot/market-api-ticker:\{\symbol\}\"，其中{symbol}是要订阅的货币。示例："spot/market-api-ticker:BTC-USDT" |


响应参数
参数	类型	描述
channel	String	订阅的频道，即'spot/market-api-ticker:BTC-USDT'
subject	string	主题：'spot/market-api-ticker'
buy	string	买入价
changePrice	string	价格变化
changeRate	String	价格变化百分比
high	String	过去24小时最高价
last	String	最新价格
low	String	过去24小时最低价
open	String	开盘价
sell	String	卖出价
symbol	String	货币对ID，即78 : BTC_USDT
vol	string	基础货币的交易量
volValue	String	USDT金额
订阅示例
以下Python代码展示了如何订阅BTC的24小时交易摘要。

注意：完整代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

symbol = "BTC-USDT"
args = f'spot/market-api-ticker:{symbol}'

SpotWebsocketPublic(args)   # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新24小时交易摘要。为简洁起见，以下仅提供初始响应：

{'channel': 'spot/market-api-ticker:BTC-USDT',
 'subject': 'spot/market-api-ticker',
 'data': '{
"buy":"82821.35",
"changePrice":"-610.48",
"changeRate":"-0.007317",
"high":"83799.09",
"last":"82821.45",
"low":"79998.45",
"open":"83431.93",
"sell":"82821.40",
"symbol":"78",
"vol":"10329.2388",
"volValue":"843619014.31"
}'
},.....

方法2
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"ticker"。注意：建议使用小写。
-pairCode	true	String	交易品种的标识符，例如，"78"表示BTC-USDT
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
pairCode	String	交易品种的标识符，例如，"78"表示BTC-USDT
channel	String	订阅类型，例如，"subscribe"。
type	String	消息类型，例如，"ticker"。
-result	Boolean	订阅请求的结果：true或false。
data	Json	数据对象，包含以下字段：
changePrice	bigdecimal	价格变化
changeRate	bigdecimal	价格变化率
high	bigdecimal	过去24小时最高价（以报价货币计）
last	bigdecimal	过去24小时最新价（以报价货币计）
low	bigdecimal	过去24小时最低价（以报价货币计）
open	bigdecimal	开盘价（以报价货币计）
symbol	string	货币对ID，即"78" : BTC-USDT
vol	bigdecimal	基础货币的交易量
volValue	bigdecimal	USDT金额
订阅示例
以下Python代码展示了如何订阅BTC-USDT的24小时交易摘要。

注意：完整代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

url = "wss://ws.futurescw.com"
subscription_params =  {"event":"sub",
			"params":{
				"biz":"exchange",
				"type":"ticker",
				"pairCode":"78"}}  # "78" : BTC-USDT
SpotWebsocketPublic(url, subscription_params)    # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新24小时交易摘要。为简洁起见，以下仅提供初始响应：

{"biz":"exchange","pairCode":"78","data":{"result":true},"channel":"subscribe","type":"ticker"}

{"biz":"exchange","pairCode":"78","data":
"{\"changePrice\":\"535.14\",
\"changeRate\":\"0.005678\",
\"high\":\"94827.32\",
\"last\":\"94788.99\",
\"low\":\"92788.41\",
\"open\":\"94253.85\",
\"symbol\":\"78\",
\"vol\":\"6209.9048\",
\"volValue\":\"583370376.71\"
}","type":"ticker"},.....


# 订阅所有交易品种的24小时交易摘要
API说明
此Websocket API提供实时现货市场交易品种，流式传输实时买卖盘数据。

注意：交易品种24小时交易摘要数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
此websocket返回交易所上所有交易品种的实时数据。
只有方法2可用于实现此功能。
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅：sub: 订阅，unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"ticker_all"。注意：建议使用小写。
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
channel	String	订阅类型，例如，"subscribe"。
type	String	定义功能类型，例如，"ticker_all"。
-result	Boolean	订阅请求的结果：true/false。
data	Json	数据对象，包含以下字段：
-activityState	Integer	活动状态（未提供具体含义）。
-currencyVol	BigDecimal	交易的货币总量。
-fPartitionIds	String	与市场或平台分区相关的ID。
-fav	Boolean	币对是否标记为收藏。
-hotCoinSort	Integer	根据受欢迎程度或交易量排名的币种排名。
-leftCoinName	String	交易品种的基础货币名称，即BTC
-leftCoinUrl	String	左侧币种图像的URL。
-newCoinSort	Integer	新上市币种的排序排名（用户可以忽略）
-oneDayHighest	BigDecimal	过去24小时币种的最高价格。（以报价货币计）
-oneDayLowest	BigDecimal	过去24小时币种的最低价格。（以报价货币计）
-oneDayTotal	BigDecimal	过去24小时交易的币种总量。（以基础货币计）
-price	BigDecimal	以报价货币计的最新价格。
-rightCoinName	String	交易品种的报价货币名称，即USDT
-rose	BigDecimal	以报价货币计的价格百分比变化。
-selective	Boolean	指示数据是否针对特定条件进行选择性筛选。（用户可以忽略）
-symbol	String	用于定价的货币符号（例如，"$"）。
-tmId	Integer	交易品种的标识符，例如，"78"表示BTC-USDT
-transferPrice	BigDecimal	转账价格（用户可以忽略）
-transferSymbol	String	转换货币的符号（用户可以忽略）
订阅示例
以下Python代码展示了如何订阅BTC-USDT。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

url = "wss://ws.futurescw.com"
subscription_params = {"event":"sub",
                      "params":
                      {"biz":"exchange",
                      "type":"ticker_all"}}
SpotWebsocketPublic(url, subscription_params)  # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新。为简洁起见，以下仅提供初始响应：

{"biz":"exchange","data":{"result":true},"channel":"subscribe","type":"ticker_all"}

{"biz":"exchange","data":"[{\"activityState\":0,\"currencyVol\":604768021.9400,\"fPartitionIds\":\"1,2006\",\"fav\":false,\"hotCoinSort\":46,\"leftCoinName\":\"BTC\",\"leftCoinUrl\":\"https://hkto-prod.oss-accelerate.aliyuncs.com/201810020046047_T9g8i.png\",\"newCoinSort\":0,\"oneDayHighest\":\"94827.32\",\"oneDayLowest\":\"92788.41\",\"oneDayTotal\":\"6434.1919000000\",\"price\":\"94728.91\",\"rightCoinName\":\"USDT\",\"rose\":\"0.0063\",\"selective\":false,\"symbol\":\"$\",\"tmId\":78,\"transferPrice\":\"664049.6591\",\"transferSymbol\":\"￥\"},.........]","type":"ticker_all"},........


# 订阅订单簿
API说明
此Websocket API提供指定现货市场交易品种的实时订单簿更新，流式传输实时买卖数据。

注意：订单簿数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
Websocket接口提供实时订单簿更新，默认提供20个级别的买单和卖单。
目前有两种方法可用于订单簿订阅。用户在创建连接时应谨慎操作。
方法1
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

Websocket URL
wss://ws.futurescw.info?token={your_token}

频率限制
无

订阅参数
| 参数  | 必填 |   类型    | 描述                                                         |
| :---- | :--- | :-------: | ------------------------------------------------------------ |
| event | True | subscribe | 订阅                                                         |
| args  | True |  String   | "spot/level2_20:{symbol}"，其中{symbol}是要订阅的货币。示例："spot/level2_20:BTC-USDT" |


响应参数
参数	类型	描述
channel	String	订阅的频道，即"spot/market-api-ticker:BTC-USDT"
subject	String	订阅的主题，即"spot/market-api-ticker"
data	json	数据对象
asks	Array	包含20个卖单级别的数组
String	报价货币计的价格
String	基础货币计的数量
bids	Array	包含20个买单级别的数组
String	报价货币计的价格
String	基础货币计的数量
time	Long	时间戳（毫秒）
seq	Big decimal	序列号
订阅示例
以下Python代码展示了如何订阅BTC-USDT的订单簿。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

symbol = "BTC-USDT"
args =  f'spot/level2_20:{symbol}'
SpotWebsocketPublic(args)    # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新订单簿。为简洁起见，以下仅提供初始响应：

{'channel': 'spot/level2_20:BTC-USDT',
 'subject': 'spot/level2_20',
 'data': '{
"asks":[
["85276.46","0.3085"],["85276.58","0.5241"],["85276.69","0.0396"],["85276.81","0.0447"],["85276.86","0.3087"],["85276.92","0.0454"],["85276.98","0.6008"],["85277.04","0.0685"],["85277.09","0.0259"],["85277.15","0.0466"],["85277.21","0.0469"],["85277.27","0.0485"],["85277.32","0.0374"],["85277.38","0.0437"],["85277.44","0.0784"],["85277.50","0.0378"],["85277.55","0.0989"],["85277.62","0.0714"],["85277.67","0.0270"],["85277.73","0.0547"]
],
"bids":[
["85276.10","0.6228"],["85275.87","1.3056"],["85275.84","0.7416"],["85275.78","0.0267"],["85275.72","0.7025"],["85275.66","0.0829"],["85275.61","0.0192"],["85275.55","0.0662"],["85275.49","0.0425"],["85275.43","0.0441"],["85275.38","0.0282"],["85275.32","0.0208"],["85275.30","1.2221"],["85275.26","0.0800"],["85275.20","0.0245"],["85275.15","0.0519"],["85275.08","0.0634"],["85275.03","0.0216"],["85274.97","0.0451"],["85274.92","0.0202"]
],
"time":1743151955887,
"seq":639334113}'
}


方法2
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

请求参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"depth_snapshot"。注意：建议使用小写。
-pairCode	true	String	交易品种的标识符，例如，"78"表示BTC-USDT
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
pairCode	String	交易品种的标识符，例如，"78"表示BTC-USDT
channel	String	订阅类型，例如，"subscribe"。
type	String	定义功能类型，例如，"depth_snapshot"。
-result	Boolean	订阅请求的结果：true或false。
data	Json	数据对象，包含以下字段：
asks	Array	包含20个卖单级别的数组
String	报价货币计的价格
String	基础货币计的数量
bids	Array	包含20个买单级别的数组
String	报价货币计的价格
String	基础货币计的数量
time	Long	时间戳（毫秒）
seq	Big decimal	序列号
请求示例
以下Python代码展示了如何订阅"BTC-USDT"的订单簿。

注意：完整代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

url = "wss://ws.futurescw.com"
subscription_params =  {"event":"sub",
			"params":
			{"biz":"exchange",
			"type":"depth_snapshot",
			"pairCode":"78"}} 	# "78"表示BTC-USDT

SpotWebsocketPublic(url, subscription_params) # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新订单簿。为简洁起见，以下仅提供初始响应：


{"biz":"exchange","pairCode":"78","data":{"result":true},"channel":"subscribe","type":"depth_snapshot"}

{"biz":"exchange","pairCode":"78","data":
"{\"asks\":
[[\"94702.48\",\"0.7071\"],[\"94702.98\",\"0.3480\"],
[\"94703.01\",\"0.9511\"],[\"94703.09\",\"0.2665\"],
[\"94703.20\",\"0.0152\"],[\"94703.32\",\"0.0422\"],
[\"94703.43\",\"0.0198\"],[\"94703.54\",\"0.0567\"],
[\"94703.65\",\"0.0693\"],[\"94703.77\",\"0.0386\"],
[\"94703.82\",\"0.9674\"],[\"94703.88\",\"0.0336\"],
[\"94703.99\",\"0.0196\"],[\"94704.10\",\"0.0437\"],
[\"94704.21\",\"0.0372\"],[\"94704.33\",\"0.0239\"],
[\"94704.34\",\"0.9195\"],[\"94704.44\",\"0.0343\"],
[\"94704.55\",\"0.0198\"],[\"94704.58\",\"0.7682\"]],
\"bids\":
[[\"94702.32\",\"0.2128\"],[\"94702.24\",\"0.0753\"],
[\"94702.21\",\"0.2408\"],[\"94702.12\",\"0.0540\"],
[\"94702.10\",\"0.0253\"],[\"94702.01\",\"0.0298\"],
[\"94701.98\",\"0.0377\"],[\"94701.90\",\"0.0263\"],
[\"94701.87\",\"0.0341\"],[\"94701.76\",\"0.0695\"],
[\"94701.67\",\"0.0758\"],[\"94701.65\",\"0.0635\"],
[\"94701.53\",\"0.0271\"],[\"94701.45\",\"0.0178\"],
[\"94701.42\",\"0.0166\"],[\"94701.34\",\"0.0261\"],
[\"94701.31\",\"0.0354\"],[\"94701.23\",\"0.0187\"],
[\"94701.20\",\"0.0529\"],[\"94701.09\",\"0.0471\"]],
\"time\":1745826899772,
\"seq\":704538922}",
"type":"depth_snapshot"},.................


# 订阅增量订单簿
API说明
此Websocket API提供现货市场交易品种的实时增量订单簿，流式传输实时买卖盘数据。

注意：增量订单簿数据只能通过 Websocket API 获取。

注意事项
此接口提供带有序列号的增量订单簿。如果某个序列中市场没有变化，响应将相应包含空的asks或bids。
只有方法2可用于实现此功能。
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅：sub: 订阅，unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"depth"。注意：建议使用小写。
-pairCode	true	String	交易品种的标识符，例如，"78"表示BTC-USDT
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
pairCode	String	交易品种的标识符，例如，"78"表示BTC-USDT
channel	String	订阅类型，例如，"subscribe"。
type	String	消息类型，例如，"depth"。
-result	Boolean	订阅请求的结果：true/false。
data	Json	数据对象，包含以下字段：
-startSeq	Long	深度更新的起始序列号。
-endSeq	Long	深度更新的结束序列号。
-asks	Array	卖单深度
-	String	报价货币计的价格
-	String	基础货币计的数量
-	String	序列号
-bids	Array	买单深度
-	String	报价货币计的价格
-	String	基础货币计的数量
-	String	序列号
订阅示例
以下Python代码展示了如何订阅BTC-USDT的增量订单簿。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

subscription_params =  {"event":"sub",
                        "params":{
                          "biz":"exchange",
                          "type":"depth",
                          "pairCode":"78"}} # "78"表示BTC-USDT
SpotWebsocketPublic(url, subscription_params)  # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新增量订单簿。为简洁起见，以下仅提供初始响应：

{"biz":"exchange","pairCode":"78","data":{"result":true},"channel":"subscribe","type":"depth"}

{"biz":"exchange","pairCode":"78","data":
"{\"startSeq\":4999544967,\"endSeq\":4999544973,
\"asks\":[
[\"94734.66\",\"0.1137\",\"4999544972\"],
[\"94733.65\",\"0.0685\",\"4999544971\"],
[\"94732.06\",\"0.0000\",\"4999544970\"]],
\"bids\":[
[\"94730.63\",\"0.0903\",\"4999544967\"],
[\"94728.84\",\"0.0554\",\"4999544973\"]]}","type":"depth"},......


# 订阅K线
API说明
此Websocket API提供指定交易品种的实时K线数据，包括时间戳、最高价格、最低价格、开盘价格、收盘价格和交易量等详细信息。

注意：K线数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
目前有两种方法可用于K线订阅。用户在创建连接时应谨慎操作。
方法1
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

Websocket URL
wss://ws.futurescw.info?token={your_token}

频率限制
无

请求参数
| 参数  | 必填 | 类型      |                             描述                             |
| :---- | :--- | :-------- | :----------------------------------------------------------: |
| event | True | Subscribe |                             订阅                             |
| args  | True | String    | 格式："spot/candle-{interval}:{symbol}"{interval}指K线间隔。可用选项：1m、3m、5m、15m、30m、1h、2h、4h、6h、12h、1d、1w、1M  {symbol}指要订阅的货币，如BTC-USDT示例："spot/candle-1m:BTC-USDT" |


响应参数
参数	类型	描述
channel	String	订阅的频道，即"spot/candle-1m:BTC-USDT"
subject	String	主题，即"spot/candle-1m"
data	Array	数据对象
-	String	时间戳（毫秒）
-	String	报价货币计的开盘价
-	String	报价货币计的收盘价
-	String	报价货币计的最高价
-	String	报价货币计的最低价
-	String	基础货币计的交易量
-	String	报价货币计的价格
请求示例
以下Python代码展示了如何获取BTC-USDT的K线。

注意：完整代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1。

interval= "1m"
symbol = "BTC-USDT"
args = f'spot/candle-{interval}:{symbol}'

SpotWebsocketPublic(args)   # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1)中定义


注意：完整Java代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新K线数据。为简洁起见，以下仅提供初始响应：

{'channel': 'spot/candle-1m:BTC-USDT',
 'subject': 'spot/candle-1m',
 'data': 
'["1743154440000",
"85366.41",
"85357.8",
"85366.76",
"85357.8",
"2.4926",
"212784.301823"
]'
},......

方法2
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

请求参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"candles"。注意：建议使用小写。
-pairCode	true	String	交易品种的标识符，例如，"78"表示BTC-USDT
-interval	true	String	表示K线间隔。可用选项：1m、3m、5m、15m、30m、1h、2h、4h、6h、12h、1d、1w和1M
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
pairCode	String	交易品种的标识符，例如，"78"表示BTC-USDT
channel	String	订阅类型，例如，"subscribe"。
type	String	定义功能类型，例如，"candles"。
-result	Boolean	订阅请求的结果：true或false。
data	Json	数据对象，包含以下字段：
-	String	时间戳（毫秒）
-	String	报价货币计的开盘价
-	String	报价货币计的收盘价
-	String	报价货币计的最高价
-	String	报价货币计的最低价
-	String	基础货币计的交易量
-	String	报价货币计的价格
请求示例
以下Python代码展示了如何订阅"BTC-USDT"的K线。

注意：完整代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

url = "wss://ws.futurescw.com"
subscription_params =  {"event":"sub",
                        "params":
                        {"biz":"exchange",
                        "type":"candles",
                        "pairCode":"78",     # "78"表示BTC-USDT
                        "interval":"1m"}}

SpotWebsocketPublic(url, subscription_params) # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新K线数据。为简洁起见，以下仅提供初始响应：

{"biz":"exchange","pairCode":"78","data":{"result":true},"channel":"subscribe","interval":"1m","type":"candles"}

{"biz":"exchange","pairCode":"78","data":"
[\"1745823600000\",
\"94580.17\",
\"94600.06\",
\"94600.08\",
\"94579.66\",
\"2.6366\",
\"249401.987844\"
]","interval":"1m","type":"candles"},.....


# 订阅交易
API说明
此Websocket接口提供指定交易品种的实时交易数据，包括交易数量、交易价格、总交易金额、交易时间戳和交易方向。

注意：K线数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
目前有两种方法可用于交易订阅。用户在创建连接时应谨慎操作。
方法1
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

Websocket URL
wss://ws.futurescw.info?token={your_token}

频率限制
无

订阅参数
| 参数  | 必填 |   类型    | 描述                                                         |
| :---- | :--- | :-------: | ------------------------------------------------------------ |
| event | True | subscribe | 订阅                                                         |
| args  | True |  String   | "spot/match:{symbol}"，其中{symbol}是要订阅的货币。示例，"spot/match:BTC-USDT" |


响应参数
参数	类型	描述
channel	String	订阅的频道，即"spot/match:BTC-USDT"
subject	String	主题，即"spot/match"
data	Array	数据对象
price	String	报价货币计的价格
seq	String	序列号
side	String	交易方向：BUY/SELL
size	String	基础货币计的数量
symbol	String	交易品种ID，即"78"表示BTC-USDT
time	String	交易时间（毫秒时间戳）
订阅示例
以下Python代码展示了如何订阅BTC的交易数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1。

symbol = "BTC-USDT"
args = f'spot/match:{symbol}' 
SpotWebsocketPublic(args)     # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法1

响应示例
以下是上述Python订阅返回的示例响应。Websocket将实时更新交易数据。为简洁起见，以下仅显示一条交易数据：

{'channel': 'spot/match:BTC-USDT',
 'subject': 'spot/match',
 'data': '[{
"price":"82861.81",
"seq":"127365683",
"side":"SELL",
"size":"0.0004",
"symbol":"78",
"time":"1741944585776"
}]'
}

方法2
认证
这是一个公共Websocket，不需要认证。有关使用Websocket API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub: 订阅; unsub: 取消订阅。注意：此参数区分大小写。
params	true	Json	请求的参数对象，包括：
-biz	true	String	指定频道，例如，"exchange"。注意：建议使用小写。
-type	true	String	定义功能类型，例如，"fills"。注意：建议使用小写。
-pairCode	true	String	交易品种的标识符，例如，"78"表示BTC-USDT
响应参数
参数	类型	描述
biz	String	频道名称，例如，"exchange"。
pairCode	String	交易品种的标识符，例如，"78"表示BTC-USDT
channel	String	订阅类型，例如，"subscribe"。
type	String	定义功能类型，例如，"fills"。
-result	Boolean	订阅请求的结果：true或false。
data	Json	数据对象，包含以下字段：
price	String	报价货币计的价格
seq	String	序列号
side	String	交易方向：BUY/SELL
size	String	基础货币计的数量
symbol	String	交易品种ID，即"78"表示BTC-USDT
time	String	交易时间（毫秒时间戳）
订阅示例
çç 以下Python代码展示了如何订阅BTC的交易数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2。

url = "wss://ws.futurescw.com"
subscription_params =  {"event":"sub",
                        "params":{
                          "biz":"exchange",
                          "type":"fills",
                          "pairCode":"78"}}   #78表示BTC-USDT
SpotWebsocketPublic(url, subscription_params) # 函数SpotWebsocketPublic()在章节(简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket公共接口 > 方法2

响应示例
以下是上述Python订阅返回的示例响应。Websocket将实时更新交易数据。为简洁起见，以下仅显示一条交易数据：

{"biz":"exchange","pairCode":"78","data":{"result":true},"channel":"subscribe","type":"fills"}

{"biz":"exchange","pairCode":"78","data":"[
{\"price\":\"94718.84\",
\"seq\":\"130167227\",
\"side\":\"BUY\",
\"size\":\"0.0010\",
\"symbol\":\"78\",
\"time\":\"1745825592789\"
}]","type":"fills"},.....


# 订阅当前订单
API说明
此Websocket允许用户订阅所有当前订单的实时更新，包括市价单和限价单。

注意：当前订单数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
除非下了新订单或订单状态发生变化，否则Websocket连接不会返回任何响应。如果没有变化发生，Websocket将不会提供更新。用户应确保有活跃的交易活动以接收实时更新。
对于市价单，响应中的"side"参数将返回空字符串。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	true	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	true	Json	包含以下内容的数据对象：
-biz	true	String	指定频道，例如"exchange"
-type	true	String	定义功能类型，例如"order"
响应参数
参数	类型	描述
biz	String	指定频道，例如"exchange"
type	String	定义功能类型，例如"order"
data	Array	数据对象
-fee	String	手续费
-dealFunds	String	订单金额
-type	String	订单成功：Done
-time	Long	订单时间（时间戳）
-product_id	String	交易品种，例如BTC-USDT
-order_id	String	订单ID
-client_id	String	用户分配的自定义订单ID
-size	String	以基础货币计的订单大小
-remaining_size	String	以基础货币计的剩余订单大小
-price	String	用户指定的订单价格：注意：对于市价单，它代表市场价格。
-side	String	交易方向：BUY/SELL
-order_type	String	订单类型：LIMIT - 限价，MARKET - 市价
-reason	String	原因：Cancelled/Filled
-dealAvgPrice	String	平均价格
订阅示例
以下Python代码展示了如何订阅当前订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

url = "wss://ws.futurescw.com"
subscription_payload = {"event": "sub",
                         "params": {"biz": "exchange",
                                    "type": "order"}}
 api_key= "your_api_key" 
sec_key = "your_sec_key"
SpotWebsocketPrivate(url, subscription_payload, api_key, sec_key)  # 函数SpotwWebsocketPrivate()在章节(简介 > 认证和代码示例 > 现货 > Websocket私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新当前订单。为简洁起见，下面仅提供一个订单信息：

{'data': {'result': True}, 'channel': 'login'}
{'biz': 'exchange', 'data': {'result': True}, 'channel': 'subscribe', 'type': 'order'}
{'biz': 'exchange',
 'data': {'side': 'BUY',
  'fee': '0',
  'dealFunds': '0',
  'type': 'RECEIVED',
  'client_id': 'you*******',
  'remaining_size': '0.0001',
  'size': '0.0001',
  'price': '82000',
  'product_id': 'BTC_USDT',
  'time': 1743244437255,
  'order_id': 4624530513294751114,
  'order_type': 'LIMIT'},
 'type': 'order'},.....


# 订阅资产
API说明
此Websocket在建立连接后，当用户的现货账户上发生交易活动时，提供资产余额的实时更新。

注意：资产数据可通过Restful和Websocket接口获取。本页是Websocket接口的描述。如需了解Restful接口，请参见 跳转

注意事项
Websocket连接仅返回连接建立后进入交易的订单所影响的资产的实时更新。连接前已存在的订单或已执行交易的更新将不会被推送。用户应确保有活跃的交易活动以接收实时更新。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

Websocket URL
wss://ws.futurescw.com

频率限制
无

订阅参数
参数	必填	类型	描述
event	True	String	订阅或取消订阅。sub：订阅；unsub：取消订阅。注意：此参数区分大小写。
params	True	Json	包含以下内容的数据对象：
-biz	True	String	指定频道，例如"exchange"
-type	True	String	定义功能类型，例如"assets"
响应参数
参数	类型	描述
biz	String	指定频道，例如"exchange"
type	String	定义功能类型，例如"assets"
data	Array	数据对象
-available	Long	可用余额
-currency	String	基础货币，例如BTC
-time	String	时间戳
-type	String	类型：change
-ledger_id	String	关联的账本ID
-account	String	账户：spot
-hold	String	持有量
订阅示例
以下Python代码展示了如何订阅用户资产。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

url = "wss://ws.futurescw.com"
 
subscription_payload = {"event": "sub",
                         "params": {"biz": "exchange",
                                    "type": "assets"}}
api_key= "your_api_key" 
sec_key = "your_sec_key"
SpotWebsocketPrivate(url, subscription_payload, api_key, sec_key)  # 函数SpotWebsocketPrivate()在章节(简介 > 认证和代码示例 > 现货 > Websocket私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Websocket私有接口。

响应示例
以下是上述Python订阅返回的示例响应。Websocket订阅将实时更新资产余额。为简洁起见，下面仅显示初始响应：

{'data': {'result': True}, 'channel': 'login'}
{'biz': 'exchange', 'data': {'result': True}, 'channel': 'subscribe', 'type': 'assets'}     
{'biz': 'exchange',
 'data': {'available': '12.59490035',
  'currency': 'USDT',
  'time': 1743773396836,
  'type': 'change',
  'ledger_id': 1125899934698144651,
  'account': 'spot',
  'hold': '0'},
 'type': 'assets'}
{'biz': 'exchange',
 'data': {'available': '0.0025',
  'currency': 'BTC',
  'time': 1743773396836,
  'type': 'change',
  'ledger_id': 1125899934698144652,
  'account': 'spot',
  'hold': '0'},
 'type': 'assets'}



