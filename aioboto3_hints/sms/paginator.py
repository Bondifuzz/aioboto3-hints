from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class GetConnectors(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetReplicationJobs(AioPaginator):
    async def paginate(self, replicationJobId: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetReplicationRuns(AioPaginator):
    async def paginate(self, replicationJobId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetServers(AioPaginator):
    async def paginate(self, vmServerAddressList: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListApps(AioPaginator):
    async def paginate(self, appIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
