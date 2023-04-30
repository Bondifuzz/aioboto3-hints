from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_cluster(self, BrokerNodeGroupInfo: Dict, ClusterName: str, KafkaVersion: str, NumberOfBrokerNodes: int, ClientAuthentication: Dict = None, ConfigurationInfo: Dict = None, EncryptionInfo: Dict = None, EnhancedMonitoring: str = None, Tags: Dict = None) -> Dict:
        pass

    async def create_configuration(self, KafkaVersions: List, Name: str, ServerProperties: bytes, Description: str = None) -> Dict:
        pass

    async def delete_cluster(self, ClusterArn: str, CurrentVersion: str = None) -> Dict:
        pass

    async def describe_cluster(self, ClusterArn: str) -> Dict:
        pass

    async def describe_cluster_operation(self, ClusterOperationArn: str) -> Dict:
        pass

    async def describe_configuration(self, Arn: str) -> Dict:
        pass

    async def describe_configuration_revision(self, Arn: str, Revision: int) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_bootstrap_brokers(self, ClusterArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_cluster_operations(self, ClusterArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_clusters(self, ClusterNameFilter: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_configuration_revisions(self, Arn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_configurations(self, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_nodes(self, ClusterArn: str, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    async def tag_resource(self, ResourceArn: str, Tags: Dict):
        pass

    async def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass

    async def update_broker_count(self, ClusterArn: str, CurrentVersion: str, TargetNumberOfBrokerNodes: int) -> Dict:
        pass

    async def update_broker_storage(self, ClusterArn: str, CurrentVersion: str, TargetBrokerEBSVolumeInfo: List) -> Dict:
        pass

    async def update_cluster_configuration(self, ClusterArn: str, ConfigurationInfo: Dict, CurrentVersion: str) -> Dict:
        pass
