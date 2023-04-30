from __future__ import annotations

from typing import Dict, List, Optional

from aioboto3.resources.base import AIOBoto3ServiceResource
from boto3.resources.collection import ResourceCollection


from boto3.resources.base import ResourceMeta as _ResourceMeta
from .client import Client

class ResourceMeta(_ResourceMeta):
    client: Optional[Client]

class ServiceResource(AIOBoto3ServiceResource):
    meta: Optional[ResourceMeta]

    queues: queues

    async def Message(self, queue_url: str = None, receipt_handle: str = None) -> Message:
        pass

    async def Queue(self, url: str = None) -> Queue:
        pass

    async def create_queue(self, QueueName: str, Attributes: Dict = None, tags: Dict = None) -> Queue:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def get_queue_by_name(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> Queue:
        pass



class Message(AIOBoto3ServiceResource):
    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict
    md5_of_message_attributes: str
    message_attributes: Dict
    queue_url: str
    receipt_handle: str

    async def Queue(self) -> Queue:
        pass

    async def change_visibility(self, VisibilityTimeout: int) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class Queue(AIOBoto3ServiceResource):
    attributes: Dict
    url: str
    dead_letter_source_queues: dead_letter_source_queues

    async def Message(self, receipt_handle: str = None) -> Message:
        pass

    async def add_permission(self, Label: str, AWSAccountIds: List, Actions: List) -> None:
        pass

    async def change_message_visibility_batch(self, Entries: List) -> Dict:
        pass

    async def delete(self) -> None:
        pass

    async def delete_messages(self, Entries: List) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def purge(self) -> None:
        pass

    async def receive_messages(self, AttributeNames: List = None, MessageAttributeNames: List = None, MaxNumberOfMessages: int = None, VisibilityTimeout: int = None, WaitTimeSeconds: int = None, ReceiveRequestAttemptId: str = None) -> List[Message]:
        pass

    async def reload(self) -> None:
        pass

    async def remove_permission(self, Label: str) -> None:
        pass

    async def send_message(self, MessageBody: str, DelaySeconds: int = None, MessageAttributes: Dict = None, MessageSystemAttributes: Dict = None, MessageDeduplicationId: str = None, MessageGroupId: str = None) -> Dict:
        pass

    async def send_messages(self, Entries: List) -> Dict:
        pass

    async def set_attributes(self, Attributes: Dict) -> None:
        pass



class queues(ResourceCollection):
    @classmethod
    async def all(cls) -> List[Queue]:
        pass

    @classmethod
    async def filter(cls, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None) -> List[Queue]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[Queue]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[Queue]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass

