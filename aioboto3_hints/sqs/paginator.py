from __future__ import annotations

from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListDeadLetterSourceQueues(AioPaginator):
    async def paginate(self, QueueUrl: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListQueues(AioPaginator):
    async def paginate(self, QueueNamePrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass

