from __future__ import annotations

from datetime import datetime
from typing import IO, Callable, Dict, List, Union

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient


class Client(AioBaseClient):
    async def abort_multipart_upload(self, Bucket: str, Key: str, UploadId: str, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None) -> bool:
        pass

    async def complete_multipart_upload(self, Bucket: str, Key: str, UploadId: str, MultipartUpload: Dict = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def copy(self, CopySource: Dict = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None):
        pass

    async def copy_object(self, Bucket: str, CopySource: Union[str, Dict], Key: str, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None, ExpectedSourceBucketOwner: str = None) -> Dict:
        pass

    async def create_bucket(self, Bucket: str, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ObjectLockEnabledForBucket: bool = None) -> Dict:
        pass

    async def create_multipart_upload(self, Bucket: str, Key: str, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def delete_bucket(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_analytics_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_cors(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_encryption(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_intelligent_tiering_configuration(self, Bucket: str, Id: str) -> None:
        pass

    async def delete_bucket_inventory_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_lifecycle(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_metrics_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_ownership_controls(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_policy(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_replication(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_tagging(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_bucket_website(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_object(self, Bucket: str, Key: str, MFA: str = None, VersionId: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def delete_object_tagging(self, Bucket: str, Key: str, VersionId: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def delete_objects(self, Bucket: str, Delete: Dict, MFA: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def delete_public_access_block(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def download_file(self, Bucket: str = None, Key: str = None, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def download_fileobj(self, Bucket: str = None, Key: str = None, Fileobj: IO = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def generate_presigned_post(self, Bucket: str = None, Key: str = None, Fields: Dict = None, Conditions: List = None, ExpiresIn: int = None) -> Dict:
        pass

    async def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> str:
        pass

    async def get_bucket_accelerate_configuration(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_acl(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_analytics_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_cors(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_encryption(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_intelligent_tiering_configuration(self, Bucket: str, Id: str) -> Dict:
        pass

    async def get_bucket_inventory_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_lifecycle(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_lifecycle_configuration(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_location(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_logging(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_metrics_configuration(self, Bucket: str, Id: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_notification(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_notification_configuration(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_ownership_controls(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_policy(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_policy_status(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_replication(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_request_payment(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_tagging(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_versioning(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_bucket_website(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object_acl(self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object_legal_hold(self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object_lock_configuration(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object_retention(self, Bucket: str, Key: str, VersionId: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_object_tagging(self, Bucket: str, Key: str, VersionId: str = None, ExpectedBucketOwner: str = None, RequestPayer: str = None) -> Dict:
        pass

    async def get_object_torrent(self, Bucket: str, Key: str, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_public_access_block(self, Bucket: str, ExpectedBucketOwner: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def head_bucket(self, Bucket: str, ExpectedBucketOwner: str = None) -> None:
        pass

    async def head_object(self, Bucket: str, Key: str, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_bucket_analytics_configurations(self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_bucket_intelligent_tiering_configurations(self, Bucket: str, ContinuationToken: str = None) -> Dict:
        pass

    async def list_bucket_inventory_configurations(self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_bucket_metrics_configurations(self, Bucket: str, ContinuationToken: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_buckets(self) -> Dict:
        pass

    async def list_multipart_uploads(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, KeyMarker: str = None, MaxUploads: int = None, Prefix: str = None, UploadIdMarker: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_object_versions(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, KeyMarker: str = None, MaxKeys: int = None, Prefix: str = None, VersionIdMarker: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_objects(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, Marker: str = None, MaxKeys: int = None, Prefix: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_objects_v2(self, Bucket: str, Delimiter: str = None, EncodingType: str = None, MaxKeys: int = None, Prefix: str = None, ContinuationToken: str = None, FetchOwner: bool = None, StartAfter: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def list_parts(self, Bucket: str, Key: str, UploadId: str, MaxParts: int = None, PartNumberMarker: int = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_bucket_accelerate_configuration(self, Bucket: str, AccelerateConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_acl(self, Bucket: str, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_analytics_configuration(self, Bucket: str, Id: str, AnalyticsConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_cors(self, Bucket: str, CORSConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_encryption(self, Bucket: str, ServerSideEncryptionConfiguration: Dict, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_intelligent_tiering_configuration(self, Bucket: str, Id: str, IntelligentTieringConfiguration: Dict) -> None:
        pass

    async def put_bucket_inventory_configuration(self, Bucket: str, Id: str, InventoryConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_lifecycle(self, Bucket: str, LifecycleConfiguration: Dict = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_lifecycle_configuration(self, Bucket: str, LifecycleConfiguration: Dict = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_logging(self, Bucket: str, BucketLoggingStatus: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_metrics_configuration(self, Bucket: str, Id: str, MetricsConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_notification(self, Bucket: str, NotificationConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_notification_configuration(self, Bucket: str, NotificationConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_ownership_controls(self, Bucket: str, OwnershipControls: Dict, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_policy(self, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_replication(self, Bucket: str, ReplicationConfiguration: Dict, Token: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_request_payment(self, Bucket: str, RequestPaymentConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_tagging(self, Bucket: str, Tagging: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_versioning(self, Bucket: str, VersioningConfiguration: Dict, MFA: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_bucket_website(self, Bucket: str, WebsiteConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def put_object(self, Bucket: str, Key: str, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_object_acl(self, Bucket: str, Key: str, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, RequestPayer: str = None, VersionId: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_object_legal_hold(self, Bucket: str, Key: str, LegalHold: Dict = None, RequestPayer: str = None, VersionId: str = None, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_object_lock_configuration(self, Bucket: str, ObjectLockConfiguration: Dict = None, RequestPayer: str = None, Token: str = None, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_object_retention(self, Bucket: str, Key: str, Retention: Dict = None, RequestPayer: str = None, VersionId: str = None, BypassGovernanceRetention: bool = None, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def put_object_tagging(self, Bucket: str, Key: str, Tagging: Dict, VersionId: str = None, ContentMD5: str = None, ExpectedBucketOwner: str = None, RequestPayer: str = None) -> Dict:
        pass

    async def put_public_access_block(self, Bucket: str, PublicAccessBlockConfiguration: Dict, ContentMD5: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def restore_object(self, Bucket: str, Key: str, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def select_object_content(self, Bucket: str, Key: str, Expression: str, ExpressionType: str, InputSerialization: Dict, OutputSerialization: Dict, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestProgress: Dict = None, ScanRange: Dict = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def upload_file(self, Filename: str = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def upload_fileobj(self, Fileobj: IO = None, Bucket: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def upload_part(self, Bucket: str, Key: str, PartNumber: int, UploadId: str, Body: Union[bytes, IO] = None, ContentLength: int = None, ContentMD5: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def upload_part_copy(self, Bucket: str, CopySource: Union[str, Dict], Key: str, PartNumber: int, UploadId: str, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, CopySourceRange: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None, ExpectedSourceBucketOwner: str = None) -> Dict:
        pass

    async def write_get_object_response(self, RequestRoute: str, RequestToken: str, Body: Union[bytes, IO] = None, StatusCode: int = None, ErrorCode: str = None, ErrorMessage: str = None, AcceptRanges: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentRange: str = None, ContentType: str = None, DeleteMarker: bool = None, ETag: str = None, Expires: datetime = None, Expiration: str = None, LastModified: datetime = None, MissingMeta: int = None, Metadata: Dict = None, ObjectLockMode: str = None, ObjectLockLegalHoldStatus: str = None, ObjectLockRetainUntilDate: datetime = None, PartsCount: int = None, ReplicationStatus: str = None, RequestCharged: str = None, Restore: str = None, ServerSideEncryption: str = None, SSECustomerAlgorithm: str = None, SSEKMSKeyId: str = None, SSECustomerKeyMD5: str = None, StorageClass: str = None, TagCount: int = None, VersionId: str = None, BucketKeyEnabled: bool = None) -> None:
        pass

