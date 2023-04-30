from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListRuleNamesByTarget(AioPaginator):
    async def paginate(self, TargetArn: str, EventBusName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListRules(AioPaginator):
    async def paginate(self, NamePrefix: str = None, EventBusName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListTargetsByRule(AioPaginator):
    async def paginate(self, Rule: str, EventBusName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
