from datetime import datetime
from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class ListBackups(AioPaginator):
    async def paginate(self, TableName: str = None, TimeRangeLowerBound: datetime = None, TimeRangeUpperBound: datetime = None, BackupType: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListTables(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListTagsOfResource(AioPaginator):
    async def paginate(self, ResourceArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class Query(AioPaginator):
    async def paginate(self, TableName: str, IndexName: str = None, Select: str = None, AttributesToGet: List = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class Scan(AioPaginator):
    async def paginate(self, TableName: str, IndexName: str = None, AttributesToGet: List = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
