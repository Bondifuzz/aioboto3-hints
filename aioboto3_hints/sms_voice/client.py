from typing import Dict

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict:
        pass

    async def create_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestination: Dict = None, EventDestinationName: str = None) -> Dict:
        pass

    async def delete_configuration_set(self, ConfigurationSetName: str) -> Dict:
        pass

    async def delete_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_configuration_set_event_destinations(self, ConfigurationSetName: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_configuration_sets(self, NextToken: str = None, PageSize: str = None) -> Dict:
        pass

    async def send_voice_message(self, CallerId: str = None, ConfigurationSetName: str = None, Content: Dict = None, DestinationPhoneNumber: str = None, OriginationPhoneNumber: str = None) -> Dict:
        pass

    async def update_configuration_set_event_destination(self, ConfigurationSetName: str, EventDestinationName: str, EventDestination: Dict = None) -> Dict:
        pass
