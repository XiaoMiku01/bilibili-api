"""
bilibili_api.exceptions.CredentialNoBuvid3Exception

Credential 类未提供 live_buvid 时的异常。
"""

from .ApiException import ApiException


class CredentialNoLiveBuvidException(ApiException):
    """
    Credential 类未提供 live_buvid 时的异常。
    """

    def __init__(self):
        super().__init__()
        self.msg = "Credential 类未提供 live_buvid。"
