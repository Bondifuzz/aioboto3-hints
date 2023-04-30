from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def add_permission(self, TopicArn: str, Label: str, AWSAccountId: List, ActionName: List):
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def check_if_phone_number_is_opted_out(self, phoneNumber: str) -> Dict:
        pass

    async def confirm_subscription(self, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None) -> Dict:
        pass

    async def create_platform_application(self, Name: str, Platform: str, Attributes: Dict) -> Dict:
        pass

    async def create_platform_endpoint(self, PlatformApplicationArn: str, Token: str, CustomUserData: str = None, Attributes: Dict = None) -> Dict:
        pass

    async def create_topic(self, Name: str, Attributes: Dict = None, Tags: List = None) -> Dict:
        pass

    async def delete_endpoint(self, EndpointArn: str):
        pass

    async def delete_platform_application(self, PlatformApplicationArn: str):
        pass

    async def delete_topic(self, TopicArn: str):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_endpoint_attributes(self, EndpointArn: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_platform_application_attributes(self, PlatformApplicationArn: str) -> Dict:
        pass

    async def get_sms_attributes(self, attributes: List = None) -> Dict:
        pass

    async def get_subscription_attributes(self, SubscriptionArn: str) -> Dict:
        pass

    async def get_topic_attributes(self, TopicArn: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_endpoints_by_platform_application(self, PlatformApplicationArn: str, NextToken: str = None) -> Dict:
        pass

    async def list_phone_numbers_opted_out(self, nextToken: str = None) -> Dict:
        pass

    async def list_platform_applications(self, NextToken: str = None) -> Dict:
        pass

    async def list_subscriptions(self, NextToken: str = None) -> Dict:
        pass

    async def list_subscriptions_by_topic(self, TopicArn: str, NextToken: str = None) -> Dict:
        pass

    async def list_tags_for_resource(self, ResourceArn: str) -> Dict:
        pass

    async def list_topics(self, NextToken: str = None) -> Dict:
        pass

    async def opt_in_phone_number(self, phoneNumber: str) -> Dict:
        pass

    async def publish(self, Message: str, TopicArn: str = None, TargetArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    async def remove_permission(self, TopicArn: str, Label: str):
        pass

    async def set_endpoint_attributes(self, EndpointArn: str, Attributes: Dict):
        pass

    async def set_platform_application_attributes(self, PlatformApplicationArn: str, Attributes: Dict):
        pass

    async def set_sms_attributes(self, attributes: Dict) -> Dict:
        pass

    async def set_subscription_attributes(self, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None):
        pass

    async def set_topic_attributes(self, TopicArn: str, AttributeName: str, AttributeValue: str = None):
        pass

    async def subscribe(self, TopicArn: str, Protocol: str, Endpoint: str = None, Attributes: Dict = None, ReturnSubscriptionArn: bool = None) -> Dict:
        pass

    async def tag_resource(self, ResourceArn: str, Tags: List) -> Dict:
        pass

    async def unsubscribe(self, SubscriptionArn: str):
        pass

    async def untag_resource(self, ResourceArn: str, TagKeys: List) -> Dict:
        pass
