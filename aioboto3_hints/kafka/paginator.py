from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListClusterOperations(AioPaginator):
    async def paginate(self, ClusterArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListClusters(AioPaginator):
    async def paginate(self, ClusterNameFilter: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListConfigurationRevisions(AioPaginator):
    async def paginate(self, Arn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListConfigurations(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListNodes(AioPaginator):
    async def paginate(self, ClusterArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
