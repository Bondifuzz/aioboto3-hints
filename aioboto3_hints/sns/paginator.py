from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListEndpointsByPlatformApplication(AioPaginator):
    async def paginate(self, PlatformApplicationArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListPhoneNumbersOptedOut(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListPlatformApplications(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListSubscriptions(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListSubscriptionsByTopic(AioPaginator):
    async def paginate(self, TopicArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListTopics(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
