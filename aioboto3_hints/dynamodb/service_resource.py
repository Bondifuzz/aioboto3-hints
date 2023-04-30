from datetime import datetime
from typing import Dict, List

from aioboto3.resources import AIOBoto3ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(AIOBoto3ServiceResource):
    tables: 'tables'

    def Table(self, name: str = None) -> 'Table':
        pass

    async def batch_get_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None) -> Dict:
        pass

    async def batch_write_item(self, RequestItems: Dict, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None) -> Dict:
        pass

    async def create_table(self, AttributeDefinitions: List, TableName: str, KeySchema: List, LocalSecondaryIndexes: List = None, GlobalSecondaryIndexes: List = None, BillingMode: str = None, ProvisionedThroughput: Dict = None, StreamSpecification: Dict = None, SSESpecification: Dict = None, Tags: List = None) -> 'Table':
        pass

    async def get_available_subresources(self) -> List[str]:
        pass


class Table(AIOBoto3ServiceResource):
    attribute_definitions: List
    table_name: str
    key_schema: List
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    billing_mode_summary: Dict
    local_secondary_indexes: List
    global_secondary_indexes: List
    stream_specification: Dict
    latest_stream_label: str
    latest_stream_arn: str
    restore_summary: Dict
    sse_description: Dict
    name: str

    async def batch_writer(self, overwrite_by_pkeys: List[str] = None):
        pass

    async def delete(self) -> Dict:
        pass

    async def delete_item(self, Key: Dict, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def get_item(self, Key: Dict, AttributesToGet: List = None, ConsistentRead: bool = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, ExpressionAttributeNames: Dict = None) -> Dict:
        pass

    async def load(self):
        pass

    async def put_item(self, Item: Dict, Expected: Dict = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, ConditionalOperator: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    async def query(self, IndexName: str = None, Select: str = None, AttributesToGet: List = None, Limit: int = None, ConsistentRead: bool = None, KeyConditions: Dict = None, QueryFilter: Dict = None, ConditionalOperator: str = None, ScanIndexForward: bool = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, ProjectionExpression: str = None, FilterExpression: str = None, KeyConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    async def reload(self):
        pass

    async def scan(self, IndexName: str = None, AttributesToGet: List = None, Limit: int = None, Select: str = None, ScanFilter: Dict = None, ConditionalOperator: str = None, ExclusiveStartKey: Dict = None, ReturnConsumedCapacity: str = None, TotalSegments: int = None, Segment: int = None, ProjectionExpression: str = None, FilterExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None, ConsistentRead: bool = None) -> Dict:
        pass

    async def update(self, AttributeDefinitions: List = None, BillingMode: str = None, ProvisionedThroughput: Dict = None, GlobalSecondaryIndexUpdates: List = None, StreamSpecification: Dict = None, SSESpecification: Dict = None) -> 'Table':
        pass

    async def update_item(self, Key: Dict, AttributeUpdates: Dict = None, Expected: Dict = None, ConditionalOperator: str = None, ReturnValues: str = None, ReturnConsumedCapacity: str = None, ReturnItemCollectionMetrics: str = None, UpdateExpression: str = None, ConditionExpression: str = None, ExpressionAttributeNames: Dict = None, ExpressionAttributeValues: Dict = None) -> Dict:
        pass

    async def wait_until_exists(self):
        pass

    async def wait_until_not_exists(self):
        pass


class tables(ResourceCollection):
    
    @classmethod
    async def all(cls) -> List['Table']:
        pass

    
    @classmethod
    async def filter(cls, ExclusiveStartTableName: str = None, Limit: int = None) -> List['Table']:
        pass

    
    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    async def limit(cls, count: int = None) -> List['Table']:
        pass

    
    @classmethod
    async def page_size(cls, count: int = None) -> List['Table']:
        pass

    
    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass
