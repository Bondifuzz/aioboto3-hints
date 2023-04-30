from __future__ import annotations

from datetime import datetime
from typing import IO, Callable, Dict, List, Union, Optional

from aioboto3.resources.base import AIOBoto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient


from boto3.resources.base import ResourceMeta as _ResourceMeta
from .client import Client

class ResourceMeta(_ResourceMeta):
    client: Optional[Client]

class ServiceResource(AIOBoto3ServiceResource):
    meta: Optional[ResourceMeta]

    buckets: buckets

    async def Bucket(self, name: str = None) -> Bucket:
        pass

    async def BucketAcl(self, bucket_name: str = None) -> BucketAcl:
        pass

    async def BucketCors(self, bucket_name: str = None) -> BucketCors:
        pass

    async def BucketLifecycle(self, bucket_name: str = None) -> BucketLifecycle:
        pass

    async def BucketLifecycleConfiguration(self, bucket_name: str = None) -> BucketLifecycleConfiguration:
        pass

    async def BucketLogging(self, bucket_name: str = None) -> BucketLogging:
        pass

    async def BucketNotification(self, bucket_name: str = None) -> BucketNotification:
        pass

    async def BucketPolicy(self, bucket_name: str = None) -> BucketPolicy:
        pass

    async def BucketRequestPayment(self, bucket_name: str = None) -> BucketRequestPayment:
        pass

    async def BucketTagging(self, bucket_name: str = None) -> BucketTagging:
        pass

    async def BucketVersioning(self, bucket_name: str = None) -> BucketVersioning:
        pass

    async def BucketWebsite(self, bucket_name: str = None) -> BucketWebsite:
        pass

    async def MultipartUpload(self, bucket_name: str = None, object_key: str = None, id: str = None) -> MultipartUpload:
        pass

    async def MultipartUploadPart(self, bucket_name: str = None, object_key: str = None, multipart_upload_id: str = None, part_number: str = None) -> MultipartUploadPart:
        pass

    async def Object(self, bucket_name: str = None, key: str = None) -> Object:
        pass

    async def ObjectAcl(self, bucket_name: str = None, object_key: str = None) -> ObjectAcl:
        pass

    async def ObjectSummary(self, bucket_name: str = None, key: str = None) -> ObjectSummary:
        pass

    async def ObjectVersion(self, bucket_name: str = None, object_key: str = None, id: str = None) -> ObjectVersion:
        pass

    async def create_bucket(self, Bucket: str, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ObjectLockEnabledForBucket: bool = None) -> Bucket:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class Bucket(AIOBoto3ServiceResource):
    creation_date: datetime
    name: str
    multipart_uploads: multipart_uploads
    object_versions: object_versions
    objects: objects

    async def Acl(self) -> BucketAcl:
        pass

    async def Cors(self) -> BucketCors:
        pass

    async def Lifecycle(self) -> BucketLifecycle:
        pass

    async def LifecycleConfiguration(self) -> BucketLifecycleConfiguration:
        pass

    async def Logging(self) -> BucketLogging:
        pass

    async def Notification(self) -> BucketNotification:
        pass

    async def Object(self, key: str = None) -> Object:
        pass

    async def Policy(self) -> BucketPolicy:
        pass

    async def RequestPayment(self) -> BucketRequestPayment:
        pass

    async def Tagging(self) -> BucketTagging:
        pass

    async def Versioning(self) -> BucketVersioning:
        pass

    async def Website(self) -> BucketWebsite:
        pass

    async def copy(self, CopySource: Dict = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None):
        pass

    async def create(self, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ObjectLockEnabledForBucket: bool = None) -> Dict:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def delete_objects(self, Delete: Dict, MFA: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def download_file(self, Key: str = None, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def download_fileobj(self, Fileobj: IO = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self):
        pass

    async def put_object(self, Key: str, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> Object:
        pass

    async def upload_file(self, Filename: str = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def upload_fileobj(self, Fileobj: IO = None, Key: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def wait_until_exists(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def wait_until_not_exists(self, ExpectedBucketOwner: str = None) -> None:
        pass



class BucketAcl(AIOBoto3ServiceResource):
    owner: Dict
    grants: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketCors(AIOBoto3ServiceResource):
    cors_rules: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, CORSConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketLifecycle(AIOBoto3ServiceResource):
    rules: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, LifecycleConfiguration: Dict = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketLifecycleConfiguration(AIOBoto3ServiceResource):
    rules: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, LifecycleConfiguration: Dict = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketLogging(AIOBoto3ServiceResource):
    logging_enabled: Dict
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, BucketLoggingStatus: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketNotification(AIOBoto3ServiceResource):
    topic_configurations: List
    queue_configurations: List
    lambda_function_configurations: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, NotificationConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketPolicy(AIOBoto3ServiceResource):
    policy: str
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketRequestPayment(AIOBoto3ServiceResource):
    payer: str
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, RequestPaymentConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketTagging(AIOBoto3ServiceResource):
    tag_set: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, Tagging: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class BucketVersioning(AIOBoto3ServiceResource):
    status: str
    mfa_delete: str
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def enable(self, MFA: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, VersioningConfiguration: Dict, MFA: str = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def suspend(self, MFA: str = None, ExpectedBucketOwner: str = None) -> None:
        pass



class BucketWebsite(AIOBoto3ServiceResource):
    redirect_all_requests_to: Dict
    index_document: Dict
    error_document: Dict
    routing_rules: List
    bucket_name: str

    async def Bucket(self) -> Bucket:
        pass

    async def delete(self, ExpectedBucketOwner: str = None) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, WebsiteConfiguration: Dict, ExpectedBucketOwner: str = None) -> None:
        pass

    async def reload(self) -> None:
        pass



class MultipartUpload(AIOBoto3ServiceResource):
    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict
    initiator: Dict
    bucket_name: str
    object_key: str
    id: str
    parts: parts

    async def Object(self) -> Object:
        pass

    async def Part(self, part_number: str = None) -> MultipartUploadPart:
        pass

    async def abort(self, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def complete(self, MultipartUpload: Dict = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Object:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class MultipartUploadPart(AIOBoto3ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    async def MultipartUpload(self) -> MultipartUpload:
        pass

    async def copy_from(self, CopySource: Union[str, Dict], CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, CopySourceRange: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None, ExpectedSourceBucketOwner: str = None) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def upload(self, Body: Union[bytes, IO] = None, ContentLength: int = None, ContentMD5: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass



class Object(AIOBoto3ServiceResource):
    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    archive_status: str
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    bucket_key_enabled: bool
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: str
    bucket_name: str
    key: str

    async def Acl(self) -> ObjectAcl:
        pass

    async def Bucket(self) -> Bucket:
        pass

    async def MultipartUpload(self, id: str = None) -> MultipartUpload:
        pass

    async def Version(self, id: str = None) -> ObjectVersion:
        pass

    async def copy(self, CopySource: Dict = None, ExtraArgs: Dict = None, Callback: Callable = None, SourceClient: BaseClient = None, Config: TransferConfig = None):
        pass

    async def copy_from(self, CopySource: Union[str, Dict], ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None, ExpectedSourceBucketOwner: str = None) -> Dict:
        pass

    async def delete(self, MFA: str = None, VersionId: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def download_file(self, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def download_fileobj(self, Fileobj: IO = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def initiate_multipart_upload(self, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> MultipartUpload:
        pass

    async def load(self) -> None:
        pass

    async def put(self, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def reload(self) -> None:
        pass

    async def restore_object(self, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def upload_file(self, Filename: str = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def upload_fileobj(self, Fileobj: IO = None, ExtraArgs: Dict = None, Callback: Callable = None, Config: TransferConfig = None):
        pass

    async def wait_until_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def wait_until_not_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> None:
        pass



class ObjectAcl(AIOBoto3ServiceResource):
    owner: Dict
    grants: List
    request_charged: str
    bucket_name: str
    object_key: str

    async def Object(self) -> Object:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, ACL: str = None, AccessControlPolicy: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, RequestPayer: str = None, VersionId: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def reload(self) -> None:
        pass



class ObjectSummary(AIOBoto3ServiceResource):
    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict
    bucket_name: str
    key: str

    async def Acl(self) -> ObjectAcl:
        pass

    async def Bucket(self) -> Bucket:
        pass

    async def MultipartUpload(self, id: str = None) -> MultipartUpload:
        pass

    async def Object(self) -> Object:
        pass

    async def Version(self, id: str = None) -> ObjectVersion:
        pass

    async def copy_from(self, CopySource: Union[str, Dict], ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, CopySourceIfMatch: str = None, CopySourceIfModifiedSince: datetime = None, CopySourceIfNoneMatch: str = None, CopySourceIfUnmodifiedSince: datetime = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, MetadataDirective: str = None, TaggingDirective: str = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, CopySourceSSECustomerAlgorithm: str = None, CopySourceSSECustomerKey: str = None, CopySourceSSECustomerKeyMD5: str = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None, ExpectedSourceBucketOwner: str = None) -> Dict:
        pass

    async def delete(self, MFA: str = None, VersionId: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def initiate_multipart_upload(self, ACL: str = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> MultipartUpload:
        pass

    async def load(self):
        pass

    async def put(self, ACL: str = None, Body: Union[bytes, IO] = None, CacheControl: str = None, ContentDisposition: str = None, ContentEncoding: str = None, ContentLanguage: str = None, ContentLength: int = None, ContentMD5: str = None, ContentType: str = None, Expires: datetime = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWriteACP: str = None, Metadata: Dict = None, ServerSideEncryption: str = None, StorageClass: str = None, WebsiteRedirectLocation: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, SSEKMSKeyId: str = None, SSEKMSEncryptionContext: str = None, BucketKeyEnabled: bool = None, RequestPayer: str = None, Tagging: str = None, ObjectLockMode: str = None, ObjectLockRetainUntilDate: datetime = None, ObjectLockLegalHoldStatus: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def restore_object(self, VersionId: str = None, RestoreRequest: Dict = None, RequestPayer: str = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def wait_until_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> None:
        pass

    async def wait_until_not_exists(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, VersionId: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> None:
        pass



class ObjectVersion(AIOBoto3ServiceResource):
    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict
    bucket_name: str
    object_key: str
    id: str

    async def Object(self) -> Object:
        pass

    async def delete(self, MFA: str = None, RequestPayer: str = None, BypassGovernanceRetention: bool = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, ResponseCacheControl: str = None, ResponseContentDisposition: str = None, ResponseContentEncoding: str = None, ResponseContentLanguage: str = None, ResponseContentType: str = None, ResponseExpires: datetime = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def head(self, IfMatch: str = None, IfModifiedSince: datetime = None, IfNoneMatch: str = None, IfUnmodifiedSince: datetime = None, Range: str = None, SSECustomerAlgorithm: str = None, SSECustomerKey: str = None, SSECustomerKeyMD5: str = None, RequestPayer: str = None, PartNumber: int = None, ExpectedBucketOwner: str = None) -> Dict:
        pass



class buckets(ResourceCollection):
    @classmethod
    async def all(cls) -> List[Bucket]:
        pass

    @classmethod
    async def filter(cls) -> List[Bucket]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls) -> List[Bucket]:
        pass

    @classmethod
    async def page_size(cls) -> List[Bucket]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass

