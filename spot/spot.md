# 获取所有交易品种24小时交易摘要
API说明
此接口提供交易所所有可用交易品种的24小时交易摘要，包括最新成交价、最高买价、最低卖价、24小时交易量等关键指标。

注意：交易品种24小时交易摘要数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
此接口返回所有交易品种的信息，不需要参数来查询特定交易品种。要访问特定交易品种的数据，请在返回的响应中查找。
对于实时更新，建议使用Websocket接口。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnTicker

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求80次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
id	String	交易品种ID，例如，78：BTC_USDT。
last	String	最新价格
lowestAsk	String	卖价
highestBid	String	买价
percentChange	String	价格变化
isFrozen	String	是否冻结：0：否，1：是
high24hr	String	24小时最高价
low24hr	String	24小时最低价
baseVolume	String	24小时以报价货币计的交易量
请求示例
以下Python代码展示了如何获取所有交易品种的24小时交易摘要。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnTicker"
 
params= {}
SpotRestfulPublic(api_url, params)  # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。为简洁起见，下面仅显示两个交易品种：

{'code': '200',
 'data': {
'BTC_USDT':
{'percentChange': '0.0135',
 'high24hr': '97371.79',
 'last': '96903.7',
 'highestBid': '96903.3200',
 'id': 78,
 'isFrozen': 0,
 'baseVolume': '773209171.37',
 'lowestAsk': '96904.3800',
 'low24hr': '95420.6'},
'ETH_USDT':
{'percentChange': '0.0102',
 'high24hr': '2757.0',
 'last': '2731.02',
 'highestBid': '2731.1400',
 'id': 79,
 'isFrozen': 0,
 'baseVolume': '220037399.94',
 'lowestAsk': '2731.2300',
 'low24hr': '2680.51'}......}
 'msg': 'SUCCESS', 
'success': True,
'failed': False
}
# 获取充提币限制信息
API说明
此接口提供交易所所有可用交易品种的详细信息，包括币种充值和提现可用性、交易费用以及最低和最高提现限额。

注意：获取充提币限制信息信息数据只能通过 Restful API 获取。

注意事项
此接口返回所有交易品种的信息，不需要参数来查询特定货币。要访问特定货币的数据，请在返回的响应中查找。
本接口支持币种级别的充提状态，不支持链级别的充提状态。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnCurrencies

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求80次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
chain	String	区块链名称
maxQty	String	最大提现金额
minQty	String	最小提现金额
recharge	String	是否支持币种充值：0：否，1：是
注意：充值状态是在币种级别返回的，而不是链级别。
symbol	String	交易品种的基础货币，即BTC。
symbolId	String	币种ID，例如BTC的"50"。
txFee	String	（用户可忽略）
withDraw	String	是否支持币种提现：0：否，1：是
注意：提现状态是在币种级别返回的，而不是链级别。
请求示例
以下Python代码展示了如何获取货币信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnCurrencies"
  
params= {}
SpotRestfulPublic(api_url, params)    # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。实际响应包含所有交易品种的信息。为简洁起见，下面仅显示BTC和ETH的信息：

{'code': '200', 
'data': 
{'BTC': {'symbolId': '50',
 'symbol': 'BTC',
 'withDraw': '1',
 'recharge': '1',
 'maxQty': '5.000000',
 'minQty': '0.001000',
 'txFee': '0.0',
 'chain': 'BTC'}, 
'ETH': {'symbolId': '16',
 'symbol': 'ETH',
 'withDraw': '1',
 'recharge': '1',
 'maxQty': '60.000000',
 'minQty': '0.010000',
 'txFee': '0.0',
 'chain': 'ETH@BSC@Arbitrum@BASE'},....
}
 'msg': 'SUCCESS', 
'success': True, 
'failed': False}

# 获取交易品种信息
API说明
此接口提供所有现货交易品种的详细信息，包括最低和最高订单价格、订单数量和价格精度。

注意：交易品种信息数据只能通过 Restful API 获取。

注意事项
此接口返回所有交易品种的信息，不需要参数来查询特定交易品种。要访问特定交易品种的数据，请在返回的响应中查找。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnSymbol

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求80次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
currencyPair	String	交易品种，例如BTC_USDT。
currencyBase	String	基础货币，例如BTC。
currencyQuote	String	报价货币，例如USDT。
maxBuyCount	String	最大订单数量
minBuyCount	String	最小订单数量
pricePrecision	Integer	价格精度
countPrecision	Integer	数量精度
minBuyAmount	String	最小订单金额
maxBuyAmount	String	最大订单金额
minBuyPrice	String	最小订单价格
maxBuyPrice	String	最大订单价格
state	Integer	交易品种状态
1：正常，
2：禁用
请求示例
以下Python代码展示了如何获取交易品种信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnSymbol"
params= {}
SpotRestfulPublic(api_url, params)   # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。为简洁起见，仅显示BTC和ETH的信息：

{'code': '200',
 'data': [
{'currencyBase': 'BTC',
 'maxBuyCount': '9999999.00000000000000000000',
 'pricePrecision': 2,
 'minBuyPrice': '0.00100000000000000000',
 'currencyPair': 'BTC_USDT',
 'minBuyAmount': '5.00000000000000000000',
 'maxBuyPrice': '99999999.00000000000000000000',
 'currencyQuote': 'USDT',
 'countPrecision': 4,
 'minBuyCount': '0.00010000000000000000',
 'state': 1,
 'maxBuyAmount': '99999999.00000000000000000000'},
{'currencyBase': 'ETH',
 'maxBuyCount': '99999999.00000000000000000000',
 'pricePrecision': 2,
 'minBuyPrice': '0.00100000000000000000',
 'currencyPair': 'ETH_USDT',
 'minBuyAmount': '5.00000000000000000000',
 'maxBuyPrice': '99999999.00000000000000000000',
 'currencyQuote': 'USDT',
 'countPrecision': 4,
 'minBuyCount': '0.00010000000000000000',
 'state': 1,
 'maxBuyAmount': '99999999.00000000000000000000'},......], 
'msg': 'SUCCESS',
 'success': True, 
'failed': False}

# 获取订单簿
API说明
此接口允许查询指定交易品种的现货市场订单簿，包括用户指定级别的买单和卖单。

注意：订单簿数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
此接口不提供时间戳信息。
订单簿深度数据仅提供5和20级。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnOrderBook

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
size	Integer	False	订单簿深度数据级别(5, 20)注意：默认为5
symbol	String	True	交易品种，例如BTC_USDT
响应参数
参数	类型	描述
asks	Array	卖方深度注意：默认返回5级卖单。
-quantity	String	以基础货币计的交易量
-price	String	以基础货币计的价格
bids	Array	买方深度注意：默认返回5级买单。
-quantity	String	以基础货币计的交易量
-price	String	以基础货币计的价格
请求示例
以下Python代码展示了如何获取BTC_USDT的订单簿。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnOrderBook"

params= {"size" : 5,
        "symbol" : "BTC_USDT",}

SpotRestfulPublic(api_url, params)   # 函数SpotRestfulPublicc()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。

{'code': '200',
 'data': {'asks': [['81517.6600', '0.6785'],
   ['81517.8400', '0.8202'],
   ['81517.9500', '0.7092'],
   ['81518.0700', '0.0232'],
   ['81518.1800', '0.0339']],
  'bids': [['81517.2600', '0.8389'],
   ['81517.1500', '0.6454'],
   ['81517.0300', '0.0366'],
   ['81516.9200', '0.0220'],
   ['81516.8100', '0.0381']]},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取最近成交
API说明
此接口允许查询指定交易品种的最近成交数据，包括成交数量、成交价格、总成交金额、成交时间、成交方向和成交记录ID。

注意：最近成交数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
如果未指定时间戳，接口将返回指定交易品种的最后50笔成交。
如果提供了开始或结束时间戳，返回的成交数据将限制为最多50条记录。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnTradeHistory

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
symbol	True	String	交易品种，例如BTC_USDT。
start	False	String	开始时间：UNIX时间戳
end	False	String	结束时间：UNIX时间戳
响应参数
参数	类型	描述
id	String	成交记录ID。
type	String	成交方向：Buy/Sell
price	String	以报价货币计的价格
amount	String	以基础货币计的成交量
total	String	以报价货币计的成交量
time	String	成交时间（时间戳）
请求示例
以下Python代码展示了如何获取BTC_USDT的成交数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnTradeHistory"
params={
    "symbol": "BTC_USDT",   
    # "start": "1579238517000", 
    # "end": "1581916917660",
       }
SpotRestfulPublic(api_url, params)  # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。实际响应包括最近50笔成交的数据。为简洁起见，下面仅显示三笔成交的数据：

{'code': '200',
 'data': [
  {'id': 127197811,
   'type': 'BUY',
   'price': '81634.91',
   'amount': '0.8377',
   'total': '68385.564107',
   'time': '2025-03-12 15:30:44'},
  {'id': 127197810,
   'type': 'SELL',
   'price': '81634.92',
   'amount': '0.0011',
   'total': '89.798412',
   'time': '2025-03-12 15:30:43'},
  {'id': 127197809,
   'type': 'SELL',
   'price': '81635.05',
   'amount': '0.0004',
   'total': '32.65402',
   'time': '2025-03-12 15:30:43'},....]
 'msg': 'SUCCESS', 
'success': True, 
'failed': False}

上一页
获取订单簿


# 获取K线
API说明
此接口允许查询指定交易品种的K线（蜡烛图）数据，包括开盘价、收盘价、最高价、最低价和交易量。

注意：K线数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
此接口返回当前时间的K线数据，间隔可能已完成或未完成。
如果未指定开始或结束时间戳，接口将默认返回100条K线数据。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=returnChartData

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
period	Integer	True	K线间隔（秒），例如，60：1分钟，180：3分钟，300：5分钟，900：15分钟，1800：30分钟，7200：2小时，14400：4小时
currencyPair	String	True	交易品种，例如BTC_USDT
start	String	False	K线开始时间（Unix 毫秒级时间戳）
end	String	False	K线结束时间（Unix 毫秒级时间戳）
响应参数
参数	类型	描述
date	Long	K线时间戳
high	String	最高价
low	String	最低价
open	String	开盘价
close	String	收盘价
volume	String	交易量
请求示例
以下Python代码展示了如何获取BTC_USDT的5分钟K线数据。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=returnChartData"
params={
    "currencyPair":"BTC_USDT",
    "period":300,
    # "start": "1579238517000",      
    # "end": "1581916917660"   
       }
SpotRestfulPublic(api_url, params)    # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。实际响应返回100条K线信息。为简洁起见，下面仅显示三条K线：

 {'code': '200',
 'data': [{'open': '9784.49',
   'high': '9786.64',
   'low': '9748.54',
   'close': '9751.8',
   'volume': '223.772822',
   'date': 1581916800000},
  {'open': '9777.25',
   'high': '9800',
   'low': '9775.87',
   'close': '9787.03',
   'volume': '143.490865',
   'date': 1581916500000},
  {'open': '9775.72',
   'high': '9780.22',
   'low': '9757.55',
   'close': '9777.32',
   'volume': '179.955498',
   'date': 1581916200000}.....],
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取热门交易品种24小时交易量
API说明
此接口允许查询交易所热门交易品种的24小时交易量。它提供主要交易品种的汇总交易量数据，包括BTC、ETH、LTC和USDT，以及总市场交易量指标。

注意：热门交易品种交易量数据只能通过 Restful API 获取。

注意事项
此接口返回过去24小时热门交易品种的交易量。它不需要参数来查询特定交易品种。要访问特定交易品种的数据，请在返回的响应中查找。
认证
这是一个公共接口，不需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

请求方法
GET

接口地址
/api/v1/public?command=return24hVolume

频率限制
该接口的调用频率限制为：每个 IP 每秒最多请求80次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
data	Json	包含热门交易品种24小时交易量的数据对象。
totalETH	String	过去24小时交易的ETH总量。
totalUSDT	String	过去24小时交易的USDT总量。
totalBTC	String	过去24小时交易的BTC总量。
ETH_USDT	Json	数据对象
-ETH	String	ETH/USDT市场中的ETH交易量。
-USDT	String	ETH/USDT市场中的USDT交易量。
LTC_CNYT	Json	数据对象
-LTC	String	LTC/CNYT市场中的LTC交易量。
-CNYT	String	LTC/CNYT市场中的CNYT交易量。
ETC_CNYT	Json	数据对象
-ETC	String	ETC/CNYT市场中的ETC交易量。
-CNYT	String	ETC/CNYT市场中的CNYT交易量。
CWT_CNYT	Json	数据对象
-CWT	String	CWT/CNYT市场中的CWT交易量。
-CNYT	String	CWT/CNYT市场中的CNYT交易量。
BTC_CNYT	Json	数据对象
-BTC	String	BTC/CNYT市场中的BTC交易量。
-CNYT	String	BTC/CNYT市场中的CNYT交易量。
BTC_USDT	Json	数据对象
-BTC	String	BTC/USDT市场中的BTC交易量。
-USDT	String	BTC/USDT市场中的USDT交易量。
LTC_USDT	Json	数据对象
-LTC	String	LTC_USDT市场中的LTC交易量。
-USDT	String	LTC_USDT市场中的USDT交易量。
msg	String	响应消息，例如"SUCCESS"
success	Boolean	表示请求是否成功：true/false
failed	Boolean	表示请求是否失败：true/false
请求示例
以下Python代码展示了如何获取热门交易品种的24小时交易量。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

api_url= "/api/v1/public?command=return24hVolume"
 
params= {}
SpotRestfulPublic(api_url, params)    # 函数SpotRestfulPublic()在章节(简介 > 认证和代码示例 > 现货 > Restful公共接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful公共接口。

响应示例
以下是上述Python请求返回的示例响应。

{'code': '200',
 'data': {'totalETH': '1118086.5235',
  'totalUSDT': '2149633150.1000',
  'ETH_USDT': {'ETH': '285517.372300', 'USDT': '548158874.9200'},
  'LTC_CNYT': {'CNYT': '0.0000', 'LTC': '0.000000'},
  'ETC_CNYT': {'ETC': '0.000000', 'CNYT': '0.0000'},
  'totalBTC': '26283.6034',
  'CWT_CNYT': {'CWT': '0.000000', 'CNYT': '0.0000'},
  'BTC_CNYT': {'BTC': '0.000000', 'CNYT': '0.0000'},
  'BTC_USDT': {'BTC': '20014.696800', 'USDT': '1594350194.0200'},
  'LTC_USDT': {'USDT': '7124081.1600', 'LTC': '79505.491700'},
  'ETH_CNYT': {'ETH': '0.000000', 'CNYT': '0.0000'}},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 下单
API说明
此接口允许用户通过指定订单类型、数量、价格和外部交易号来下现货交易订单。

注意：下单只能通过 Restful API 可用。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=doTrade

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
symbol	True	String	交易品种，例如：BTC_USDT
type	True	String	交易方向：0：买单，1：卖单。
amount	False	String	以基础货币计的订单大小。注意：限价单必填。
rate	True	String	用户指定的订单价格
funds	False	String	以报价货币计的订单大小。注意：仅对市价单有效。
isMarket	True	String	订单类型：true：市价单，false：限价单。
out_trade_no	True	String	用户分配的自定义订单ID。用户需使其唯一以区分不同订单。注意：最大长度：50个字符；仅允许拉丁字符、数字、连字符（-）和下划线（_）。
响应参数
参数	类型	描述
orderNumber	String	订单ID
请求示例
以下Python代码展示了如何为BTC-USDT下限价单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=doTrade"
method = "post"
params = {
          "symbol": "BTC_USDT",
          "type": "0",
          "amount": "0.0001",
          "rate": "82000" ,
          # "funds" : 100,
          "isMarket" : "false",
          "out_trade_no" : "3-04-11-06"
         }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': {'orderNumber': 4624603081039753080},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 取消订单
API说明
此接口允许用户通过指定订单ID取消未成交的现货订单。

注意：取消订单只能通过 Restful API 可用。

注意事项
此接口每个请求仅支持一个订单ID。不支持多个订单ID。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=cancelOrder

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
orderNumber	True	String	订单ID
响应参数
参数	类型	描述
clientOrderId	String	订单ID
请求示例
以下Python代码展示了如何通过指定订单ID取消未成交订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command\=cancelOrder"
method = "post"
params = {
        "orderNumber": "4624385377826472939"
        }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

 {'code': '200',
 'data': {'clientOrderId': 4624385377826472939},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 取消所有订单
API说明
此接口允许用户取消指定交易品种的所有未成交订单。

注意：取消所有订单只能通过 Restful API 可用。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=cancelAllOrder

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
currencyPair	False	String	交易品种，例如BTC_USDT
响应参数
参数	类型	描述
msg	string	success
请求示例
以下Python代码展示了如何取消BTC_USDT的所有未成交订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command\=cancelAllOrder"
method = "post"
params = {
            "currencyPair" :"BTC_USDT"
            }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

 {'code': '200', 'data': {}, 'msg': 'SUCCESS', 'success': True, 'failed': False}


# 获取挂单数据
API说明
此接口允许用户获取指定交易品种的所有当前未成交订单，提供订单ID、交易时间、数量和状态等详细信息。

注意：获取挂单数据可通过Restful和Websocket接口获取。本页是Restfu接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
此接口仅支持查询指定交易品种的当前未成交订单。不支持查询所有交易品种的未成交订单。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnOpenOrders

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
currencyPair	True	String	交易品种，例如BTC_USDT
startAt	False	Long	开始时间（时间戳）
endAt	False	Long	结束时间（时间戳）
响应参数
参数	类型	描述
orderNumber	String	订单ID
date	String	交易时间（时间戳）
startingAmount	String	以报价货币计的订单大小
total	String	以基础货币计的订单大小
type	String	交易方向：buy/sell
prize	String	用户设置的订单价格
success_count	String	以基础货币计的已执行订单大小
success_amount	String	以报价货币计的已执行订单大小
status	String	状态：1：未完成，2：部分完成，3：完全完成，4：用户取消
请求示例
以下Python代码展示了如何获取BTC-USDT的当前未成交订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnOpenOrders"
method = "post"
params = {
    "currencyPair": "BTC_USDT",
    "startAt": "1741671490745",
    "endAt": "1741844290745"
}
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': [{'orderNumber': 4624541508540145096,
   'date': 1743669325942,
   'startingAmount': '8.20',
   'total': '0.0001',
   'type': 'buy',
   'prize': '82000.00',
   'success_count': '0.0000',
   'success_amount': '0.00',
   'status': 1},
  {'orderNumber': 4624586588413897537,
   'date': 1743669298855,
   'startingAmount': '8.20',
   'total': '0.0001',
   'type': 'buy',
   'prize': '82000.00',
   'success_count': '0.0000',
   'success_amount': '0.00',
   'status': 1}],
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取订单详请
API说明
此接口通过指定订单ID获取订单的详细信息。

注意：订单详请只能通过 Restful API 可用。

注意事项
此接口每个请求仅接受一个订单ID。不支持指定多个订单ID。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnOrderTrades

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
orderNumber	True	String	订单ID
响应参数
参数	类型	描述
tradeID	Long	订单ID
currencyPair	String	交易品种，例如BTC_USDT
type	String	交易方向：buy/sell
amount	String	以报价货币计的当前订单大小
success_amount	String	以报价货币计的已交易订单大小
total	String	以基础货币计的当前订单大小
success_total	String	以基础货币计的已交易订单大小
fee	String	手续费
date	String	交易时间
status	Integer	状态：1：未完成，2：部分完成，3：完全完成，4：用户取消
请求示例
以下Python代码展示了如何获取订单详请。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnOrderTrades"
method = "POST"
params = {
            "orderNumber": "4624385377802383167"
        }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': {'tradeID': 4624385377802383167,
  'currencyPair': 'BTC_USDT',
  'type': 'buy',
  'amount': '0.00',
  'success_amount': '98.91',
  'total': '0.0000',
  'success_total': '0.0012',
  'fee': '0.00',
  'date': '2025-03-12 17:37:31',
  'status': 3},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取订单状态
API说明
此接口允许用户通过提供相应的订单 ID 来查询订单的状态。它返回的信息包括交易品种、方向、数量、执行状态以及时间戳。

注意：订单状态只能通过 Restful API 获取。

注意事项
此接口每个请求仅支持一个订单ID。不支持指定多个订单ID。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnOrderStatus

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求30次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
orderNumber	True	String	订单ID
响应参数
参数	类型	描述
currencyPair	String	交易品种，例如BTC_USDT
type	String	交易方向：buy/sell
total	String	以基础货币计的当前订单大小
startingAmount	String	以报价货币计的当前订单金额
status	Integer	状态：1：未完成，2：部分完成，3：完全完成，4：用户取消
date	String	交易时间
请求示例
以下Python代码展示了如何获取订单状态。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnOrderStatus"
method = "post"
params = {
            "orderNumber": "4624544807079846405"
            }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': {'status': 4,
  'currencyPair': 'BTC_USDT',
  'date': '2025-04-03 18:39:58',
  'total': '0.0001',
  'type': 'buy',
  'startingAmount': '8.20'},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取成交记录
API说明
此接口返回指定交易品种的历史成交记录.

注意：成交记录只能通过 Restful API 获取。

注意事项
此接口不返回尚未执行的订单的交易历史。
"startAt"和"endAt"参数可能无法按预期工作。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnUTradeHistory

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
currencyPair	True	String	交易品种，例如BTC_USDT
startAt	False	String	开始时间（时间戳）
endAt	False	String	结束时间（时间戳）
响应参数
参数	类型	描述
tradeID	String	交易ID
type	String	交易方向：Buy/Sell
amount	String	以报价货币计的当前订单大小
success_amount	String	以报价货币计的已交易订单大小
total	String	以基础货币计的当前订单大小
success_count	String	以基础货币计的已交易订单大小
fee	String	手续费
prize	String	用户指定的订单价格
date	String	交易时间（时间戳）
status	String	状态：1：未完成，2：部分完成，3：完全完成，4：用户取消
请求示例
以下Python代码展示了如何获取成交记录。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnUTradeHistory"
method = "post"
params = {"currencyPair": "BTC_USDT",
          "startAt":"1631526172583",
          "endAt":"1631526317779"
         }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应。为简洁起见，下面仅显示一个订单**：**

{'code': '200',
 'data': [{'tradeID': 4624544807079846405,
   'date': 1743676798747,
   'amount': '8.20',
   'total': '0.0001',
   'fee': '0.00',
   'type': 'buy',
   'prize': '82000.00',
   'success_count': '0.0000',
   'success_amount': '0.00',
   'status': 4,
   'out_trade_no': '3-04-2-4*******'}],
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取历史订单
API说明
此接口允许用户检索所有交易品种的历史订单。它支持通过特定交易品种进行可选过滤，每个请求最多返回100条记录。用户可以使用基于时间的过滤器或分页进一步细化结果，以实现高效的数据检索。

注意：历史订单数据只能通过 Restful API 获取。

注意事项
每个请求最多返回100条记录。
市价单的"orderType"将返回为"LIMIT"。
未开始交易的订单将不会在此接口中显示。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考常规信息 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=getUserTrades

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
symbol	False	String	交易品种，例如BTC_USDT
startAt	False	Long	开始时间（时间戳）
endAt	False	Long	结束时间（时间戳）
limit	False	Integer	查询数量：0 < limit <= 100
before	False	String	上一页的分页参数（如有）
after	False	String	下一页的分页参数（如有）
响应参数
参数	类型	描述
tradeId	Long	交易ID
orderId	Long	订单ID
price	string	以报价货币计的订单价格
size	String	以基础货币计的订单大小
side	String	交易方向：Buy/Sell
orderType	String	订单类型：Limit
time	Long	交易时间（时间戳）
fee	String	手续费
before	Long	上一页的分页参数（如有）
after	Long	下一页的分页参数（如有）
请求示例
以下Python代码展示了如何获取BTC_USDT的用户历史订单。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=getUserTrades"
method = "post"
params = {"symbol": "BTC_USDT",
          # "startAt":"1631526172583",
          # "endAt":"1631526317779",
         }
SpotRestuflPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestuflPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应。为简洁起见，下面仅显示一个订单数据**：**

{'code': '200',
 'data': {'list': [{'orderType': 'LIMIT',
    'orderId': 4624385377802383167,
    'fee': '0E-18',
    'price': '82429.080000000000000000',
    'size': '0.001200000000000000',
    'side': 'BUY',
    'time': 1741772251663,
    'tradeId': 127204554},.......]},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取现货账户余额
API说明
此接口检索用户现货账户的可用余额，包括不同交易品种的所有持有量。

注意：资产数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
如果用户没有资产，将返回空响应。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnBalances

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求3次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
响应包含交易品种名称和用户现货账户中持有的相应金额。

参数	类型	描述
data	Json	包含所有持有量的数据对象。
msg	String	Success
请求示例
以下Python代码展示了如何获取用户现货账户的可用余额。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnBalances"
method = "post"
params = {}
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key)    # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': {
  'BTC': '0.0012',
  'CWT': '400.000',
  'SAND': '108.467',
  'ETH': '0.0330',
  'USDT': '257.518301140000000'},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取完整现货账户余额
API说明
此接口允许用户检索其现货交易账户的完整余额详情。这里的“完整” 指的是数据维度的全面性，既包括可用余额，还包括被挂单冻结的余额，提供了账户的全貌视图，对于需要精确核算账户所有资金动向的应用场景，建议使用完整现货账户余额接口。

注意：完整现货账户余额数据只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnCompleteBalances

频率限制
该接口的调用频率限制为：每个用户 ID 每2秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
data	Json	包含所有持有量的数据对象
-available	String	可用余额
-onOrders	String	冻结余额
请求示例
以下Python代码展示了如何获取完整余额信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnCompleteBalances"
method = "post"
params = {}
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': {'BTC': {'onOrders': '0', 'available': '0.0012'},
  'CWT': {'onOrders': '0', 'available': '400'},
  'SAND': {'onOrders': '0', 'available': '108.467'},
  'ETH': {'onOrders': '0', 'available': '0.033'},
  'USDT': {'onOrders': '0', 'available': '257.51830114'}},
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 获取充值和提现历史
API说明
此接口允许用户检索指定加密货币的充值和提现记录摘要，包括金额、状态、链和转账方式。

注意：充值和提现历史数据只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnDepositsWithdrawals

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求3次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
symbol	True	String	交易品种的基础货币。（例如，BTC）
depositNumber	False	String	唯一ID
响应参数
参数	类型	描述
amount	String	数量
chain	String	区块链名称
side	Integer	1：充值，2：提现
depositNumber	String	唯一ID
address	String	充值和提现地址
txid	String	交易哈希
memo	String	备注地址
currency	String	货币名称
time	Long	充值和提现时间
confirmations	String	确认数
status	String	状态：1：等待提现，3：提现成功，4：用户提现
dest	String	提现方式：on_chain：链上提现，internal_transfer：内部转账
fromAddress	String	提现发起者的UID
toAddress	String	接收方信息。-如果"dest"是"on_chain"，这是一个链上地址。-如果"dest"是"internal_transfer"，这是一个UID、电子邮件地址或电话号码。
请求示例
以下Python代码展示了如何获取充值和提现记录。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnDepositsWithdrawals"
method = "post"
params = {"symbol":  "BTC",
         # "depositNumber" :  "" 
         }
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{
 "code":"200",
 "data":[
 {
 "amount":31659.654543,
 "chain": "ERC20",
 "side": 1,
 "depositNumber":937963,
 "address":"123",
 "txid":"已提交autocoinone937963Mon Oct 08 20:19:25 CST 2018",
 "memo": null,
 "currency":"HC",
 "time": 1704858504000,
 "confirmations":0,
 "status":3
 },{
 "amount":398.8,
 "chain": "ERC20",
 "side": 1,
 "depositNumber":903010,
 "address":"123",
 "memo": null,
 "txid":"已提交autocoinone903010Fri Aug 31 18:26:16 CST 2018",
 "currency":"HC",
 "time": 1704858504000,
 "confirmations":0,
 "status":3
 }
 ],
 "msg":"SUCCESS"
 }
# 获取充值和提现地址
API说明
此接口允许用户获取特定加密货币及其关联区块链的充值地址。

注意：充值和提现地址量数据只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=returnDepositAddresses

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求3次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
symbolId	True	String	货币ID，例如BTC的货币ID是50。
chain	True	String	区块链名称
响应参数
参数	类型	描述
minRechargeAmount	String	最低充值金额
chainName	String	区块链名称
address	Integer	充值和提现地址
请求示例
以下Python代码展示了如何获取BTC的充值和提现地址。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=returnDepositAddresses"
method = "post"
params = {
        "symbolId":  "50",
         "chain" :  "BTC" 
}
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key) # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': [{'chainName': 'BTC',
   'address': '1HCtJq9kWbBG1W24CLQ7SAiDivy6E7xHFj',
   'memo': None,
   'minRechargeAmount': '0.00001'}],
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}

# 发起提现
API说明
此接口用于发起提现，支持链上转账和CoinW用户之间的内部转账。必需参数包括金额、地址、链和备注。

注意：历史订单只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=doWithdraw

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求3次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
memo	True	String	备注
type	False	String	ordinary_withdraw，internal_transfer 默认：ordinary_withdraw
amount	True	String	提现数量
currency	True	String	货币
address	True	String	提现地址：当"type"为"ordinary_withdraw"时，提供区块链地址。当"type"为"internal_transfer"时，根据"innerToType"提供用户ID、电子邮件地址或手机号码。
chain	True	String	区块链名称，例如ERC20、TRC20、BSC
innerToType	True	Integer	内部提现地址类型。当type为internal_transfer时，需要1. 用户ID，2. 手机号码，3. 电子邮件地址。
响应参数
参数	类型	描述
depositNumber	String	唯一ID
请求示例
以下Python代码展示了如何提现。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=doWithdraw"
method = "post"
params = {
         "memo" : "None"  ,
         "type"  : "internal_transfer"  ,
         "amount" :  "0.001" ,
         "currency" : "BTC" ,
         "address"  :  "3491077",
         "chain"  :   "BTC"  ,
         "innerToType" : 1 ,
                            }
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200', 'data': {'depositNumber': '23705'}, 'msg': 'SUCCESS'}


# 取消提现
API说明
此接口允许用户通过提供相应的提现申请ID来取消先前提交的提现请求。

注意：取消提现数据只能通过 Restful API 可用。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=cancelWithdraw

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求3次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
id	True	String	提现申请ID
响应参数
参数	类型	描述
msg	String	Success
请求示例
以下Python代码展示了如何使用提现申请ID取消提现。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=cancelWithdraw"
method = "post"
params = {
    "id" : ""
}
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key)  # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200', 'data': null, 'msg': 'SUCCESS'}

# 产转账资
API说明
此API允许在现货账户和资金账户之间进行资产转账，以实现高效的资金管理。

注意：资产转账只能通过 Restful API可用。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

请求方法
POST

接口地址
/api/v1/private?command=spotWealthTransfer

频率限制
该接口的调用频率限制为：每个用户 ID 每秒最多请求1次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
accountType	True	String	源账户类型：WEALTH：资金账户，SPOT：现货账户
targetAccountType	True	String	目标账户类型：WEALTH：资金账户，SPOT：现货账户
bizType	True	String	转账方向：WEALTH_TO_SPOT：资金账户到现货账户，SPOT_TO_WEALTH：现货账户到资金账户。
coinCode	True	String	交易品种的基础货币，例如BTC
amount	True	BigDecimal	以基础币种计的转账金额。
响应参数
参数	类型	描述
data	Boolean	True
msg	String	Success
请求示例
以下Python代码展示了如何从资金账户向现货账户转账。

注意：完整代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

api_url = "/api/v1/private?command=spotWealthTransfer"
method = "post"
params = {
    "accountType" :  "WEALTH",
    "targetAccountType" : "SPOT",
    "bizType" :  "WEALTH_TO_SPOT" ,
    "coinCode" :  "BTC",
    "amount"  : 0.0001,
}
SpotRestfulPrivate(host, api_url, method, api_key, params, secret_key) # 函数SpotRestfulPrivate()在章节(简介 > 认证和代码示例 > 现货 > Restful私有接口)中定义


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 现货 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': '200',
 'data': True,
 'msg': 'SUCCESS',
 'success': True,
 'failed': False}


