from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class DescribeDirectories(AioPaginator):
    async def paginate(self, DirectoryIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeDomainControllers(AioPaginator):
    async def paginate(self, DirectoryId: str, DomainControllerIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSharedDirectories(AioPaginator):
    async def paginate(self, OwnerDirectoryId: str, SharedDirectoryIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSnapshots(AioPaginator):
    async def paginate(self, DirectoryId: str = None, SnapshotIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTrusts(AioPaginator):
    async def paginate(self, DirectoryId: str = None, TrustIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListIpRoutes(AioPaginator):
    async def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListLogSubscriptions(AioPaginator):
    async def paginate(self, DirectoryId: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListSchemaExtensions(AioPaginator):
    async def paginate(self, DirectoryId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListTagsForResource(AioPaginator):
    async def paginate(self, ResourceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
