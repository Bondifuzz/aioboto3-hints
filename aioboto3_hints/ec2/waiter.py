from typing import Dict, List

from aiobotocore.waiter import AIOWaiter


class BundleTaskComplete(AIOWaiter):
    async def wait(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskCancelled(AIOWaiter):
    async def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskCompleted(AIOWaiter):
    async def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ConversionTaskDeleted(AIOWaiter):
    async def wait(self, ConversionTaskIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class CustomerGatewayAvailable(AIOWaiter):
    async def wait(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ExportTaskCancelled(AIOWaiter):
    async def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None):
        pass


class ExportTaskCompleted(AIOWaiter):
    async def wait(self, ExportTaskIds: List = None, WaiterConfig: Dict = None):
        pass


class ImageAvailable(AIOWaiter):
    async def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class ImageExists(AIOWaiter):
    async def wait(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class InstanceExists(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceRunning(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceStatusOk(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None):
        pass


class InstanceStopped(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class InstanceTerminated(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class KeyPairExists(AIOWaiter):
    async def wait(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class NatGatewayAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class NetworkInterfaceAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class PasswordDataAvailable(AIOWaiter):
    async def wait(self, InstanceId: str, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class SnapshotCompleted(AIOWaiter):
    async def wait(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class SpotInstanceRequestFulfilled(AIOWaiter):
    async def wait(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class SubnetAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class SystemStatusOk(AIOWaiter):
    async def wait(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None, WaiterConfig: Dict = None):
        pass


class VolumeAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VolumeDeleted(AIOWaiter):
    async def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VolumeInUse(AIOWaiter):
    async def wait(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, WaiterConfig: Dict = None):
        pass


class VpcAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class VpcExists(AIOWaiter):
    async def wait(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class VpcPeeringConnectionDeleted(AIOWaiter):
    async def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class VpcPeeringConnectionExists(AIOWaiter):
    async def wait(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, NextToken: str = None, MaxResults: int = None, WaiterConfig: Dict = None):
        pass


class VpnConnectionAvailable(AIOWaiter):
    async def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass


class VpnConnectionDeleted(AIOWaiter):
    async def wait(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None, WaiterConfig: Dict = None):
        pass
