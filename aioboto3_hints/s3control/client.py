from __future__ import annotations

from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None) -> bool:
        pass

    async def create_access_point(self, AccountId: str, Name: str, Bucket: str, VpcConfiguration: Dict = None, PublicAccessBlockConfiguration: Dict = None) -> Dict:
        pass

    async def create_access_point_for_object_lambda(self, AccountId: str, Name: str, Configuration: Dict) -> Dict:
        pass

    async def create_bucket(self, Bucket: str, ACL: str = None, CreateBucketConfiguration: Dict = None, GrantFullControl: str = None, GrantRead: str = None, GrantReadACP: str = None, GrantWrite: str = None, GrantWriteACP: str = None, ObjectLockEnabledForBucket: bool = None, OutpostId: str = None) -> Dict:
        pass

    async def create_job(self, AccountId: str, Operation: Dict, Report: Dict, ClientRequestToken: str, Manifest: Dict, Priority: int, RoleArn: str, ConfirmationRequired: bool = None, Description: str = None, Tags: List = None) -> Dict:
        pass

    async def delete_access_point(self, AccountId: str, Name: str) -> None:
        pass

    async def delete_access_point_for_object_lambda(self, AccountId: str, Name: str) -> None:
        pass

    async def delete_access_point_policy(self, AccountId: str, Name: str) -> None:
        pass

    async def delete_access_point_policy_for_object_lambda(self, AccountId: str, Name: str) -> None:
        pass

    async def delete_bucket(self, AccountId: str, Bucket: str) -> None:
        pass

    async def delete_bucket_lifecycle_configuration(self, AccountId: str, Bucket: str) -> None:
        pass

    async def delete_bucket_policy(self, AccountId: str, Bucket: str) -> None:
        pass

    async def delete_bucket_tagging(self, AccountId: str, Bucket: str) -> None:
        pass

    async def delete_job_tagging(self, AccountId: str, JobId: str) -> Dict:
        pass

    async def delete_public_access_block(self, AccountId: str) -> None:
        pass

    async def delete_storage_lens_configuration(self, ConfigId: str, AccountId: str) -> None:
        pass

    async def delete_storage_lens_configuration_tagging(self, ConfigId: str, AccountId: str) -> Dict:
        pass

    async def describe_job(self, AccountId: str, JobId: str) -> Dict:
        pass

    async def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> str:
        pass

    async def get_access_point(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_configuration_for_object_lambda(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_for_object_lambda(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_policy(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_policy_for_object_lambda(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_policy_status(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_access_point_policy_status_for_object_lambda(self, AccountId: str, Name: str) -> Dict:
        pass

    async def get_bucket(self, AccountId: str, Bucket: str) -> Dict:
        pass

    async def get_bucket_lifecycle_configuration(self, AccountId: str, Bucket: str) -> Dict:
        pass

    async def get_bucket_policy(self, AccountId: str, Bucket: str) -> Dict:
        pass

    async def get_bucket_tagging(self, AccountId: str, Bucket: str) -> Dict:
        pass

    async def get_job_tagging(self, AccountId: str, JobId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_public_access_block(self, AccountId: str) -> Dict:
        pass

    async def get_storage_lens_configuration(self, ConfigId: str, AccountId: str) -> Dict:
        pass

    async def get_storage_lens_configuration_tagging(self, ConfigId: str, AccountId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_access_points(self, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_access_points_for_object_lambda(self, AccountId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_jobs(self, AccountId: str, JobStatuses: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_regional_buckets(self, AccountId: str, NextToken: str = None, MaxResults: int = None, OutpostId: str = None) -> Dict:
        pass

    async def list_storage_lens_configurations(self, AccountId: str, NextToken: str = None) -> Dict:
        pass

    async def put_access_point_configuration_for_object_lambda(self, AccountId: str, Name: str, Configuration: Dict) -> None:
        pass

    async def put_access_point_policy(self, AccountId: str, Name: str, Policy: str) -> None:
        pass

    async def put_access_point_policy_for_object_lambda(self, AccountId: str, Name: str, Policy: str) -> None:
        pass

    async def put_bucket_lifecycle_configuration(self, AccountId: str, Bucket: str, LifecycleConfiguration: Dict = None) -> None:
        pass

    async def put_bucket_policy(self, AccountId: str, Bucket: str, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> None:
        pass

    async def put_bucket_tagging(self, AccountId: str, Bucket: str, Tagging: Dict) -> None:
        pass

    async def put_job_tagging(self, AccountId: str, JobId: str, Tags: List) -> Dict:
        pass

    async def put_public_access_block(self, PublicAccessBlockConfiguration: Dict, AccountId: str) -> None:
        pass

    async def put_storage_lens_configuration(self, ConfigId: str, AccountId: str, StorageLensConfiguration: Dict, Tags: List = None) -> None:
        pass

    async def put_storage_lens_configuration_tagging(self, ConfigId: str, AccountId: str, Tags: List) -> Dict:
        pass

    async def update_job_priority(self, AccountId: str, JobId: str, Priority: int) -> Dict:
        pass

    async def update_job_status(self, AccountId: str, JobId: str, RequestedJobStatus: str, StatusUpdateReason: str = None) -> Dict:
        pass

