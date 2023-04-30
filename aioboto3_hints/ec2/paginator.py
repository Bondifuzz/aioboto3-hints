from datetime import datetime
from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class DescribeByoipCidrs(AioPaginator):
    async def paginate(self, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeCapacityReservations(AioPaginator):
    async def paginate(self, CapacityReservationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClassicLinkInstances(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClientVpnAuthorizationRules(AioPaginator):
    async def paginate(self, ClientVpnEndpointId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClientVpnConnections(AioPaginator):
    async def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClientVpnEndpoints(AioPaginator):
    async def paginate(self, ClientVpnEndpointIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClientVpnRoutes(AioPaginator):
    async def paginate(self, ClientVpnEndpointId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeClientVpnTargetNetworks(AioPaginator):
    async def paginate(self, ClientVpnEndpointId: str, AssociationIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeDhcpOptions(AioPaginator):
    async def paginate(self, DhcpOptionsIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeEgressOnlyInternetGateways(AioPaginator):
    async def paginate(self, DryRun: bool = None, EgressOnlyInternetGatewayIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeFleets(AioPaginator):
    async def paginate(self, DryRun: bool = None, FleetIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeFlowLogs(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, FlowLogIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeFpgaImages(AioPaginator):
    async def paginate(self, DryRun: bool = None, FpgaImageIds: List = None, Owners: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeHostReservationOfferings(AioPaginator):
    async def paginate(self, Filters: List = None, MaxDuration: int = None, MinDuration: int = None, OfferingId: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeHostReservations(AioPaginator):
    async def paginate(self, Filters: List = None, HostReservationIdSet: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeHosts(AioPaginator):
    async def paginate(self, Filters: List = None, HostIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeIamInstanceProfileAssociations(AioPaginator):
    async def paginate(self, AssociationIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeImportImageTasks(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeImportSnapshotTasks(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeInstanceCreditSpecifications(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, InstanceIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeInstanceStatus(AioPaginator):
    async def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, IncludeAllInstances: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeInstances(AioPaginator):
    async def paginate(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeInternetGateways(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeLaunchTemplateVersions(AioPaginator):
    async def paginate(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, Versions: List = None, MinVersion: str = None, MaxVersion: str = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeLaunchTemplates(AioPaginator):
    async def paginate(self, DryRun: bool = None, LaunchTemplateIds: List = None, LaunchTemplateNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeMovingAddresses(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, PublicIps: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeNatGateways(AioPaginator):
    async def paginate(self, Filters: List = None, NatGatewayIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeNetworkAcls(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeNetworkInterfacePermissions(AioPaginator):
    async def paginate(self, NetworkInterfacePermissionIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeNetworkInterfaces(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribePrefixLists(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, PrefixListIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribePrincipalIdFormat(AioPaginator):
    async def paginate(self, DryRun: bool = None, Resources: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribePublicIpv4Pools(AioPaginator):
    async def paginate(self, PoolIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeReservedInstancesModifications(AioPaginator):
    async def paginate(self, Filters: List = None, ReservedInstancesModificationIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeReservedInstancesOfferings(AioPaginator):
    async def paginate(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, OfferingType: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeRouteTables(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeScheduledInstanceAvailability(AioPaginator):
    async def paginate(self, FirstSlotStartTimeRange: Dict, Recurrence: Dict, DryRun: bool = None, Filters: List = None, MaxSlotDurationInHours: int = None, MinSlotDurationInHours: int = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeScheduledInstances(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, ScheduledInstanceIds: List = None, SlotStartTimeRange: Dict = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSecurityGroups(AioPaginator):
    async def paginate(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSnapshots(AioPaginator):
    async def paginate(self, Filters: List = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSpotFleetInstances(AioPaginator):
    async def paginate(self, SpotFleetRequestId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSpotFleetRequests(AioPaginator):
    async def paginate(self, DryRun: bool = None, SpotFleetRequestIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSpotInstanceRequests(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSpotPriceHistory(AioPaginator):
    async def paginate(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, ProductDescriptions: List = None, StartTime: datetime = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeStaleSecurityGroups(AioPaginator):
    async def paginate(self, VpcId: str, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSubnets(AioPaginator):
    async def paginate(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTags(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTrafficMirrorFilters(AioPaginator):
    async def paginate(self, TrafficMirrorFilterIds: List = None, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTrafficMirrorSessions(AioPaginator):
    async def paginate(self, TrafficMirrorSessionIds: List = None, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTrafficMirrorTargets(AioPaginator):
    async def paginate(self, TrafficMirrorTargetIds: List = None, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTransitGatewayAttachments(AioPaginator):
    async def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTransitGatewayRouteTables(AioPaginator):
    async def paginate(self, TransitGatewayRouteTableIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTransitGatewayVpcAttachments(AioPaginator):
    async def paginate(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeTransitGateways(AioPaginator):
    async def paginate(self, TransitGatewayIds: List = None, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVolumeStatus(AioPaginator):
    async def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVolumes(AioPaginator):
    async def paginate(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVolumesModifications(AioPaginator):
    async def paginate(self, DryRun: bool = None, VolumeIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcClassicLinkDnsSupport(AioPaginator):
    async def paginate(self, VpcIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpointConnectionNotifications(AioPaginator):
    async def paginate(self, DryRun: bool = None, ConnectionNotificationId: str = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpointConnections(AioPaginator):
    async def paginate(self, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpointServiceConfigurations(AioPaginator):
    async def paginate(self, DryRun: bool = None, ServiceIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpointServicePermissions(AioPaginator):
    async def paginate(self, ServiceId: str, DryRun: bool = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpointServices(AioPaginator):
    async def paginate(self, DryRun: bool = None, ServiceNames: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcEndpoints(AioPaginator):
    async def paginate(self, DryRun: bool = None, VpcEndpointIds: List = None, Filters: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcPeeringConnections(AioPaginator):
    async def paginate(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeVpcs(AioPaginator):
    async def paginate(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetTransitGatewayAttachmentPropagations(AioPaginator):
    async def paginate(self, TransitGatewayAttachmentId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetTransitGatewayRouteTableAssociations(AioPaginator):
    async def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetTransitGatewayRouteTablePropagations(AioPaginator):
    async def paginate(self, TransitGatewayRouteTableId: str, Filters: List = None, DryRun: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
