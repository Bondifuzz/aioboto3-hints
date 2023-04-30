from __future__ import annotations

from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListBrokers(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass

