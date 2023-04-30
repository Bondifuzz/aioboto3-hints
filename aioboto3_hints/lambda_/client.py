from datetime import datetime
from typing import IO, Dict, List, Union

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def add_layer_version_permission(self, LayerName: str, VersionNumber: int, StatementId: str, Action: str, Principal: str, OrganizationId: str = None, RevisionId: str = None) -> Dict:
        pass

    async def add_permission(self, FunctionName: str, StatementId: str, Action: str, Principal: str, SourceArn: str = None, SourceAccount: str = None, EventSourceToken: str = None, Qualifier: str = None, RevisionId: str = None) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_alias(self, FunctionName: str, Name: str, FunctionVersion: str, Description: str = None, RoutingConfig: Dict = None) -> Dict:
        pass

    async def create_event_source_mapping(self, EventSourceArn: str, FunctionName: str, Enabled: bool = None, BatchSize: int = None, MaximumBatchingWindowInSeconds: int = None, StartingPosition: str = None, StartingPositionTimestamp: datetime = None) -> Dict:
        pass

    async def create_function(self, FunctionName: str, Runtime: str, Role: str, Handler: str, Code: Dict, Description: str = None, Timeout: int = None, MemorySize: int = None, Publish: bool = None, VpcConfig: Dict = None, DeadLetterConfig: Dict = None, Environment: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, Tags: Dict = None, Layers: List = None) -> Dict:
        pass

    async def delete_alias(self, FunctionName: str, Name: str):
        pass

    async def delete_event_source_mapping(self, UUID: str) -> Dict:
        pass

    async def delete_function(self, FunctionName: str, Qualifier: str = None):
        pass

    async def delete_function_concurrency(self, FunctionName: str):
        pass

    async def delete_layer_version(self, LayerName: str, VersionNumber: int):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_account_settings(self) -> Dict:
        pass

    async def get_alias(self, FunctionName: str, Name: str) -> Dict:
        pass

    async def get_event_source_mapping(self, UUID: str) -> Dict:
        pass

    async def get_function(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    async def get_function_configuration(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    async def get_layer_version(self, LayerName: str, VersionNumber: int) -> Dict:
        pass

    async def get_layer_version_by_arn(self, Arn: str) -> Dict:
        pass

    async def get_layer_version_policy(self, LayerName: str, VersionNumber: int) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_policy(self, FunctionName: str, Qualifier: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def invoke(self, FunctionName: str, InvocationType: str = None, LogType: str = None, ClientContext: str = None, Payload: Union[bytes, IO] = None, Qualifier: str = None) -> Dict:
        pass

    async def invoke_async(self, FunctionName: str, InvokeArgs: Union[bytes, IO]) -> Dict:
        pass

    async def list_aliases(self, FunctionName: str, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_event_source_mappings(self, EventSourceArn: str = None, FunctionName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_functions(self, MasterRegion: str = None, FunctionVersion: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_layer_versions(self, LayerName: str, CompatibleRuntime: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_layers(self, CompatibleRuntime: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_tags(self, Resource: str) -> Dict:
        pass

    async def list_versions_by_function(self, FunctionName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def publish_layer_version(self, LayerName: str, Content: Dict, Description: str = None, CompatibleRuntimes: List = None, LicenseInfo: str = None) -> Dict:
        pass

    async def publish_version(self, FunctionName: str, CodeSha256: str = None, Description: str = None, RevisionId: str = None) -> Dict:
        pass

    async def put_function_concurrency(self, FunctionName: str, ReservedConcurrentExecutions: int) -> Dict:
        pass

    async def remove_layer_version_permission(self, LayerName: str, VersionNumber: int, StatementId: str, RevisionId: str = None):
        pass

    async def remove_permission(self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None):
        pass

    async def tag_resource(self, Resource: str, Tags: Dict):
        pass

    async def untag_resource(self, Resource: str, TagKeys: List):
        pass

    async def update_alias(self, FunctionName: str, Name: str, FunctionVersion: str = None, Description: str = None, RoutingConfig: Dict = None, RevisionId: str = None) -> Dict:
        pass

    async def update_event_source_mapping(self, UUID: str, FunctionName: str = None, Enabled: bool = None, BatchSize: int = None, MaximumBatchingWindowInSeconds: int = None) -> Dict:
        pass

    async def update_function_code(self, FunctionName: str, ZipFile: bytes = None, S3Bucket: str = None, S3Key: str = None, S3ObjectVersion: str = None, Publish: bool = None, DryRun: bool = None, RevisionId: str = None) -> Dict:
        pass

    async def update_function_configuration(self, FunctionName: str, Role: str = None, Handler: str = None, Description: str = None, Timeout: int = None, MemorySize: int = None, VpcConfig: Dict = None, Environment: Dict = None, Runtime: str = None, DeadLetterConfig: Dict = None, KMSKeyArn: str = None, TracingConfig: Dict = None, RevisionId: str = None, Layers: List = None) -> Dict:
        pass
