from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListAliases(AioPaginator):
    async def paginate(self, KeyId: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListGrants(AioPaginator):
    async def paginate(self, KeyId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListKeyPolicies(AioPaginator):
    async def paginate(self, KeyId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListKeys(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
