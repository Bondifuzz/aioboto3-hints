from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def assume_role(self, RoleArn: str, RoleSessionName: str, PolicyArns: List = None, Policy: str = None, DurationSeconds: int = None, ExternalId: str = None, SerialNumber: str = None, TokenCode: str = None) -> Dict:
        pass

    async def assume_role_with_saml(self, RoleArn: str, PrincipalArn: str, SAMLAssertion: str, PolicyArns: List = None, Policy: str = None, DurationSeconds: int = None) -> Dict:
        pass

    async def assume_role_with_web_identity(self, RoleArn: str, RoleSessionName: str, WebIdentityToken: str, ProviderId: str = None, PolicyArns: List = None, Policy: str = None, DurationSeconds: int = None) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def decode_authorization_message(self, EncodedMessage: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_access_key_info(self, AccessKeyId: str) -> Dict:
        pass

    async def get_caller_identity(self) -> Dict:
        pass

    async def get_federation_token(self, Name: str, Policy: str = None, PolicyArns: List = None, DurationSeconds: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_session_token(self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass
