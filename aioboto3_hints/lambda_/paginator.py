from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListAliases(AioPaginator):
    async def paginate(self, FunctionName: str, FunctionVersion: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListEventSourceMappings(AioPaginator):
    async def paginate(self, EventSourceArn: str = None, FunctionName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListFunctions(AioPaginator):
    async def paginate(self, MasterRegion: str = None, FunctionVersion: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListLayerVersions(AioPaginator):
    async def paginate(self, LayerName: str, CompatibleRuntime: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListLayers(AioPaginator):
    async def paginate(self, CompatibleRuntime: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListVersionsByFunction(AioPaginator):
    async def paginate(self, FunctionName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
