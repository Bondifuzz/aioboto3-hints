from typing import Dict

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def send_ssh_public_key(self, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str) -> Dict:
        pass
