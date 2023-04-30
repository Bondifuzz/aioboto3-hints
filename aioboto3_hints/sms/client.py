from datetime import datetime
from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_app(self, name: str = None, description: str = None, roleName: str = None, clientToken: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        pass

    async def create_replication_job(self, serverId: str, seedReplicationTime: datetime, frequency: int = None, runOnce: bool = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        pass

    async def delete_app(self, appId: str = None, forceStopAppReplication: bool = None, forceTerminateApp: bool = None) -> Dict:
        pass

    async def delete_app_launch_configuration(self, appId: str = None) -> Dict:
        pass

    async def delete_app_replication_configuration(self, appId: str = None) -> Dict:
        pass

    async def delete_replication_job(self, replicationJobId: str) -> Dict:
        pass

    async def delete_server_catalog(self) -> Dict:
        pass

    async def disassociate_connector(self, connectorId: str) -> Dict:
        pass

    async def generate_change_set(self, appId: str = None, changesetFormat: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def generate_template(self, appId: str = None, templateFormat: str = None) -> Dict:
        pass

    async def get_app(self, appId: str = None) -> Dict:
        pass

    async def get_app_launch_configuration(self, appId: str = None) -> Dict:
        pass

    async def get_app_replication_configuration(self, appId: str = None) -> Dict:
        pass

    async def get_connectors(self, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_replication_jobs(self, replicationJobId: str = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    async def get_replication_runs(self, replicationJobId: str, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    async def get_servers(self, nextToken: str = None, maxResults: int = None, vmServerAddressList: List = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def import_server_catalog(self) -> Dict:
        pass

    async def launch_app(self, appId: str = None) -> Dict:
        pass

    async def list_apps(self, appIds: List = None, nextToken: str = None, maxResults: int = None) -> Dict:
        pass

    async def put_app_launch_configuration(self, appId: str = None, roleName: str = None, serverGroupLaunchConfigurations: List = None) -> Dict:
        pass

    async def put_app_replication_configuration(self, appId: str = None, serverGroupReplicationConfigurations: List = None) -> Dict:
        pass

    async def start_app_replication(self, appId: str = None) -> Dict:
        pass

    async def start_on_demand_replication_run(self, replicationJobId: str, description: str = None) -> Dict:
        pass

    async def stop_app_replication(self, appId: str = None) -> Dict:
        pass

    async def terminate_app(self, appId: str = None) -> Dict:
        pass

    async def update_app(self, appId: str = None, name: str = None, description: str = None, roleName: str = None, serverGroups: List = None, tags: List = None) -> Dict:
        pass

    async def update_replication_job(self, replicationJobId: str, frequency: int = None, nextReplicationRunStartTime: datetime = None, licenseType: str = None, roleName: str = None, description: str = None, numberOfRecentAmisToKeep: int = None, encrypted: bool = None, kmsKeyId: str = None) -> Dict:
        pass
