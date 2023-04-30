from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def accept_shared_directory(self, SharedDirectoryId: str) -> Dict:
        pass

    async def add_ip_routes(self, DirectoryId: str, IpRoutes: List, UpdateSecurityGroupForDirectoryControllers: bool = None) -> Dict:
        pass

    async def add_tags_to_resource(self, ResourceId: str, Tags: List) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict:
        pass

    async def connect_directory(self, Name: str, Password: str, Size: str, ConnectSettings: Dict, ShortName: str = None, Description: str = None, Tags: List = None) -> Dict:
        pass

    async def create_alias(self, DirectoryId: str, Alias: str) -> Dict:
        pass

    async def create_computer(self, DirectoryId: str, ComputerName: str, Password: str, OrganizationalUnitDistinguishedName: str = None, ComputerAttributes: List = None) -> Dict:
        pass

    async def create_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List) -> Dict:
        pass

    async def create_directory(self, Name: str, Password: str, Size: str, ShortName: str = None, Description: str = None, VpcSettings: Dict = None, Tags: List = None) -> Dict:
        pass

    async def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict:
        pass

    async def create_microsoft_ad(self, Name: str, Password: str, VpcSettings: Dict, ShortName: str = None, Description: str = None, Edition: str = None, Tags: List = None) -> Dict:
        pass

    async def create_snapshot(self, DirectoryId: str, Name: str = None) -> Dict:
        pass

    async def create_trust(self, DirectoryId: str, RemoteDomainName: str, TrustPassword: str, TrustDirection: str, TrustType: str = None, ConditionalForwarderIpAddrs: List = None, SelectiveAuth: str = None) -> Dict:
        pass

    async def delete_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str) -> Dict:
        pass

    async def delete_directory(self, DirectoryId: str) -> Dict:
        pass

    async def delete_log_subscription(self, DirectoryId: str) -> Dict:
        pass

    async def delete_snapshot(self, SnapshotId: str) -> Dict:
        pass

    async def delete_trust(self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None) -> Dict:
        pass

    async def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict:
        pass

    async def describe_conditional_forwarders(self, DirectoryId: str, RemoteDomainNames: List = None) -> Dict:
        pass

    async def describe_directories(self, DirectoryIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_domain_controllers(self, DirectoryId: str, DomainControllerIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_event_topics(self, DirectoryId: str = None, TopicNames: List = None) -> Dict:
        pass

    async def describe_shared_directories(self, OwnerDirectoryId: str, SharedDirectoryIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_snapshots(self, DirectoryId: str = None, SnapshotIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_trusts(self, DirectoryId: str = None, TrustIds: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def disable_radius(self, DirectoryId: str) -> Dict:
        pass

    async def disable_sso(self, DirectoryId: str, UserName: str = None, Password: str = None) -> Dict:
        pass

    async def enable_radius(self, DirectoryId: str, RadiusSettings: Dict) -> Dict:
        pass

    async def enable_sso(self, DirectoryId: str, UserName: str = None, Password: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_directory_limits(self) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_snapshot_limits(self, DirectoryId: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_ip_routes(self, DirectoryId: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_log_subscriptions(self, DirectoryId: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_schema_extensions(self, DirectoryId: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_tags_for_resource(self, ResourceId: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict:
        pass

    async def reject_shared_directory(self, SharedDirectoryId: str) -> Dict:
        pass

    async def remove_ip_routes(self, DirectoryId: str, CidrIps: List) -> Dict:
        pass

    async def remove_tags_from_resource(self, ResourceId: str, TagKeys: List) -> Dict:
        pass

    async def reset_user_password(self, DirectoryId: str, UserName: str, NewPassword: str) -> Dict:
        pass

    async def restore_from_snapshot(self, SnapshotId: str) -> Dict:
        pass

    async def share_directory(self, DirectoryId: str, ShareTarget: Dict, ShareMethod: str, ShareNotes: str = None) -> Dict:
        pass

    async def start_schema_extension(self, DirectoryId: str, CreateSnapshotBeforeSchemaExtension: bool, LdifContent: str, Description: str) -> Dict:
        pass

    async def unshare_directory(self, DirectoryId: str, UnshareTarget: Dict) -> Dict:
        pass

    async def update_conditional_forwarder(self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List) -> Dict:
        pass

    async def update_number_of_domain_controllers(self, DirectoryId: str, DesiredNumber: int) -> Dict:
        pass

    async def update_radius(self, DirectoryId: str, RadiusSettings: Dict) -> Dict:
        pass

    async def update_trust(self, TrustId: str, SelectiveAuth: str = None) -> Dict:
        pass

    async def verify_trust(self, TrustId: str) -> Dict:
        pass
