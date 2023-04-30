from typing import Dict

from aiobotocore.waiter import AIOWaiter


class TableExists(AIOWaiter):
    async def wait(self, TableName: str, WaiterConfig: Dict = None):
        pass


class TableNotExists(AIOWaiter):
    async def wait(self, TableName: str, WaiterConfig: Dict = None):
        pass
