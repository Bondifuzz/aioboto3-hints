from __future__ import annotations

from typing import Dict

from aiobotocore.waiter import AIOWaiter


class InstanceProfileExists(AIOWaiter):
    async def wait(self, InstanceProfileName: str, WaiterConfig: Dict = None) -> None:
        pass



class PolicyExists(AIOWaiter):
    async def wait(self, PolicyArn: str, WaiterConfig: Dict = None) -> None:
        pass



class RoleExists(AIOWaiter):
    async def wait(self, RoleName: str, WaiterConfig: Dict = None) -> None:
        pass



class UserExists(AIOWaiter):
    async def wait(self, UserName: str = None, WaiterConfig: Dict = None) -> None:
        pass

