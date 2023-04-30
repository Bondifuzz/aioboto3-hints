from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def activate_event_source(self, Name: str):
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_event_bus(self, Name: str, EventSourceName: str = None) -> Dict:
        pass

    async def create_partner_event_source(self, Name: str, Account: str) -> Dict:
        pass

    async def deactivate_event_source(self, Name: str):
        pass

    async def delete_event_bus(self, Name: str):
        pass

    async def delete_partner_event_source(self, Name: str, Account: str):
        pass

    async def delete_rule(self, Name: str, EventBusName: str = None, Force: bool = None):
        pass

    async def describe_event_bus(self, Name: str = None) -> Dict:
        pass

    async def describe_event_source(self, Name: str) -> Dict:
        pass

    async def describe_partner_event_source(self, Name: str) -> Dict:
        pass

    async def describe_rule(self, Name: str, EventBusName: str = None) -> Dict:
        pass

    async def disable_rule(self, Name: str, EventBusName: str = None):
        pass

    async def enable_rule(self, Name: str, EventBusName: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_event_buses(self, NamePrefix: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_event_sources(self, NamePrefix: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_partner_event_source_accounts(self, EventSourceName: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_partner_event_sources(self, NamePrefix: str, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_rule_names_by_target(self, TargetArn: str, EventBusName: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_rules(self, NamePrefix: str = None, EventBusName: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def list_tags_for_resource(self, ResourceARN: str) -> Dict:
        pass

    async def list_targets_by_rule(self, Rule: str, EventBusName: str = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def put_events(self, Entries: List) -> Dict:
        pass

    async def put_partner_events(self, Entries: List) -> Dict:
        pass

    async def put_permission(self, Action: str, Principal: str, StatementId: str, EventBusName: str = None, Condition: Dict = None):
        pass

    async def put_rule(self, Name: str, ScheduleExpression: str = None, EventPattern: str = None, State: str = None, Description: str = None, RoleArn: str = None, Tags: List = None, EventBusName: str = None) -> Dict:
        pass

    async def put_targets(self, Rule: str, Targets: List, EventBusName: str = None) -> Dict:
        pass

    async def remove_permission(self, StatementId: str, EventBusName: str = None):
        pass

    async def remove_targets(self, Rule: str, Ids: List, EventBusName: str = None, Force: bool = None) -> Dict:
        pass

    async def tag_resource(self, ResourceARN: str, Tags: List) -> Dict:
        pass

    async def test_event_pattern(self, EventPattern: str, Event: str) -> Dict:
        pass

    async def untag_resource(self, ResourceARN: str, TagKeys: List) -> Dict:
        pass
