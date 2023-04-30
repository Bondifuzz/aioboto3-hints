from typing import Dict, List

from aioboto3.resources import AIOBoto3ServiceResource
from boto3.resources.collection import ResourceCollection


class ServiceResource(AIOBoto3ServiceResource):
    platform_applications: 'platform_applications'
    subscriptions: 'subscriptions'
    topics: 'topics'

    def PlatformApplication(self, arn: str = None) -> 'PlatformApplication':
        pass

    def PlatformEndpoint(self, arn: str = None) -> 'PlatformEndpoint':
        pass

    def Subscription(self, arn: str = None) -> 'Subscription':
        pass

    def Topic(self, arn: str = None) -> 'Topic':
        pass

    async def create_platform_application(self, Name: str, Platform: str, Attributes: Dict) -> 'PlatformApplication':
        pass

    async def create_topic(self, Name: str, Attributes: Dict = None, Tags: List = None) -> 'Topic':
        pass

    async def get_available_subresources(self) -> List[str]:
        pass


class PlatformApplication(AIOBoto3ServiceResource):
    attributes: Dict
    arn: str
    endpoints: 'endpoints'

    async def create_platform_endpoint(self, Token: str, CustomUserData: str = None, Attributes: Dict = None) -> 'PlatformEndpoint':
        pass

    async def delete(self):
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self):
        pass

    async def reload(self):
        pass

    async def set_attributes(self, Attributes: Dict):
        pass


class PlatformEndpoint(AIOBoto3ServiceResource):
    attributes: Dict
    arn: str

    async def delete(self):
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self):
        pass

    async def publish(self, Message: str, TopicArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    async def reload(self):
        pass

    async def set_attributes(self, Attributes: Dict):
        pass


class Subscription(AIOBoto3ServiceResource):
    attributes: Dict
    arn: str

    async def delete(self):
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self):
        pass

    async def reload(self):
        pass

    async def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        pass


class Topic(AIOBoto3ServiceResource):
    attributes: Dict
    arn: str
    subscriptions: 'subscriptions'

    async def add_permission(self, Label: str, AWSAccountId: List, ActionName: List):
        pass

    async def confirm_subscription(self, Token: str, AuthenticateOnUnsubscribe: str = None) -> 'Subscription':
        pass

    async def delete(self):
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self):
        pass

    async def publish(self, Message: str, TargetArn: str = None, PhoneNumber: str = None, Subject: str = None, MessageStructure: str = None, MessageAttributes: Dict = None) -> Dict:
        pass

    async def reload(self):
        pass

    async def remove_permission(self, Label: str):
        pass

    async def set_attributes(self, AttributeName: str, AttributeValue: str = None):
        pass

    async def subscribe(self, Protocol: str, Endpoint: str = None, Attributes: Dict = None, ReturnSubscriptionArn: bool = None) -> 'Subscription':
        pass


class platform_applications(ResourceCollection):
    
    @classmethod
    async def all(cls) -> List['PlatformApplication']:
        pass

    
    @classmethod
    async def filter(cls, NextToken: str = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    async def limit(cls, count: int = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    async def page_size(cls, count: int = None) -> List['PlatformApplication']:
        pass

    
    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass


class subscriptions(ResourceCollection):
    
    @classmethod
    async def all(cls) -> List['Subscription']:
        pass

    
    @classmethod
    async def filter(cls, NextToken: str = None) -> List['Subscription']:
        pass

    
    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    async def limit(cls, count: int = None) -> List['Subscription']:
        pass

    
    @classmethod
    async def page_size(cls, count: int = None) -> List['Subscription']:
        pass

    
    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass


class topics(ResourceCollection):
    
    @classmethod
    async def all(cls) -> List['Topic']:
        pass

    
    @classmethod
    async def filter(cls, NextToken: str = None) -> List['Topic']:
        pass

    
    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    
    @classmethod
    async def limit(cls, count: int = None) -> List['Topic']:
        pass

    
    @classmethod
    async def page_size(cls, count: int = None) -> List['Topic']:
        pass

    
    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass
