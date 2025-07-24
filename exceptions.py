"""
CoinW API 異常處理
官方沒有寫
定義了所有可能的API錯誤類型，便於錯誤處理和調試
"""


class CoinWAPIError(Exception):
    """CoinW API 基礎異常類別"""
    
    def __init__(self, message, code=None, response=None):
        self.message = message
        self.code = code
        self.response = response
        super().__init__(self.message)
    
    def __str__(self):
        if self.code:
            return f"[{self.code}] {self.message}"
        return self.message


class InvalidCredentialsError(CoinWAPIError):
    """無效的API憑證"""
    pass


class RateLimitError(CoinWAPIError):
    """API請求頻率限制"""
    pass


class InsufficientBalanceError(CoinWAPIError):
    """餘額不足"""
    pass


class OrderNotFoundError(CoinWAPIError):
    """訂單不存在"""
    pass


class InvalidParameterError(CoinWAPIError):
    """參數錯誤"""
    pass


class NetworkError(CoinWAPIError):
    """網路連接錯誤"""
    pass


class ServerError(CoinWAPIError):
    """伺服器錯誤"""
    pass


class SignatureError(CoinWAPIError):
    """簽名錯誤"""
    pass


def handle_api_error(response_data, status_code):
    """
    根據API響應處理錯誤
    
    Args:
        response_data: API響應數據
        status_code: HTTP狀態碼
    
    Raises:
        相應的異常類型
    """
    if status_code == 401:
        raise InvalidCredentialsError("API憑證無效或已過期")
    
    if status_code == 429:
        raise RateLimitError("API請求頻率超出限制")
    
    if status_code >= 500:
        raise ServerError(f"伺服器錯誤: {status_code}")
    
    # 處理業務邏輯錯誤
    if isinstance(response_data, dict):
        code = response_data.get('code')
        message = response_data.get('message', '未知錯誤')
        
        error_mapping = {
            'INSUFFICIENT_BALANCE': InsufficientBalanceError,
            'ORDER_NOT_FOUND': OrderNotFoundError,
            'INVALID_PARAMETER': InvalidParameterError,
            'SIGNATURE_ERROR': SignatureError,
        }
        
        error_class = error_mapping.get(code, CoinWAPIError)
        raise error_class(message, code=code, response=response_data)
    
    # 預設錯誤
    raise CoinWAPIError(f"API請求失敗: {status_code}") 