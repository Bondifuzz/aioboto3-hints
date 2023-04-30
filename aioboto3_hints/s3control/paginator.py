from __future__ import annotations

from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListAccessPointsForObjectLambda(AioPaginator):
    async def paginate(self, AccountId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass

