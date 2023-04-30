from aioboto3_hints.sqs.client import Client
from aioboto3_hints.sqs.service_resource import (Message, Queue,
                                                 ServiceResource, queues)

__all__ = (
    'Client',
    'ServiceResource',
    'Message',
    'Queue',
    'queues',
)
