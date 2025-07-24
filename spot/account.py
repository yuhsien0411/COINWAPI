"""
CoinW 現貨帳戶模組

專門處理現貨帳戶 API
端點格式: /api/v1/private?command=...
認證方式: MD5 簽名
"""

from typing import Dict, Any, Optional
from .http_manager import SpotHTTPManager


class SpotAccount:
    """現貨帳戶接口"""
    
    def __init__(
        self,
        api_key: str,
        secret_key: str,
        base_url: str = "https://api.coinw.com",
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        初始化現貨帳戶接口
        
        Args:
            api_key: API金鑰
            secret_key: 密鑰
            base_url: API基礎URL
            timeout: 請求超時時間
            max_retries: 最大重試次數
        """
        self._http_manager = SpotHTTPManager(
            api_key=api_key,
            secret_key=secret_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries
        )
    
    def get_balance(self) -> Dict[str, Any]:
        """
        獲取現貨帳戶餘額
        
        Returns:
            帳戶餘額信息
        """
        data = {'command': 'returnBalances'}
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_full_balance(self) -> Dict[str, Any]:
        """
        獲取完整現貨帳戶餘額（包含凍結餘額）
        
        Returns:
            完整帳戶餘額信息
        """
        data = {'command': 'returnCompleteBalances'}
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_deposit_address(self, symbol_id: str, chain: str) -> Dict[str, Any]:
        """
        獲取充值地址
        
        Args:
            symbol_id: 幣種ID，如 BTC 的 ID 是 "50"
            chain: 區塊鏈名稱，如 "BTC"
            
        Returns:
            充值地址信息
        """
        data = {
            'command': 'returnDepositAddresses',
            'symbolId': symbol_id,  # 修正：使用 symbolId 而不是 currency
            'chain': chain
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def get_deposit_history(
        self, 
        symbol: str, 
        deposit_number: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        獲取充值和提現歷史
        
        Args:
            symbol: 交易品種的基礎貨幣，如 "BTC"
            deposit_number: 唯一ID（可選）
            
        Returns:
            充值和提現歷史記錄
        """
        data = {
            'command': 'returnDepositsWithdrawals',
            'symbol': symbol  # 修正：使用 symbol 而不是 currency
        }
        
        if deposit_number:
            data['depositNumber'] = deposit_number
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def withdraw(
        self, 
        currency: str, 
        amount: float, 
        address: str, 
        chain: str,
        memo: str = "None",
        withdraw_type: str = "ordinary_withdraw",
        inner_to_type: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        發起提現
        
        Args:
            currency: 幣種名稱
            amount: 提現數量
            address: 提現地址（普通提現為區塊鏈地址，內部轉賬為用戶ID/郵箱/手機號）
            chain: 區塊鏈名稱，如 "BTC", "ERC20", "TRC20", "BSC"
            memo: 備註，默認 "None"
            withdraw_type: 提現類型，"ordinary_withdraw" 或 "internal_transfer"
            inner_to_type: 內部轉賬地址類型（1=用戶ID, 2=手機號, 3=郵箱）
            
        Returns:
            提現結果
        """
        data = {
            'command': 'doWithdraw',
            'currency': currency,
            'amount': str(amount),
            'address': address,
            'chain': chain,
            'memo': memo,
            'type': withdraw_type
        }
        
        # 如果是內部轉賬，需要設置 innerToType
        if withdraw_type == "internal_transfer" and inner_to_type:
            data['innerToType'] = inner_to_type
        
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def cancel_withdraw(self, withdraw_id: str) -> Dict[str, Any]:
        """
        取消提現
        
        Args:
            withdraw_id: 提現申請ID
            
        Returns:
            取消結果
        """
        data = {
            'command': 'cancelWithdraw',
            'id': withdraw_id
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def transfer(
        self, 
        account_type: str, 
        target_account_type: str, 
        biz_type: str,
        coin_code: str, 
        amount: float
    ) -> Dict[str, Any]:
        """
        資產轉賬
        
        Args:
            account_type: 源帳戶類型（WEALTH=資金帳戶, SPOT=現貨帳戶）
            target_account_type: 目標帳戶類型（WEALTH=資金帳戶, SPOT=現貨帳戶）
            biz_type: 轉賬方向（WEALTH_TO_SPOT 或 SPOT_TO_WEALTH）
            coin_code: 幣種代碼，如 "BTC"
            amount: 轉賬數量
            
        Returns:
            轉賬結果
        """
        data = {
            'command': 'spotWealthTransfer',
            'accountType': account_type,
            'targetAccountType': target_account_type,
            'bizType': biz_type,  # 添加 bizType 參數
            'coinCode': coin_code,
            'amount': amount
        }
        return self._http_manager.spot_restful_private("/api/v1/private", "POST", data)
    
    def internal_transfer(
        self, 
        currency: str, 
        amount: float, 
        address: str,
        chain: str = "BTC",
        inner_to_type: int = 3  # 3=EMAIL
    ) -> Dict[str, Any]:
        """
        內部轉賬（用戶間轉賬）
        
        Args:
            currency: 幣種
            amount: 數量
            address: 目標用戶郵箱或ID
            chain: 區塊鏈名稱
            inner_to_type: 轉賬類型（1=用戶ID, 2=手機號, 3=郵箱）
            
        Returns:
            轉賬結果
        """
        return self.withdraw(
            currency=currency,
            amount=amount,
            address=address,
            chain=chain,
            memo="None",
            withdraw_type="internal_transfer",
            inner_to_type=inner_to_type
        ) 