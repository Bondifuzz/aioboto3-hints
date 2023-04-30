from __future__ import annotations

from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def add_permission(self, QueueUrl: str, Label: str, AWSAccountIds: List, Actions: List) -> None:
        pass

    async def can_paginate(self, operation_name: str = None) -> bool:
        pass

    async def change_message_visibility(self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int) -> None:
        pass

    async def change_message_visibility_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    async def create_queue(self, QueueName: str, Attributes: Dict = None, tags: Dict = None) -> Dict:
        pass

    async def delete_message(self, QueueUrl: str, ReceiptHandle: str) -> None:
        pass

    async def delete_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    async def delete_queue(self, QueueUrl: str) -> None:
        pass

    async def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> str:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_queue_attributes(self, QueueUrl: str, AttributeNames: List = None) -> Dict:
        pass

    async def get_queue_url(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_dead_letter_source_queues(self, QueueUrl: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_queue_tags(self, QueueUrl: str) -> Dict:
        pass

    async def list_queues(self, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def purge_queue(self, QueueUrl: str) -> None:
        pass

    async def receive_message(self, QueueUrl: str, AttributeNames: List = None, MessageAttributeNames: List = None, MaxNumberOfMessages: int = None, VisibilityTimeout: int = None, WaitTimeSeconds: int = None, ReceiveRequestAttemptId: str = None) -> Dict:
        pass

    async def remove_permission(self, QueueUrl: str, Label: str) -> None:
        pass

    async def send_message(self, QueueUrl: str, MessageBody: str, DelaySeconds: int = None, MessageAttributes: Dict = None, MessageSystemAttributes: Dict = None, MessageDeduplicationId: str = None, MessageGroupId: str = None) -> Dict:
        pass

    async def send_message_batch(self, QueueUrl: str, Entries: List) -> Dict:
        pass

    async def set_queue_attributes(self, QueueUrl: str, Attributes: Dict) -> None:
        pass

    async def tag_queue(self, QueueUrl: str, Tags: Dict) -> None:
        pass

    async def untag_queue(self, QueueUrl: str, TagKeys: List) -> None:
        pass

