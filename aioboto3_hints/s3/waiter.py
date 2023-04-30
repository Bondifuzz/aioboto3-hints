from __future__ import annotations

from datetime import datetime
from typing import Dict

from aiobotocore.waiter import AIOWaiter


class BucketExists(AIOWaiter):
    async def wait(self, Bucket: str, ExpectedBucketOwner: str = None, WaiterConfig: Dict = None) -> None:
        pass



class BucketNotExists(AIOWaiter):
    async def wait(self, Bucket: str, ExpectedBucketOwner: str = None, WaiterConfig: Dict = None) -> None:
        pass



class ObjectExists(AIOWaiter):
    async def wait(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None, WaiterConfig: Dict = None) -> None:
        pass



class ObjectNotExists(AIOWaiter):
    async def wait(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None, WaiterConfig: Dict = None) -> None:
        pass

