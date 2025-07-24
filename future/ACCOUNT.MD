## 获取最大可转账余额
API说明
此接口允许查询用户合约账户中的最大可转账余额。

注意：最大可转账余额数据只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/account/available

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
此接口不需要任何请求参数。

响应参数
参数	类型	描述
data	BigDecimal	最大可转账金额
请求示例
以下Python代码展示了如何获取用户合约账户的最大可转账余额。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {}
api_url = "/v1/perpum/account/available"
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)    # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0, 'data': {'value': '438.799142390000018'}, 'msg': ''}

## 获取交易详情（3天）
API说明
此接口允许查询过去三天的全面交易详情摘要，包括订单状态、持仓详情、费用、盈亏、杠杆、保证金等关键交易指标。

注意：交易详情数据只能通过 Restful API 获取。

注意事项
如果某个订单已成交，请求参数"originalType"可能会产生误导，因为即使请求指定类型（plan或execute），接口返回的响应是相同的。用户不应仅依赖此参数来确定订单性质，应验证额外的订单详情（订单状态、持仓ID、订单ID）以确保准确性。
响应参数"total"也可能产生误导，因为在已成交订单的情况下，即使指定了特定类型，execute和plan订单都会被包含在内。建议不要仅依赖此参数。
未成交订单不会在此接口中显示。但是，如果未成交订单被取消，取消将通过此接口反映出来。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/orders/deals

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
page	false	Integer	当前页码
pageSize	false	Integer	每页响应数量
originType	false	String	初始订单类型：execute：市价单plan：用于不同计划订单，包括限价单、触发限价单、带SL/TP的限价单、带SL/TP的触发限价单、触发市价单、带SL/TP的触发市价单planTrigger：计划触发订单
instrument	true	String	交易品种的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如1000PEPE），大写和小写格式都有效。
positionModel	false	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
响应参数
参数	类型	描述
closePrice	BigDecimal	持仓平仓价格
userId	Long	合约账户用户ID
closedPiece	BigDecimal	已平仓合约
createdDate	Long	订单创建的时间戳
currentPiece	BigDecimal	当前合约数量
direction	String	交易方向：做多(long)/做空(short)
fee	BigDecimal	费用
feeRate	BigDecimal	手续费率
fundingSettle	BigDecimal	资金费率结算金额
hedgeId	Long	对冲ID
indexPrice	BigDecimal	指数价格/最新价格
instrument	String	交易品种的基础货币，例如BTC或ETH
leverage	BigDecimal	持仓杠杆率
liquidateBy	String	平仓或开仓事件类型
margin	BigDecimal	为此持仓分配的保证金
netProfit	BigDecimal	净利润
openId	Long	持仓ID
openPrice	BigDecimal	订单实际成交的开仓价格
orderId	Long	订单ID
orderPrice	BigDecimal	用户指定的订单价格
orderStatus	String	订单状态：unFinish：未成交，part：部分成交，Finish：完全成交，Cancel：已取消
originalType	String	原始订单类型
positionMargin	BigDecimal	持仓保证金
positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
quantity	BigDecimal	基于quantityUnit 指定订单数量：
当 quantityUnit = 0 时，数量以计价货币计量（例如，BTC-USDT 中的 USDT）；
当 quantityUnit = 1 时，数量以合约张数计量；
当 quantityUnit = 2 时，数量以基础货币计量（例如，BTC-USDT 中的 BTC）。
quantityUnit	Integer	用于指定订单数量的计量单位：
0：以计价货币计价（例如，BTC-USDT 合约中的 USDT）；
1：以合约张数计价；
2：以基础货币计价（例如，BTC-USDT 合约中的 BTC）。
settlementId	Long	交易对手ID
status	String	交易状态：open：活跃持仓，close：已平仓持仓，cancel：已取消订单
takerMaker	Integer	标识交易是吃单还是挂单交易：1-吃单，2-挂单
totalPiece	BigDecimal	合约总数量
updatedDate	Long	最新交易更新的时间戳
thirdOrderId	String	用户分配的自定义订单ID
id	Long	ID
contractType	Integer	合约类型：1：永续合约
baseSize	Integer	合约规模
isProfession	Integer	（用户可忽略）
processStatus	Integer	匹配服务器处理状态：0：等待，1：处理中，2：成功，3：失败
source	String	来源：web/api
total	Integer	交易总数
请求示例
以下Python代码展示了如何获取过去三天BTC的交易详情。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
    "instrument" : "btc",
    "positionModel" : 0,
    "originType" : "plan",
    "page" : 1,
    # "pageSize" : 1,
    }
 
api_url = "/v1/perpum/orders/deals"
request_url = f'{base_url}{api_url}'
 
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)    # the function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应。实际响应包含73个交易历史。为简洁起见，以下仅显示一个交易历史：

{'code': 0,
 'data': {'nextId': 0,
  'prevId': 0,
  'rows': [{'baseSize': 0.001,
 'closePrice': 0,
 'closedPiece': 0,
 'contractType': 1,
 'createdDate': 1741325037000,
 'currentPiece': 0,
 'direction': 'long',
 'fee': '0',
 'feeRate': '0',
 'fundingFee': '0',
 'fundingSettle': 0,
 'id': 20865618454160389,
 'instrument': 'BTC',
 'isProfession': 0,
 'leverage': 1,
 'liquidateBy': 'moveStopProfitAndLoss',
 'margin': 87.90975,
 'netProfit': 0,
 'openId': 2435521222632288678,
 'openPrice': 87909.75,
 'orderId': 20865172723909637,
 'orderPrice': 0,
 'orderStatus': 'cancel',
 'originalType': 'moveStopProfitLoss',
 'positionMargin': 0.0,
 'positionModel': 0,
 'processStatus': 1,
 'quantity': 1,
 'quantityUnit': 1,
 'source': 'api',
 'status': 'close',
 'takerMaker': 1,
 'thirdOrderId': '07-9-16',
 'totalPiece': 1,
 'triggerPrice': 0,
 'triggerType': 1,
 'updatedDate': 1741328437000,
 'userId': 1162061}......],
  'total': 73},
 'msg': ''}

## 获取交易详情（3个月）
API说明
此接口允许查询过去三个月的全面交易详情摘要，包括订单状态、持仓详情、费用、盈亏、杠杆和保证金等关键交易指标。

注意：交易详情数据只能通过 Restful API 获取。

注意事项
如果某个订单已成交，请求参数"originalType"可能会产生误导，因为即使请求指定类型（plan或execute），接口返回的响应是相同的。用户不应仅依赖此参数来确定订单性质，应验证额外的订单详情（订单状态、持仓ID、订单ID）以确保准确性。
响应参数"total"也可能产生误导，因为在已成交订单的情况下，即使指定了特定类型，execute和plan订单都会被包含在内。建议不要仅依赖此参数。
未成交订单不会在此接口中显示。但是，如果未成交订单被取消，取消将通过此接口反映出来。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/orders/deals/history

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
page	false	Integer	当前页码
pageSize	false	Integer	每页响应数量
originType	false	String	初始订单类型：execute：市价单plan：用于不同计划订单，包括限价单、触发限价单、带SL/TP的限价单、带SL/TP的触发限价单、触发市价单、带SL/TP的触发市价单planTrigger：计划触发订单
instrument	true	String	交易品种的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如1000PEPE），大写和小写格式都有效。
positionModel	false	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
响应参数
参数	类型	描述
closePrice	BigDecimal	持仓平仓价格
userId	Long	合约账户用户ID
closedPiece	BigDecimal	已平仓合约
createdDate	Long	订单创建的时间戳
currentPiece	BigDecimal	当前合约数量
direction	String	交易方向：做多(long)/做空(short)
fee	BigDecimal	费用
feeRate	BigDecimal	手续费率
fundingSettle	BigDecimal	资金费率结算金额
hedgeId	Long	对冲ID
indexPrice	BigDecimal	指数价格/最新价格
instrument	String	交易品种的基础货币，例如BTC或ETH
leverage	BigDecimal	持仓杠杆率
liquidateBy	String	平仓或开仓事件类型
margin	BigDecimal	为此持仓分配的保证金
netProfit	BigDecimal	净利润
openId	Long	持仓ID
openPrice	BigDecimal	订单实际成交的开仓价格
orderId	Long	订单ID
orderPrice	BigDecimal	用户指定的订单价格
orderStatus	String	订单状态：unFinish：未成交，part：部分成交，Finish：完全成交，Cancel：已取消
originalType	String	原始订单类型
positionMargin	BigDecimal	持仓保证金
positionModel	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
quantity	BigDecimal	基于quantityUnit 指定订单数量：
当 quantityUnit = 0 时，数量以计价货币计量（例如，BTC-USDT 中的 USDT）；
当 quantityUnit = 1 时，数量以合约张数计量；
当 quantityUnit = 2 时，数量以基础货币计量（例如，BTC-USDT 中的 BTC）。
quantityUnit	Integer	用于指定订单数量的计量单位：
0：以计价货币计价（例如，BTC-USDT 合约中的 USDT）；
1：以合约张数计价；
2：以基础货币计价（例如，BTC-USDT 合约中的 BTC）。
settlementId	Long	交易对手ID
status	String	交易状态：open：活跃持仓，close：已平仓持仓，cancel：已取消订单
takerMaker	Integer	标识交易是吃单还是挂单交易：1-吃单，2-挂单
totalPiece	BigDecimal	合约总数量
updatedDate	Long	最新交易更新的时间戳
thirdOrderId	String	用户分配的自定义订单ID
id	Long	ID
contractType	Integer	合约类型：1：永续合约
baseSize	Integer	合约规模
isProfession	Integer	（用户可忽略）
processStatus	Integer	匹配服务器处理状态：0：等待，1：处理中，2：成功，3：失败
source	String	来源：web/api
total	Integer	交易总数
请求示例
以下Python代码展示了如何获取过去三个月BTC的交易详情。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
    "instrument" : "btc", 
    "positionModel" : 1,
    "originType" : "plan",
    # "page" : 1,
    # "pageSize" : 1,
    }
 
api_url = "/v1/perpum/orders/deals"
request_url = f'{base_url}{api_url}'
 
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)      # the function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface.)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应。实际响应包含21个交易历史。为简洁起见，以下仅显示一个交易历史：

{'code': 0,
 'data': {'nextId': 0,
  'prevId': 0,
  'rows': [{'baseSize': 0.001,
 'closePrice': 85992.4,
 'closedPiece': 1,
 'contractType': 1,
 'createdDate': 1740645498000,
 'currentPiece': 0,
 'direction': 'long',
 'fee': '0.05159544',
 'feeRate': '0.0006',
 'fundingFee': '0',
 'fundingSettle': 0,
 'hedgeId': 20776111118334982,
 'id': 20776111118334981,
 'indexPrice': 85992.5,
 'instrument': 'BTC',
 'isProfession': 0,
 'leverage': 1,
 'liquidateBy': 'manual',
 'margin': 85.9926,
 'netProfit': -0.05179544,
 'openId': 2435521222632017955,
 'openPrice': 85992.6,
 'orderId': 33308749975880237,
 'orderPrice': 0,
 'orderStatus': 'finish',
 'originalType': 'execute',
 'positionMargin': 85.9926,
 'positionModel': 1,
 'processStatus': 1,
 'quantity': 85.9926,
 'quantityUnit': 1,
 'settlementId': 588150,
 'source': 'api',
 'status': 'close',
 'takerMaker': 1,
 'thirdOrderId': '27-12-32',
 'totalPiece': 1,
 'updatedDate': 1740645551000,
 'userId': 1162061}.....],
  'total': 21},
 'msg': ''}

## 获取合约账户资产
API说明
此接口允许用户查询合约账户资产信息，包括可用保证金、USDT余额和冻结资产等。

注意：合约账户资产数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
响应参数"availableMargin"在已成交订单的情况下可能具有误导性，因为它包括"alMargin"（当前分配给已成交订单的保证金），而不仅仅是自由可用的保证金。更多说明请参考官方网站。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/account/getUserAssets

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
无

响应参数
参数	类型	描述
availableMargin	BigDecimal	可用保证金余额（包括万能金）
userId	Long	合约账户用户ID
almightyGold	BigDecimal	可用万能金余额
availableUsdt	BigDecimal	可用USDT余额
alMargin	BigDecimal	持有资产（用于已成交订单）
alFreeze	BigDecimal	冻结资产（用于未成交订单）
time	Long	检索响应数据的时间戳
请求示例
以下Python代码展示了如何获取用户的合约账户资产信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = { }
api_url = "/v1/perpum/account/getUserAssets"
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key) # the function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0,
 'data': {'alFreeze': 0,
  'alMargin': 0.14311,
  'almightyGold': 4.64407693,
  'availableMargin': 499.71964459000003,
  'availableUsdt': 495.07556766,
  'time': 1742374984772,
  'userId': 1162061},
 'msg': ''}

## 获取合约账户费用
API说明
此接口允许查询用户的合约账户手续费率，包括maker和taker费用。

注意：合约账户费用数据只能通过 Restful API 获取。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/account/fees

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求2次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
无

响应参数
参数	类型	描述
makerFee	BigDecimal	maker费用
takerFee	BigDecimal	taker费用
userId	Long	合约合约用户ID
请求示例
以下Python代码展示了如何获取用户的合约账户手续费。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = { }
api_url = "/v1/perpum/account/fees"
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)   # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0,
 'data': {'makerFee': '0.0001', 'takerFee': '0.0006', 'userId': 1162061},
 'msg': ''}

## 获取万能金余额
API说明
此接口提供万能金余额信息，允许用户根据时间范围和状态筛选数据。它提供万能金余额、状态和有效期等关键详情，实现高效的资产管理。此外，此接口帮助用户确定使用时是否需要高级身份验证。

有关万能金的更多信息，请参考 https://coinw.zendesk.com/hc/en-us/articles/23111150445977-Introduction-to-Futures-Mega-Coupon

注意：万能金余额数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/account/almightyGoldInfo

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求1次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
startTime	false	Long	有效期开始时间
endTime	false	Long	有效期截止时间
type	true	Integer	万能金状态：0：待生效，1：未使用，2：已使用，3：已过期，4：发放失败
响应参数
参数	类型	描述
id	Long	万能金ID
assetsOut	Integer	转出的资产是否无效：1：是，0：否
agRecordId	Integer	发放记录ID
kyc	Integer	是否需要高级KYC：1：是，0：否
currentAmount	BigDecimal	剩余金额
totalAmount	BigDecimal	万能金总额
type	Integer	状态：0：待生效，1：未使用，2：已使用，3：已过期，4：发放失败
startTime	long	有效期开始的时间戳
endTime	long	有效期结束的时间戳
remark	String	备注
createdDate	long	创建日期的时间戳
updateDate	long	最后更新的时间戳
userId	Long	用户ID
请求示例
以下Python代码展示了如何获取万能金余额信息。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
    # "startTime" : "1740467460000",
    # "endTime" : "1740467430000",
    "type" : 3,    
    }
api_url = "/v1/perpum/account/almightyGoldInfo"
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key).  # the function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0,
 'data': [{'agRecordId': 4004,
   'assetsOut': 0,
   'backAmount': 0,
   'backMark': 0,
   'createdDate': 1740555154000,
   'currentAmount': 5,
   'endTime': 1742918400000,
   'id': 800149683,
   'kyc': 0,
   'name': '万能金',
   'processStatus': 0,
   'remark': '产品测试 Aimen Malik',
   'startTime': 1740555125000,
   'totalAmount': 5,
   'transferExpire': 0,
   'type': 1,
   'updateDate': 1740555154000,
   'userId': 1162061}],
 'msg': ''}


## 单位转换
API说明
此接口允许在合约交易中进行合约单位（张数）和加密货币（币）之间的转换。

注意：单位转换数据只能通过 Restful API可用。

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
POST

接口地址
/v1/perpum/pieceConvert

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
convertType	true	Long	转换类型：1：将合约单位（张数）转换为币，2：将币转换为合约单位（张数）注意：对于"1"：dealPiece是必需的，对于"2"：baseSize是必需的
dealPiece	false	BigDecimal	合约数量
faceValue	true	BigDecimal	每手最小价值
baseSize	false	BigDecimal	面值*份数（币的数量）
响应参数
参数	类型	描述
value	BigDecimal	合约或币的值
请求示例
以下Python代码展示了如何将合约转换为币。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
          "convertType": 1,
          "dealPiece": 11,
          "faceValue": 0.001,
         }
api_url = "/v1/perpum/pieceConvert"
method = "POST"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)     # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0, 'data': {'value': 0.011}, 'msg': ''}

## 获取保证金模式
API说明
此接口允许查询持仓保证金模式（逐仓或全仓）和持仓布局（合并或分开持仓），使用户能够有效管理其交易策略。

注意：保证金模式数据可通过Restful和Websocket接口获取。本页是Restful接口的描述。如需了解Websocket接口，请参见 跳转

注意事项
无

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/positions/type

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求5次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
无

响应参数
参数	必填	参数类型	描述
layout	true	String	持仓布局：0：合并持仓（相同方向的持仓将被合并），1：分开持仓（相同方向的持仓将保持分离）
positionModel	true	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
请求示例
以下Python代码展示了如何检查持仓布局和持仓保证金模式。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = { }
 
api_url = "/v1/perpum/positions/type"
 
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)     # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0, 'data': {'layout': 0, 'positionModel': 0}, 'msg': ''}

## 设置保证金模式
API说明
此接口允许用户将其持仓保证金模式配置为逐仓或全仓保证金，并通过选择合并持仓（合并相同方向的新持仓）或分开持仓（保持新持仓分离）来设置持仓布局。

注意：设置保证金模式只能通过 Restful API 可用。

注意事项

要将持仓保证金模式从逐仓更改为全仓或反之，用户必须确保没有未成交订单。否则，接口将返回以下错误：
{'code': 9042, 'msg': 'You have an open order in this mode, please close or cancel it first.'}


要将持仓布局从合并持仓更改为分开持仓或反之，用户必须确保没有未成交订单。否则，接口也将返回上述错误。
认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
POST

接口地址
/v1/perpum/positions/type

频率限制
此接口的频率限制为每用户ID和IP每2秒2个请求。

请求参数
参数	必填	类型	描述
positionModel	true	Integer	持仓保证金模式：0：逐仓保证金，1：全仓保证金
layout	true	String	持仓布局：0：合并持仓（相同方向的持仓将被合并），1：分开持仓（相同方向的持仓将保持分离）
响应参数
参数	类型	描述
data	String	TRANSACTION_SUCCESS
请求示例
以下Python代码展示了如何将持仓布局设置为合并(layout=0)和持仓保证金模式设置为逐仓(positionModel=0)。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
        "layout": "0",   
        "positionModel": 0,
        }
 
api_url = "/v1/perpum/positions/type"
method = "POST"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)     # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应：

{'code': 0, 'data': 'TRANSACTION_SUCCESS', 'msg': ''}

## 启用/禁用万能金
API说明
此接口允许用户激活和停用万能金。万能金可用作合约交易中的保证金，抵消交易费用、亏损和资金成本。

有关万能金的更多详情，请参考 https://coinw.zendesk.com/hc/en-us/articles/23111150445977-Introduction-to-Futures-Mega-Coupon

注意：此功能仅通过Restful API可用。

注意事项
此接口在请求成功时不返回任何信息。收到(code: 0)表示请求成功。
{'code': 0, 'msg': ''}

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
POST

接口地址
/v1/perpum/account/almightyGoldInfo

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求1次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
status	true	String	状态：1：开启，0：关闭
响应参数
此接口在请求成功时不返回任何信息。收到(code: 0)表示请求成功。

{'code': 0, 'msg': ''}

请求示例
以下Python代码展示了如何激活万能金。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {"status": 1,}             
 
api_url = "/v1/perpum/account/almightyGoldInfo"
 
method = "POST"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)    # FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应；收到"code": 0表示成功。

{'code': 0, 'msg': ''}

## 获取用户最大合约规模
API说明
此接口允许用户检索其合约账户中已成交订单的最大可用合约规模。用户必须指定合约，响应将包括做多和做空持仓的最大合约规模。

注意：用户最大合约规模数据只能通过 Restful API 获取。

注意事项
此接口不支持指定合约列表。

如果指定合约没有已成交订单，将返回以下响应：

{'code': 0, 'msg': ''}

认证
这是一个私有接口，需要认证。有关使用Restful API的详细信息，请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

请求方法
GET

接口地址
/v1/perpum/orders/availSize

频率限制
该接口的调用频率限制为：每个 IP 和用户 ID 每2秒最多请求10次。
此外，该接口还受到全局频率限制的约束。
有关"全局速率限制"和"API限频策略"的详细信息，请参阅“频率限制”部分，跳转

请求参数
参数	必填	类型	描述
instrument	true	String	交易品种的基础货币（例如，BTC或btc）。此参数不区分大小写。注意：对于以数字开头的交易品种（例如1000PEPE），大写和小写格式都有效。
响应参数
参数	类型	描述
availBuy	BigDecimal	用户可以平仓的做多方向的最大合约数量
availSell	BigDecimal	用户可以平仓的做空方向的最大合约数量
请求示例
以下Python代码展示了如何检索用户合约账户中"BTC"的最大可用合约规模。

注意：完整代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

params = {
        "instrument" : "BTC",
    }
api_url = "/v1/perpum/orders/availSize"
method = "GET"
response_code, response_data = FuturesRestfulPrivate(params, api_url, method, sec_key, api_key)    # function FuturesRestfulPrivate() is defined in section (Introduction > Authentication & Code Snippet > Futures > Restful Private Interface.)


注意：完整Java代码示例请参考简介 > 认证和代码示例 > 合约 > Restful私有接口。

响应示例
以下是上述Python请求返回的示例响应，显示用户账户中有一个合约可用（做空方向）。
{'code': 0, 'data': {'availBuy': 0, 'availSell': 1}, 'msg': ''}

##