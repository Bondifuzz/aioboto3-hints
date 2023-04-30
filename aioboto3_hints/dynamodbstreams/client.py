from typing import Dict

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def describe_stream(self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_records(self, ShardIterator: str, Limit: int = None) -> Dict:
        pass

    async def get_shard_iterator(self, StreamArn: str, ShardId: str, ShardIteratorType: str, SequenceNumber: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_streams(self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None) -> Dict:
        pass
