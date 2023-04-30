from typing import Dict

from aiobotocore.waiter import AIOWaiter


class FunctionExists(AIOWaiter):
    async def wait(self, FunctionName: str, Qualifier: str = None, WaiterConfig: Dict = None):
        pass
