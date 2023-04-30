from __future__ import annotations

from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None) -> bool:
        pass

    async def create_broker(self, AuthenticationStrategy: str = None, AutoMinorVersionUpgrade: bool = None, BrokerName: str = None, Configuration: Dict = None, CreatorRequestId: str = None, DeploymentMode: str = None, EncryptionOptions: Dict = None, EngineType: str = None, EngineVersion: str = None, HostInstanceType: str = None, LdapServerMetadata: Dict = None, Logs: Dict = None, MaintenanceWindowStartTime: Dict = None, PubliclyAccessible: bool = None, SecurityGroups: List = None, StorageType: str = None, SubnetIds: List = None, Tags: Dict = None, Users: List = None) -> Dict:
        pass

    async def create_configuration(self, AuthenticationStrategy: str = None, EngineType: str = None, EngineVersion: str = None, Name: str = None, Tags: Dict = None) -> Dict:
        pass

    async def create_tags(self, ResourceArn: str, Tags: Dict = None) -> None:
        pass

    async def create_user(self, BrokerId: str, Username: str, ConsoleAccess: bool = None, Groups: List = None, Password: str = None) -> Dict:
        pass

    async def delete_broker(self, BrokerId: str) -> Dict:
        pass

    async def delete_tags(self, ResourceArn: str, TagKeys: List) -> None:
        pass

    async def delete_user(self, BrokerId: str, Username: str) -> Dict:
        pass

    async def describe_broker(self, BrokerId: str) -> Dict:
        pass

    async def describe_broker_engine_types(self, EngineType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_broker_instance_options(self, EngineType: str = None, HostInstanceType: str = None, MaxResults: int = None, NextToken: str = None, StorageType: str = None) -> Dict:
        pass

    async def describe_configuration(self, ConfigurationId: str) -> Dict:
        pass

    async def describe_configuration_revision(self, ConfigurationId: str, ConfigurationRevision: str) -> Dict:
        pass

    async def describe_user(self, BrokerId: str, Username: str) -> Dict:
        pass

    async def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> str:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_brokers(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_configuration_revisions(self, ConfigurationId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_tags(self, ResourceArn: str) -> Dict:
        pass

    async def list_users(self, BrokerId: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def reboot_broker(self, BrokerId: str) -> Dict:
        pass

    async def update_broker(self, BrokerId: str, AuthenticationStrategy: str = None, AutoMinorVersionUpgrade: bool = None, Configuration: Dict = None, EngineVersion: str = None, HostInstanceType: str = None, LdapServerMetadata: Dict = None, Logs: Dict = None, SecurityGroups: List = None) -> Dict:
        pass

    async def update_configuration(self, ConfigurationId: str, Data: str = None, Description: str = None) -> Dict:
        pass

    async def update_user(self, BrokerId: str, Username: str, ConsoleAccess: bool = None, Groups: List = None, Password: str = None) -> Dict:
        pass

