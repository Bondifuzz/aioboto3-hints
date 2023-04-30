from __future__ import annotations

from typing import AsyncIterator, Dict

from aiobotocore.paginate import AioPaginator


class ListMultipartUploads(AioPaginator):
    async def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, ExpectedBucketOwner: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListObjectVersions(AioPaginator):
    async def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, ExpectedBucketOwner: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListObjects(AioPaginator):
    async def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListObjectsV2(AioPaginator):
    async def paginate(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Prefix: str = None, FetchOwner: bool = None, StartAfter: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListParts(AioPaginator):
    async def paginate(self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None, ExpectedBucketOwner: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass

