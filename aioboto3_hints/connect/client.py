from datetime import datetime
from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_user(self, Username: str, PhoneConfig: Dict, SecurityProfileIds: List, RoutingProfileId: str, InstanceId: str, Password: str = None, IdentityInfo: Dict = None, DirectoryUserId: str = None, HierarchyGroupId: str = None) -> Dict:
        pass

    async def delete_user(self, InstanceId: str, UserId: str):
        pass

    async def describe_user(self, UserId: str, InstanceId: str) -> Dict:
        pass

    async def describe_user_hierarchy_group(self, HierarchyGroupId: str, InstanceId: str) -> Dict:
        pass

    async def describe_user_hierarchy_structure(self, InstanceId: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_contact_attributes(self, InstanceId: str, InitialContactId: str) -> Dict:
        pass

    async def get_current_metric_data(self, InstanceId: str, Filters: Dict, CurrentMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def get_federation_token(self, InstanceId: str) -> Dict:
        pass

    async def get_metric_data(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_contact_flows(self, InstanceId: str, ContactFlowTypes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_hours_of_operations(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_phone_numbers(self, InstanceId: str, PhoneNumberTypes: List = None, PhoneNumberCountryCodes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_queues(self, InstanceId: str, QueueTypes: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_routing_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_security_profiles(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_user_hierarchy_groups(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def list_users(self, InstanceId: str, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def start_outbound_voice_contact(self, DestinationPhoneNumber: str, ContactFlowId: str, InstanceId: str, ClientToken: str = None, SourcePhoneNumber: str = None, QueueId: str = None, Attributes: Dict = None) -> Dict:
        pass

    async def stop_contact(self, ContactId: str, InstanceId: str) -> Dict:
        pass

    async def update_contact_attributes(self, InitialContactId: str, InstanceId: str, Attributes: Dict) -> Dict:
        pass

    async def update_user_hierarchy(self, UserId: str, InstanceId: str, HierarchyGroupId: str = None):
        pass

    async def update_user_identity_info(self, IdentityInfo: Dict, UserId: str, InstanceId: str):
        pass

    async def update_user_phone_config(self, PhoneConfig: Dict, UserId: str, InstanceId: str):
        pass

    async def update_user_routing_profile(self, RoutingProfileId: str, UserId: str, InstanceId: str):
        pass

    async def update_user_security_profiles(self, SecurityProfileIds: List, UserId: str, InstanceId: str):
        pass
