from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def associate_kms_key(self, logGroupName: str, kmsKeyId: str):
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def cancel_export_task(self, taskId: str):
        pass

    async def create_export_task(self, logGroupName: str, fromTime: int, to: int, destination: str, taskName: str = None, logStreamNamePrefix: str = None, destinationPrefix: str = None) -> Dict:
        pass

    async def create_log_group(self, logGroupName: str, kmsKeyId: str = None, tags: Dict = None):
        pass

    async def create_log_stream(self, logGroupName: str, logStreamName: str):
        pass

    async def delete_destination(self, destinationName: str):
        pass

    async def delete_log_group(self, logGroupName: str):
        pass

    async def delete_log_stream(self, logGroupName: str, logStreamName: str):
        pass

    async def delete_metric_filter(self, logGroupName: str, filterName: str):
        pass

    async def delete_resource_policy(self, policyName: str = None):
        pass

    async def delete_retention_policy(self, logGroupName: str):
        pass

    async def delete_subscription_filter(self, logGroupName: str, filterName: str):
        pass

    async def describe_destinations(self, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def describe_export_tasks(self, taskId: str = None, statusCode: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def describe_log_groups(self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def describe_log_streams(self, logGroupName: str, logStreamNamePrefix: str = None, orderBy: str = None, descending: bool = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def describe_metric_filters(self, logGroupName: str = None, filterNamePrefix: str = None, nextToken: str = None, limit: int = None, metricName: str = None, metricNamespace: str = None) -> Dict:
        pass

    async def describe_queries(self, logGroupName: str = None, status: str = None, maxResults: int = None, nextToken: str = None) -> Dict:
        pass

    async def describe_resource_policies(self, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def describe_subscription_filters(self, logGroupName: str, filterNamePrefix: str = None, nextToken: str = None, limit: int = None) -> Dict:
        pass

    async def disassociate_kms_key(self, logGroupName: str):
        pass

    async def filter_log_events(self, logGroupName: str, logStreamNames: List = None, logStreamNamePrefix: str = None, startTime: int = None, endTime: int = None, filterPattern: str = None, nextToken: str = None, limit: int = None, interleaved: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_log_events(self, logGroupName: str, logStreamName: str, startTime: int = None, endTime: int = None, nextToken: str = None, limit: int = None, startFromHead: bool = None) -> Dict:
        pass

    async def get_log_group_fields(self, logGroupName: str, time: int = None) -> Dict:
        pass

    async def get_log_record(self, logRecordPointer: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_query_results(self, queryId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_tags_log_group(self, logGroupName: str) -> Dict:
        pass

    async def put_destination(self, destinationName: str, targetArn: str, roleArn: str) -> Dict:
        pass

    async def put_destination_policy(self, destinationName: str, accessPolicy: str):
        pass

    async def put_log_events(self, logGroupName: str, logStreamName: str, logEvents: List, sequenceToken: str = None) -> Dict:
        pass

    async def put_metric_filter(self, logGroupName: str, filterName: str, filterPattern: str, metricTransformations: List):
        pass

    async def put_resource_policy(self, policyName: str = None, policyDocument: str = None) -> Dict:
        pass

    async def put_retention_policy(self, logGroupName: str, retentionInDays: int):
        pass

    async def put_subscription_filter(self, logGroupName: str, filterName: str, filterPattern: str, destinationArn: str, roleArn: str = None, distribution: str = None):
        pass

    async def start_query(self, startTime: int, endTime: int, queryString: str, logGroupName: str = None, logGroupNames: List = None, limit: int = None) -> Dict:
        pass

    async def stop_query(self, queryId: str) -> Dict:
        pass

    async def tag_log_group(self, logGroupName: str, tags: Dict):
        pass

    async def test_metric_filter(self, filterPattern: str, logEventMessages: List) -> Dict:
        pass

    async def untag_log_group(self, logGroupName: str, tags: List):
        pass
