from datetime import datetime
from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def accept_reserved_instances_exchange_quote(self, ReservedInstanceIds: List, DryRun: bool = None, TargetConfigurations: List = None) -> Dict:
        pass

    async def accept_transit_gateway_vpc_attachment(self, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def accept_vpc_endpoint_connections(self, ServiceId: str, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    async def accept_vpc_peering_connection(self, DryRun: bool = None, VpcPeeringConnectionId: str = None) -> Dict:
        pass

    async def advertise_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass

    async def allocate_address(self, Domain: str = None, Address: str = None, PublicIpv4Pool: str = None, DryRun: bool = None) -> Dict:
        pass

    async def allocate_hosts(self, AvailabilityZone: str, InstanceType: str, Quantity: int, AutoPlacement: str = None, ClientToken: str = None, TagSpecifications: List = None, HostRecovery: str = None) -> Dict:
        pass

    async def apply_security_groups_to_client_vpn_target_network(self, ClientVpnEndpointId: str, VpcId: str, SecurityGroupIds: List, DryRun: bool = None) -> Dict:
        pass

    async def assign_ipv6_addresses(self, NetworkInterfaceId: str, Ipv6AddressCount: int = None, Ipv6Addresses: List = None) -> Dict:
        pass

    async def assign_private_ip_addresses(self, NetworkInterfaceId: str, AllowReassignment: bool = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None) -> Dict:
        pass

    async def associate_address(self, AllocationId: str = None, InstanceId: str = None, PublicIp: str = None, AllowReassociation: bool = None, DryRun: bool = None, NetworkInterfaceId: str = None, PrivateIpAddress: str = None) -> Dict:
        pass

    async def associate_client_vpn_target_network(self, ClientVpnEndpointId: str, SubnetId: str, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def associate_dhcp_options(self, DhcpOptionsId: str, VpcId: str, DryRun: bool = None):
        pass

    async def associate_iam_instance_profile(self, IamInstanceProfile: Dict, InstanceId: str) -> Dict:
        pass

    async def associate_route_table(self, RouteTableId: str, SubnetId: str, DryRun: bool = None) -> Dict:
        pass

    async def associate_subnet_cidr_block(self, Ipv6CidrBlock: str, SubnetId: str) -> Dict:
        pass

    async def associate_transit_gateway_route_table(self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def associate_vpc_cidr_block(self, VpcId: str, AmazonProvidedIpv6CidrBlock: bool = None, CidrBlock: str = None) -> Dict:
        pass

    async def attach_classic_link_vpc(self, Groups: List, InstanceId: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def attach_internet_gateway(self, InternetGatewayId: str, VpcId: str, DryRun: bool = None):
        pass

    async def attach_network_interface(self, DeviceIndex: int, InstanceId: str, NetworkInterfaceId: str, DryRun: bool = None) -> Dict:
        pass

    async def attach_volume(self, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None) -> Dict:
        pass

    async def attach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> Dict:
        pass

    async def authorize_client_vpn_ingress(self, ClientVpnEndpointId: str, TargetNetworkCidr: str, AccessGroupId: str = None, AuthorizeAllGroups: bool = None, Description: str = None, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def authorize_security_group_egress(self, GroupId: str, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None):
        pass

    async def authorize_security_group_ingress(self, CidrIp: str = None, FromPort: int = None, GroupId: str = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        pass

    async def bundle_instance(self, InstanceId: str, Storage: Dict, DryRun: bool = None) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def cancel_bundle_task(self, BundleId: str, DryRun: bool = None) -> Dict:
        pass

    async def cancel_capacity_reservation(self, CapacityReservationId: str, DryRun: bool = None) -> Dict:
        pass

    async def cancel_conversion_task(self, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None):
        pass

    async def cancel_export_task(self, ExportTaskId: str):
        pass

    async def cancel_import_task(self, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None) -> Dict:
        pass

    async def cancel_reserved_instances_listing(self, ReservedInstancesListingId: str) -> Dict:
        pass

    async def cancel_spot_fleet_requests(self, SpotFleetRequestIds: List, TerminateInstances: bool, DryRun: bool = None) -> Dict:
        pass

    async def cancel_spot_instance_requests(self, SpotInstanceRequestIds: List, DryRun: bool = None) -> Dict:
        pass

    async def confirm_product_instance(self, InstanceId: str, ProductCode: str, DryRun: bool = None) -> Dict:
        pass

    async def copy_fpga_image(self, SourceFpgaImageId: str, SourceRegion: str, DryRun: bool = None, Description: str = None, Name: str = None, ClientToken: str = None) -> Dict:
        pass

    async def copy_image(self, Name: str, SourceImageId: str, SourceRegion: str, ClientToken: str = None, Description: str = None, Encrypted: bool = None, KmsKeyId: str = None, DryRun: bool = None) -> Dict:
        pass

    async def copy_snapshot(self, SourceRegion: str, SourceSnapshotId: str, Description: str = None, DestinationRegion: str = None, Encrypted: bool = None, KmsKeyId: str = None, PresignedUrl: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_capacity_reservation(self, InstanceType: str, InstancePlatform: str, InstanceCount: int, ClientToken: str = None, AvailabilityZone: str = None, AvailabilityZoneId: str = None, Tenancy: str = None, EbsOptimized: bool = None, EphemeralStorage: bool = None, EndDate: datetime = None, EndDateType: str = None, InstanceMatchCriteria: str = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    async def create_client_vpn_endpoint(self, ClientCidrBlock: str, ServerCertificateArn: str, AuthenticationOptions: List, ConnectionLogOptions: Dict, DnsServers: List = None, TransportProtocol: str = None, Description: str = None, SplitTunnel: bool = None, DryRun: bool = None, ClientToken: str = None, TagSpecifications: List = None) -> Dict:
        pass

    async def create_client_vpn_route(self, ClientVpnEndpointId: str, DestinationCidrBlock: str, TargetVpcSubnetId: str, Description: str = None, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_customer_gateway(self, BgpAsn: int, Type: str, PublicIp: str = None, CertificateArn: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_default_subnet(self, AvailabilityZone: str, DryRun: bool = None) -> Dict:
        pass

    async def create_default_vpc(self, DryRun: bool = None) -> Dict:
        pass

    async def create_dhcp_options(self, DhcpConfigurations: List, DryRun: bool = None) -> Dict:
        pass

    async def create_egress_only_internet_gateway(self, VpcId: str, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_fleet(self, LaunchTemplateConfigs: List, TargetCapacitySpecification: Dict, DryRun: bool = None, ClientToken: str = None, SpotOptions: Dict = None, OnDemandOptions: Dict = None, ExcessCapacityTerminationPolicy: str = None, TerminateInstancesWithExpiration: bool = None, Type: str = None, ValidFrom: datetime = None, ValidUntil: datetime = None, ReplaceUnhealthyInstances: bool = None, TagSpecifications: List = None) -> Dict:
        pass

    async def create_flow_logs(self, ResourceIds: List, ResourceType: str, TrafficType: str, DryRun: bool = None, ClientToken: str = None, DeliverLogsPermissionArn: str = None, LogGroupName: str = None, LogDestinationType: str = None, LogDestination: str = None, LogFormat: str = None) -> Dict:
        pass

    async def create_fpga_image(self, InputStorageLocation: Dict, DryRun: bool = None, LogsStorageLocation: Dict = None, Description: str = None, Name: str = None, ClientToken: str = None, TagSpecifications: List = None) -> Dict:
        pass

    async def create_image(self, InstanceId: str, Name: str, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, NoReboot: bool = None) -> Dict:
        pass

    async def create_instance_export_task(self, InstanceId: str, Description: str = None, ExportToS3Task: Dict = None, TargetEnvironment: str = None) -> Dict:
        pass

    async def create_internet_gateway(self, DryRun: bool = None) -> Dict:
        pass

    async def create_key_pair(self, KeyName: str, DryRun: bool = None) -> Dict:
        pass

    async def create_launch_template(self, LaunchTemplateName: str, LaunchTemplateData: Dict, DryRun: bool = None, ClientToken: str = None, VersionDescription: str = None, TagSpecifications: List = None) -> Dict:
        pass

    async def create_launch_template_version(self, LaunchTemplateData: Dict, DryRun: bool = None, ClientToken: str = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, SourceVersion: str = None, VersionDescription: str = None) -> Dict:
        pass

    async def create_nat_gateway(self, AllocationId: str, SubnetId: str, ClientToken: str = None) -> Dict:
        pass

    async def create_network_acl(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def create_network_acl_entry(self, Egress: bool, NetworkAclId: str, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None):
        pass

    async def create_network_interface(self, SubnetId: str, Description: str = None, DryRun: bool = None, Groups: List = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, PrivateIpAddress: str = None, PrivateIpAddresses: List = None, SecondaryPrivateIpAddressCount: int = None, InterfaceType: str = None) -> Dict:
        pass

    async def create_network_interface_permission(self, NetworkInterfaceId: str, Permission: str, AwsAccountId: str = None, AwsService: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_placement_group(self, DryRun: bool = None, GroupName: str = None, Strategy: str = None, PartitionCount: int = None):
        pass

    async def create_reserved_instances_listing(self, ClientToken: str, InstanceCount: int, PriceSchedules: List, ReservedInstancesId: str) -> Dict:
        pass

    async def create_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, TransitGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None) -> Dict:
        pass

    async def create_route_table(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def create_security_group(self, Description: str, GroupName: str, VpcId: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_snapshot(self, VolumeId: str, Description: str = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    async def create_snapshots(self, InstanceSpecification: Dict, Description: str = None, TagSpecifications: List = None, DryRun: bool = None, CopyTagsFromSource: str = None) -> Dict:
        pass

    async def create_spot_datafeed_subscription(self, Bucket: str, DryRun: bool = None, Prefix: str = None) -> Dict:
        pass

    async def create_subnet(self, CidrBlock: str, VpcId: str, AvailabilityZone: str = None, AvailabilityZoneId: str = None, Ipv6CidrBlock: str = None, DryRun: bool = None) -> Dict:
        pass

    async def create_tags(self, Resources: List, Tags: List, DryRun: bool = None):
        pass

    async def create_traffic_mirror_filter(self, Description: str = None, TagSpecifications: List = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def create_traffic_mirror_filter_rule(self, TrafficMirrorFilterId: str, TrafficDirection: str, RuleNumber: int, RuleAction: str, DestinationCidrBlock: str, SourceCidrBlock: str, DestinationPortRange: Dict = None, SourcePortRange: Dict = None, Protocol: int = None, Description: str = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def create_traffic_mirror_session(self, NetworkInterfaceId: str, TrafficMirrorTargetId: str, TrafficMirrorFilterId: str, SessionNumber: int, PacketLength: int = None, VirtualNetworkId: int = None, Description: str = None, TagSpecifications: List = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def create_traffic_mirror_target(self, NetworkInterfaceId: str = None, NetworkLoadBalancerArn: str = None, Description: str = None, TagSpecifications: List = None, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def create_transit_gateway(self, Description: str = None, Options: Dict = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    async def create_transit_gateway_route(self, DestinationCidrBlock: str, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str = None, Blackhole: bool = None, DryRun: bool = None) -> Dict:
        pass

    async def create_transit_gateway_route_table(self, TransitGatewayId: str, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    async def create_transit_gateway_vpc_attachment(self, TransitGatewayId: str, VpcId: str, SubnetIds: List, Options: Dict = None, TagSpecifications: List = None, DryRun: bool = None) -> Dict:
        pass

    async def create_volume(self, AvailabilityZone: str, Encrypted: bool = None, Iops: int = None, KmsKeyId: str = None, Size: int = None, SnapshotId: str = None, VolumeType: str = None, DryRun: bool = None, TagSpecifications: List = None) -> Dict:
        pass

    async def create_vpc(self, CidrBlock: str, AmazonProvidedIpv6CidrBlock: bool = None, DryRun: bool = None, InstanceTenancy: str = None) -> Dict:
        pass

    async def create_vpc_endpoint(self, VpcId: str, ServiceName: str, DryRun: bool = None, VpcEndpointType: str = None, PolicyDocument: str = None, RouteTableIds: List = None, SubnetIds: List = None, SecurityGroupIds: List = None, ClientToken: str = None, PrivateDnsEnabled: bool = None) -> Dict:
        pass

    async def create_vpc_endpoint_connection_notification(self, ConnectionNotificationArn: str, ConnectionEvents: List, DryRun: bool = None, ServiceId: str = None, VpcEndpointId: str = None, ClientToken: str = None) -> Dict:
        pass

    async def create_vpc_endpoint_service_configuration(self, NetworkLoadBalancerArns: List, DryRun: bool = None, AcceptanceRequired: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def create_vpc_peering_connection(self, DryRun: bool = None, PeerOwnerId: str = None, PeerVpcId: str = None, VpcId: str = None, PeerRegion: str = None) -> Dict:
        pass

    async def create_vpn_connection(self, CustomerGatewayId: str, Type: str, VpnGatewayId: str = None, TransitGatewayId: str = None, DryRun: bool = None, Options: Dict = None) -> Dict:
        pass

    async def create_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str):
        pass

    async def create_vpn_gateway(self, Type: str, AvailabilityZone: str = None, AmazonSideAsn: int = None, DryRun: bool = None) -> Dict:
        pass

    async def delete_client_vpn_endpoint(self, ClientVpnEndpointId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_client_vpn_route(self, ClientVpnEndpointId: str, DestinationCidrBlock: str, TargetVpcSubnetId: str = None, DryRun: bool = None) -> Dict:
        pass

    async def delete_customer_gateway(self, CustomerGatewayId: str, DryRun: bool = None):
        pass

    async def delete_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None):
        pass

    async def delete_egress_only_internet_gateway(self, EgressOnlyInternetGatewayId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_fleets(self, FleetIds: List, TerminateInstances: bool, DryRun: bool = None) -> Dict:
        pass

    async def delete_flow_logs(self, FlowLogIds: List, DryRun: bool = None) -> Dict:
        pass

    async def delete_fpga_image(self, FpgaImageId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None):
        pass

    async def delete_key_pair(self, KeyName: str, DryRun: bool = None):
        pass

    async def delete_launch_template(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None) -> Dict:
        pass

    async def delete_launch_template_versions(self, Versions: List, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None) -> Dict:
        pass

    async def delete_nat_gateway(self, NatGatewayId: str) -> Dict:
        pass

    async def delete_network_acl(self, NetworkAclId: str, DryRun: bool = None):
        pass

    async def delete_network_acl_entry(self, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None):
        pass

    async def delete_network_interface(self, NetworkInterfaceId: str, DryRun: bool = None):
        pass

    async def delete_network_interface_permission(self, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None) -> Dict:
        pass

    async def delete_placement_group(self, GroupName: str, DryRun: bool = None):
        pass

    async def delete_queued_reserved_instances(self, ReservedInstancesIds: List, DryRun: bool = None) -> Dict:
        pass

    async def delete_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None):
        pass

    async def delete_route_table(self, RouteTableId: str, DryRun: bool = None):
        pass

    async def delete_security_group(self, GroupId: str = None, GroupName: str = None, DryRun: bool = None):
        pass

    async def delete_snapshot(self, SnapshotId: str, DryRun: bool = None):
        pass

    async def delete_spot_datafeed_subscription(self, DryRun: bool = None):
        pass

    async def delete_subnet(self, SubnetId: str, DryRun: bool = None):
        pass

    async def delete_tags(self, Resources: List, DryRun: bool = None, Tags: List = None):
        pass

    async def delete_traffic_mirror_filter(self, TrafficMirrorFilterId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_traffic_mirror_filter_rule(self, TrafficMirrorFilterRuleId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_traffic_mirror_session(self, TrafficMirrorSessionId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_traffic_mirror_target(self, TrafficMirrorTargetId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_transit_gateway(self, TransitGatewayId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_transit_gateway_route(self, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_transit_gateway_route_table(self, TransitGatewayRouteTableId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_transit_gateway_vpc_attachment(self, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_volume(self, VolumeId: str, DryRun: bool = None):
        pass

    async def delete_vpc(self, VpcId: str, DryRun: bool = None):
        pass

    async def delete_vpc_endpoint_connection_notifications(self, ConnectionNotificationIds: List, DryRun: bool = None) -> Dict:
        pass

    async def delete_vpc_endpoint_service_configurations(self, ServiceIds: List, DryRun: bool = None) -> Dict:
        pass

    async def delete_vpc_endpoints(self, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    async def delete_vpc_peering_connection(self, VpcPeeringConnectionId: str, DryRun: bool = None) -> Dict:
        pass

    async def delete_vpn_connection(self, VpnConnectionId: str, DryRun: bool = None):
        pass

    async def delete_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str):
        pass

    async def delete_vpn_gateway(self, VpnGatewayId: str, DryRun: bool = None):
        pass

    async def deprovision_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass

    async def deregister_image(self, ImageId: str, DryRun: bool = None):
        pass

    async def describe_account_attributes(self, AttributeNames: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_addresses(self, Filters: List = None, PublicIps: List = None, AllocationIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_aggregate_id_format(self, DryRun: bool = None) -> Dict:
        pass

    async def describe_availability_zones(self, Filters: List = None, ZoneNames: List = None, ZoneIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_bundle_tasks(self, BundleIds: List = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_byoip_cidrs(self, MaxResults: int, DryRun: bool = None, NextToken: str = None) -> Dict:
        pass

    async def describe_capacity_reservations(self, CapacityReservationIds: List = None, NextToken: str = None, MaxResults: int = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_classic_link_instances(self, Filters: List = None, DryRun: bool = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_client_vpn_authorization_rules(self, ClientVpnEndpointId: str, DryRun: bool = None, NextToken: str = None, Filters: List = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_client_vpn_connections(self, ClientVpnEndpointId: str, Filters: List = None, NextToken: str = None, MaxResults: int = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_client_vpn_endpoints(self, ClientVpnEndpointIds: List = None, MaxResults: int = None, NextToken: str = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_client_vpn_routes(self, ClientVpnEndpointId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_client_vpn_target_networks(self, ClientVpnEndpointId: str, AssociationIds: List = None, MaxResults: int = None, NextToken: str = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_conversion_tasks(self, ConversionTaskIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_customer_gateways(self, CustomerGatewayIds: List = None, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_dhcp_options(self, DhcpOptionsIds: List = None, Filters: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_egress_only_internet_gateways(self, DryRun: bool = None, EgressOnlyInternetGatewayIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_elastic_gpus(self, ElasticGpuIds: List = None, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_export_image_tasks(self, DryRun: bool = None, Filters: List = None, ExportImageTaskIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_export_tasks(self, ExportTaskIds: List = None) -> Dict:
        pass

    async def describe_fleet_history(self, FleetId: str, StartTime: datetime, DryRun: bool = None, EventType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_fleet_instances(self, FleetId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, Filters: List = None) -> Dict:
        pass

    async def describe_fleets(self, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, FleetIds: List = None, Filters: List = None) -> Dict:
        pass

    async def describe_flow_logs(self, DryRun: bool = None, Filters: List = None, FlowLogIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_fpga_image_attribute(self, FpgaImageId: str, Attribute: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_fpga_images(self, DryRun: bool = None, FpgaImageIds: List = None, Owners: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_host_reservation_offerings(self, Filters: List = None, MaxDuration: int = None, MaxResults: int = None, MinDuration: int = None, NextToken: str = None, OfferingId: str = None) -> Dict:
        pass

    async def describe_host_reservations(self, Filters: List = None, HostReservationIdSet: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_hosts(self, Filters: List = None, HostIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_iam_instance_profile_associations(self, AssociationIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_id_format(self, Resource: str = None) -> Dict:
        pass

    async def describe_identity_id_format(self, PrincipalArn: str, Resource: str = None) -> Dict:
        pass

    async def describe_image_attribute(self, Attribute: str, ImageId: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_images(self, ExecutableUsers: List = None, Filters: List = None, ImageIds: List = None, Owners: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_import_image_tasks(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_import_snapshot_tasks(self, DryRun: bool = None, Filters: List = None, ImportTaskIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_instance_attribute(self, Attribute: str, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_instance_credit_specifications(self, DryRun: bool = None, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_instance_status(self, Filters: List = None, InstanceIds: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None, IncludeAllInstances: bool = None) -> Dict:
        pass

    async def describe_instances(self, Filters: List = None, InstanceIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_internet_gateways(self, Filters: List = None, DryRun: bool = None, InternetGatewayIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_key_pairs(self, Filters: List = None, KeyNames: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_launch_template_versions(self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, Versions: List = None, MinVersion: str = None, MaxVersion: str = None, NextToken: str = None, MaxResults: int = None, Filters: List = None) -> Dict:
        pass

    async def describe_launch_templates(self, DryRun: bool = None, LaunchTemplateIds: List = None, LaunchTemplateNames: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_moving_addresses(self, Filters: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, PublicIps: List = None) -> Dict:
        pass

    async def describe_nat_gateways(self, Filters: List = None, MaxResults: int = None, NatGatewayIds: List = None, NextToken: str = None) -> Dict:
        pass

    async def describe_network_acls(self, Filters: List = None, DryRun: bool = None, NetworkAclIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_network_interface_attribute(self, NetworkInterfaceId: str, Attribute: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_network_interface_permissions(self, NetworkInterfacePermissionIds: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_network_interfaces(self, Filters: List = None, DryRun: bool = None, NetworkInterfaceIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_placement_groups(self, Filters: List = None, DryRun: bool = None, GroupNames: List = None) -> Dict:
        pass

    async def describe_prefix_lists(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, PrefixListIds: List = None) -> Dict:
        pass

    async def describe_principal_id_format(self, DryRun: bool = None, Resources: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_public_ipv4_pools(self, PoolIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_regions(self, Filters: List = None, RegionNames: List = None, DryRun: bool = None, AllRegions: bool = None) -> Dict:
        pass

    async def describe_reserved_instances(self, Filters: List = None, OfferingClass: str = None, ReservedInstancesIds: List = None, DryRun: bool = None, OfferingType: str = None) -> Dict:
        pass

    async def describe_reserved_instances_listings(self, Filters: List = None, ReservedInstancesId: str = None, ReservedInstancesListingId: str = None) -> Dict:
        pass

    async def describe_reserved_instances_modifications(self, Filters: List = None, ReservedInstancesModificationIds: List = None, NextToken: str = None) -> Dict:
        pass

    async def describe_reserved_instances_offerings(self, AvailabilityZone: str = None, Filters: List = None, IncludeMarketplace: bool = None, InstanceType: str = None, MaxDuration: int = None, MaxInstanceCount: int = None, MinDuration: int = None, OfferingClass: str = None, ProductDescription: str = None, ReservedInstancesOfferingIds: List = None, DryRun: bool = None, InstanceTenancy: str = None, MaxResults: int = None, NextToken: str = None, OfferingType: str = None) -> Dict:
        pass

    async def describe_route_tables(self, Filters: List = None, DryRun: bool = None, RouteTableIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_scheduled_instance_availability(self, FirstSlotStartTimeRange: Dict, Recurrence: Dict, DryRun: bool = None, Filters: List = None, MaxResults: int = None, MaxSlotDurationInHours: int = None, MinSlotDurationInHours: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_scheduled_instances(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, ScheduledInstanceIds: List = None, SlotStartTimeRange: Dict = None) -> Dict:
        pass

    async def describe_security_group_references(self, GroupId: List, DryRun: bool = None) -> Dict:
        pass

    async def describe_security_groups(self, Filters: List = None, GroupIds: List = None, GroupNames: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_snapshot_attribute(self, Attribute: str, SnapshotId: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_snapshots(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, OwnerIds: List = None, RestorableByUserIds: List = None, SnapshotIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_spot_datafeed_subscription(self, DryRun: bool = None) -> Dict:
        pass

    async def describe_spot_fleet_instances(self, SpotFleetRequestId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_spot_fleet_request_history(self, SpotFleetRequestId: str, StartTime: datetime, DryRun: bool = None, EventType: str = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_spot_fleet_requests(self, DryRun: bool = None, MaxResults: int = None, NextToken: str = None, SpotFleetRequestIds: List = None) -> Dict:
        pass

    async def describe_spot_instance_requests(self, Filters: List = None, DryRun: bool = None, SpotInstanceRequestIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_spot_price_history(self, Filters: List = None, AvailabilityZone: str = None, DryRun: bool = None, EndTime: datetime = None, InstanceTypes: List = None, MaxResults: int = None, NextToken: str = None, ProductDescriptions: List = None, StartTime: datetime = None) -> Dict:
        pass

    async def describe_stale_security_groups(self, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_subnets(self, Filters: List = None, SubnetIds: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_tags(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_traffic_mirror_filters(self, TrafficMirrorFilterIds: List = None, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_traffic_mirror_sessions(self, TrafficMirrorSessionIds: List = None, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_traffic_mirror_targets(self, TrafficMirrorTargetIds: List = None, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_transit_gateway_attachments(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_transit_gateway_route_tables(self, TransitGatewayRouteTableIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_transit_gateway_vpc_attachments(self, TransitGatewayAttachmentIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_transit_gateways(self, TransitGatewayIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_volume_attribute(self, Attribute: str, VolumeId: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_volume_status(self, Filters: List = None, MaxResults: int = None, NextToken: str = None, VolumeIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_volumes(self, Filters: List = None, VolumeIds: List = None, DryRun: bool = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_volumes_modifications(self, DryRun: bool = None, VolumeIds: List = None, Filters: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_vpc_attribute(self, Attribute: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def describe_vpc_classic_link(self, Filters: List = None, DryRun: bool = None, VpcIds: List = None) -> Dict:
        pass

    async def describe_vpc_classic_link_dns_support(self, MaxResults: int = None, NextToken: str = None, VpcIds: List = None) -> Dict:
        pass

    async def describe_vpc_endpoint_connection_notifications(self, DryRun: bool = None, ConnectionNotificationId: str = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_endpoint_connections(self, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_endpoint_service_configurations(self, DryRun: bool = None, ServiceIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_endpoint_service_permissions(self, ServiceId: str, DryRun: bool = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_endpoint_services(self, DryRun: bool = None, ServiceNames: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_endpoints(self, DryRun: bool = None, VpcEndpointIds: List = None, Filters: List = None, MaxResults: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_vpc_peering_connections(self, Filters: List = None, DryRun: bool = None, VpcPeeringConnectionIds: List = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_vpcs(self, Filters: List = None, VpcIds: List = None, DryRun: bool = None, NextToken: str = None, MaxResults: int = None) -> Dict:
        pass

    async def describe_vpn_connections(self, Filters: List = None, VpnConnectionIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def describe_vpn_gateways(self, Filters: List = None, VpnGatewayIds: List = None, DryRun: bool = None) -> Dict:
        pass

    async def detach_classic_link_vpc(self, InstanceId: str, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def detach_internet_gateway(self, InternetGatewayId: str, VpcId: str, DryRun: bool = None):
        pass

    async def detach_network_interface(self, AttachmentId: str, DryRun: bool = None, Force: bool = None):
        pass

    async def detach_volume(self, VolumeId: str, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None) -> Dict:
        pass

    async def detach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None):
        pass

    async def disable_ebs_encryption_by_default(self, DryRun: bool = None) -> Dict:
        pass

    async def disable_transit_gateway_route_table_propagation(self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def disable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str):
        pass

    async def disable_vpc_classic_link(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def disable_vpc_classic_link_dns_support(self, VpcId: str = None) -> Dict:
        pass

    async def disassociate_address(self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None):
        pass

    async def disassociate_client_vpn_target_network(self, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = None) -> Dict:
        pass

    async def disassociate_iam_instance_profile(self, AssociationId: str) -> Dict:
        pass

    async def disassociate_route_table(self, AssociationId: str, DryRun: bool = None):
        pass

    async def disassociate_subnet_cidr_block(self, AssociationId: str) -> Dict:
        pass

    async def disassociate_transit_gateway_route_table(self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def disassociate_vpc_cidr_block(self, AssociationId: str) -> Dict:
        pass

    async def enable_ebs_encryption_by_default(self, DryRun: bool = None) -> Dict:
        pass

    async def enable_transit_gateway_route_table_propagation(self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def enable_vgw_route_propagation(self, GatewayId: str, RouteTableId: str):
        pass

    async def enable_volume_io(self, VolumeId: str, DryRun: bool = None):
        pass

    async def enable_vpc_classic_link(self, VpcId: str, DryRun: bool = None) -> Dict:
        pass

    async def enable_vpc_classic_link_dns_support(self, VpcId: str = None) -> Dict:
        pass

    async def export_client_vpn_client_certificate_revocation_list(self, ClientVpnEndpointId: str, DryRun: bool = None) -> Dict:
        pass

    async def export_client_vpn_client_configuration(self, ClientVpnEndpointId: str, DryRun: bool = None) -> Dict:
        pass

    async def export_image(self, DiskImageFormat: str, ImageId: str, S3ExportLocation: Dict, ClientToken: str = None, Description: str = None, DryRun: bool = None, RoleName: str = None) -> Dict:
        pass

    async def export_transit_gateway_routes(self, TransitGatewayRouteTableId: str, S3Bucket: str, Filters: List = None, DryRun: bool = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_capacity_reservation_usage(self, CapacityReservationId: str, NextToken: str = None, MaxResults: int = None, DryRun: bool = None) -> Dict:
        pass

    async def get_console_output(self, InstanceId: str, DryRun: bool = None, Latest: bool = None) -> Dict:
        pass

    async def get_console_screenshot(self, InstanceId: str, DryRun: bool = None, WakeUp: bool = None) -> Dict:
        pass

    async def get_ebs_default_kms_key_id(self, DryRun: bool = None) -> Dict:
        pass

    async def get_ebs_encryption_by_default(self, DryRun: bool = None) -> Dict:
        pass

    async def get_host_reservation_purchase_preview(self, HostIdSet: List, OfferingId: str) -> Dict:
        pass

    async def get_launch_template_data(self, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_password_data(self, InstanceId: str, DryRun: bool = None) -> Dict:
        pass

    async def get_reserved_instances_exchange_quote(self, ReservedInstanceIds: List, DryRun: bool = None, TargetConfigurations: List = None) -> Dict:
        pass

    async def get_transit_gateway_attachment_propagations(self, TransitGatewayAttachmentId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def get_transit_gateway_route_table_associations(self, TransitGatewayRouteTableId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def get_transit_gateway_route_table_propagations(self, TransitGatewayRouteTableId: str, Filters: List = None, MaxResults: int = None, NextToken: str = None, DryRun: bool = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def import_client_vpn_client_certificate_revocation_list(self, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = None) -> Dict:
        pass

    async def import_image(self, Architecture: str = None, ClientData: Dict = None, ClientToken: str = None, Description: str = None, DiskContainers: List = None, DryRun: bool = None, Encrypted: bool = None, Hypervisor: str = None, KmsKeyId: str = None, LicenseType: str = None, Platform: str = None, RoleName: str = None) -> Dict:
        pass

    async def import_instance(self, Platform: str, Description: str = None, DiskImages: List = None, DryRun: bool = None, LaunchSpecification: Dict = None) -> Dict:
        pass

    async def import_key_pair(self, KeyName: str, PublicKeyMaterial: bytes, DryRun: bool = None) -> Dict:
        pass

    async def import_snapshot(self, ClientData: Dict = None, ClientToken: str = None, Description: str = None, DiskContainer: Dict = None, DryRun: bool = None, Encrypted: bool = None, KmsKeyId: str = None, RoleName: str = None) -> Dict:
        pass

    async def import_volume(self, AvailabilityZone: str, Image: Dict, Volume: Dict, Description: str = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_capacity_reservation(self, CapacityReservationId: str, InstanceCount: int = None, EndDate: datetime = None, EndDateType: str = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_client_vpn_endpoint(self, ClientVpnEndpointId: str, ServerCertificateArn: str = None, ConnectionLogOptions: Dict = None, DnsServers: Dict = None, Description: str = None, SplitTunnel: bool = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_ebs_default_kms_key_id(self, KmsKeyId: str, DryRun: bool = None) -> Dict:
        pass

    async def modify_fleet(self, FleetId: str, TargetCapacitySpecification: Dict, DryRun: bool = None, ExcessCapacityTerminationPolicy: str = None) -> Dict:
        pass

    async def modify_fpga_image_attribute(self, FpgaImageId: str, DryRun: bool = None, Attribute: str = None, OperationType: str = None, UserIds: List = None, UserGroups: List = None, ProductCodes: List = None, LoadPermission: Dict = None, Description: str = None, Name: str = None) -> Dict:
        pass

    async def modify_hosts(self, HostIds: List, AutoPlacement: str = None, HostRecovery: str = None) -> Dict:
        pass

    async def modify_id_format(self, Resource: str, UseLongIds: bool):
        pass

    async def modify_identity_id_format(self, PrincipalArn: str, Resource: str, UseLongIds: bool):
        pass

    async def modify_image_attribute(self, ImageId: str, Attribute: str = None, Description: Dict = None, LaunchPermission: Dict = None, OperationType: str = None, ProductCodes: List = None, UserGroups: List = None, UserIds: List = None, Value: str = None, DryRun: bool = None):
        pass

    async def modify_instance_attribute(self, InstanceId: str, SourceDestCheck: Dict = None, Attribute: str = None, BlockDeviceMappings: List = None, DisableApiTermination: Dict = None, DryRun: bool = None, EbsOptimized: Dict = None, EnaSupport: Dict = None, Groups: List = None, InstanceInitiatedShutdownBehavior: Dict = None, InstanceType: Dict = None, Kernel: Dict = None, Ramdisk: Dict = None, SriovNetSupport: Dict = None, UserData: Dict = None, Value: str = None):
        pass

    async def modify_instance_capacity_reservation_attributes(self, InstanceId: str, CapacityReservationSpecification: Dict, DryRun: bool = None) -> Dict:
        pass

    async def modify_instance_credit_specification(self, InstanceCreditSpecifications: List, DryRun: bool = None, ClientToken: str = None) -> Dict:
        pass

    async def modify_instance_event_start_time(self, InstanceId: str, InstanceEventId: str, NotBefore: datetime, DryRun: bool = None) -> Dict:
        pass

    async def modify_instance_placement(self, InstanceId: str, Affinity: str = None, GroupName: str = None, HostId: str = None, Tenancy: str = None, PartitionNumber: int = None) -> Dict:
        pass

    async def modify_launch_template(self, DryRun: bool = None, ClientToken: str = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None, DefaultVersion: str = None) -> Dict:
        pass

    async def modify_network_interface_attribute(self, NetworkInterfaceId: str, Attachment: Dict = None, Description: Dict = None, DryRun: bool = None, Groups: List = None, SourceDestCheck: Dict = None):
        pass

    async def modify_reserved_instances(self, ReservedInstancesIds: List, TargetConfigurations: List, ClientToken: str = None) -> Dict:
        pass

    async def modify_snapshot_attribute(self, SnapshotId: str, Attribute: str = None, CreateVolumePermission: Dict = None, GroupNames: List = None, OperationType: str = None, UserIds: List = None, DryRun: bool = None):
        pass

    async def modify_spot_fleet_request(self, SpotFleetRequestId: str, ExcessCapacityTerminationPolicy: str = None, TargetCapacity: int = None, OnDemandTargetCapacity: int = None) -> Dict:
        pass

    async def modify_subnet_attribute(self, SubnetId: str, AssignIpv6AddressOnCreation: Dict = None, MapPublicIpOnLaunch: Dict = None):
        pass

    async def modify_traffic_mirror_filter_network_services(self, TrafficMirrorFilterId: str, AddNetworkServices: List = None, RemoveNetworkServices: List = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_traffic_mirror_filter_rule(self, TrafficMirrorFilterRuleId: str, TrafficDirection: str = None, RuleNumber: int = None, RuleAction: str = None, DestinationPortRange: Dict = None, SourcePortRange: Dict = None, Protocol: int = None, DestinationCidrBlock: str = None, SourceCidrBlock: str = None, Description: str = None, RemoveFields: List = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_traffic_mirror_session(self, TrafficMirrorSessionId: str, TrafficMirrorTargetId: str = None, TrafficMirrorFilterId: str = None, PacketLength: int = None, SessionNumber: int = None, VirtualNetworkId: int = None, Description: str = None, RemoveFields: List = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_transit_gateway_vpc_attachment(self, TransitGatewayAttachmentId: str, AddSubnetIds: List = None, RemoveSubnetIds: List = None, Options: Dict = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_volume(self, VolumeId: str, DryRun: bool = None, Size: int = None, VolumeType: str = None, Iops: int = None) -> Dict:
        pass

    async def modify_volume_attribute(self, VolumeId: str, AutoEnableIO: Dict = None, DryRun: bool = None):
        pass

    async def modify_vpc_attribute(self, VpcId: str, EnableDnsHostnames: Dict = None, EnableDnsSupport: Dict = None):
        pass

    async def modify_vpc_endpoint(self, VpcEndpointId: str, DryRun: bool = None, ResetPolicy: bool = None, PolicyDocument: str = None, AddRouteTableIds: List = None, RemoveRouteTableIds: List = None, AddSubnetIds: List = None, RemoveSubnetIds: List = None, AddSecurityGroupIds: List = None, RemoveSecurityGroupIds: List = None, PrivateDnsEnabled: bool = None) -> Dict:
        pass

    async def modify_vpc_endpoint_connection_notification(self, ConnectionNotificationId: str, DryRun: bool = None, ConnectionNotificationArn: str = None, ConnectionEvents: List = None) -> Dict:
        pass

    async def modify_vpc_endpoint_service_configuration(self, ServiceId: str, DryRun: bool = None, AcceptanceRequired: bool = None, AddNetworkLoadBalancerArns: List = None, RemoveNetworkLoadBalancerArns: List = None) -> Dict:
        pass

    async def modify_vpc_endpoint_service_permissions(self, ServiceId: str, DryRun: bool = None, AddAllowedPrincipals: List = None, RemoveAllowedPrincipals: List = None) -> Dict:
        pass

    async def modify_vpc_peering_connection_options(self, VpcPeeringConnectionId: str, AccepterPeeringConnectionOptions: Dict = None, DryRun: bool = None, RequesterPeeringConnectionOptions: Dict = None) -> Dict:
        pass

    async def modify_vpc_tenancy(self, VpcId: str, InstanceTenancy: str, DryRun: bool = None) -> Dict:
        pass

    async def modify_vpn_connection(self, VpnConnectionId: str, TransitGatewayId: str = None, CustomerGatewayId: str = None, VpnGatewayId: str = None, DryRun: bool = None) -> Dict:
        pass

    async def modify_vpn_tunnel_certificate(self, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None) -> Dict:
        pass

    async def modify_vpn_tunnel_options(self, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, TunnelOptions: Dict, DryRun: bool = None) -> Dict:
        pass

    async def monitor_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    async def move_address_to_vpc(self, PublicIp: str, DryRun: bool = None) -> Dict:
        pass

    async def provision_byoip_cidr(self, Cidr: str, CidrAuthorizationContext: Dict = None, Description: str = None, DryRun: bool = None) -> Dict:
        pass

    async def purchase_host_reservation(self, HostIdSet: List, OfferingId: str, ClientToken: str = None, CurrencyCode: str = None, LimitPrice: str = None) -> Dict:
        pass

    async def purchase_reserved_instances_offering(self, InstanceCount: int, ReservedInstancesOfferingId: str, DryRun: bool = None, LimitPrice: Dict = None, PurchaseTime: datetime = None) -> Dict:
        pass

    async def purchase_scheduled_instances(self, PurchaseRequests: List, ClientToken: str = None, DryRun: bool = None) -> Dict:
        pass

    async def reboot_instances(self, InstanceIds: List, DryRun: bool = None):
        pass

    async def register_image(self, Name: str, ImageLocation: str = None, Architecture: str = None, BlockDeviceMappings: List = None, Description: str = None, DryRun: bool = None, EnaSupport: bool = None, KernelId: str = None, BillingProducts: List = None, RamdiskId: str = None, RootDeviceName: str = None, SriovNetSupport: str = None, VirtualizationType: str = None) -> Dict:
        pass

    async def reject_transit_gateway_vpc_attachment(self, TransitGatewayAttachmentId: str, DryRun: bool = None) -> Dict:
        pass

    async def reject_vpc_endpoint_connections(self, ServiceId: str, VpcEndpointIds: List, DryRun: bool = None) -> Dict:
        pass

    async def reject_vpc_peering_connection(self, VpcPeeringConnectionId: str, DryRun: bool = None) -> Dict:
        pass

    async def release_address(self, AllocationId: str = None, PublicIp: str = None, DryRun: bool = None):
        pass

    async def release_hosts(self, HostIds: List) -> Dict:
        pass

    async def replace_iam_instance_profile_association(self, IamInstanceProfile: Dict, AssociationId: str) -> Dict:
        pass

    async def replace_network_acl_association(self, AssociationId: str, NetworkAclId: str, DryRun: bool = None) -> Dict:
        pass

    async def replace_network_acl_entry(self, Egress: bool, NetworkAclId: str, Protocol: str, RuleAction: str, RuleNumber: int, CidrBlock: str = None, DryRun: bool = None, IcmpTypeCode: Dict = None, Ipv6CidrBlock: str = None, PortRange: Dict = None):
        pass

    async def replace_route(self, RouteTableId: str, DestinationCidrBlock: str = None, DestinationIpv6CidrBlock: str = None, DryRun: bool = None, EgressOnlyInternetGatewayId: str = None, GatewayId: str = None, InstanceId: str = None, NatGatewayId: str = None, TransitGatewayId: str = None, NetworkInterfaceId: str = None, VpcPeeringConnectionId: str = None):
        pass

    async def replace_route_table_association(self, AssociationId: str, RouteTableId: str, DryRun: bool = None) -> Dict:
        pass

    async def replace_transit_gateway_route(self, DestinationCidrBlock: str, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str = None, Blackhole: bool = None, DryRun: bool = None) -> Dict:
        pass

    async def report_instance_status(self, Instances: List, ReasonCodes: List, Status: str, Description: str = None, DryRun: bool = None, EndTime: datetime = None, StartTime: datetime = None):
        pass

    async def request_spot_fleet(self, SpotFleetRequestConfig: Dict, DryRun: bool = None) -> Dict:
        pass

    async def request_spot_instances(self, AvailabilityZoneGroup: str = None, BlockDurationMinutes: int = None, ClientToken: str = None, DryRun: bool = None, InstanceCount: int = None, LaunchGroup: str = None, LaunchSpecification: Dict = None, SpotPrice: str = None, Type: str = None, ValidFrom: datetime = None, ValidUntil: datetime = None, InstanceInterruptionBehavior: str = None) -> Dict:
        pass

    async def reset_ebs_default_kms_key_id(self, DryRun: bool = None) -> Dict:
        pass

    async def reset_fpga_image_attribute(self, FpgaImageId: str, DryRun: bool = None, Attribute: str = None) -> Dict:
        pass

    async def reset_image_attribute(self, Attribute: str, ImageId: str, DryRun: bool = None):
        pass

    async def reset_instance_attribute(self, Attribute: str, InstanceId: str, DryRun: bool = None):
        pass

    async def reset_network_interface_attribute(self, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None):
        pass

    async def reset_snapshot_attribute(self, Attribute: str, SnapshotId: str, DryRun: bool = None):
        pass

    async def restore_address_to_classic(self, PublicIp: str, DryRun: bool = None) -> Dict:
        pass

    async def revoke_client_vpn_ingress(self, ClientVpnEndpointId: str, TargetNetworkCidr: str, AccessGroupId: str = None, RevokeAllGroups: bool = None, DryRun: bool = None) -> Dict:
        pass

    async def revoke_security_group_egress(self, GroupId: str, DryRun: bool = None, IpPermissions: List = None, CidrIp: str = None, FromPort: int = None, IpProtocol: str = None, ToPort: int = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None):
        pass

    async def revoke_security_group_ingress(self, CidrIp: str = None, FromPort: int = None, GroupId: str = None, GroupName: str = None, IpPermissions: List = None, IpProtocol: str = None, SourceSecurityGroupName: str = None, SourceSecurityGroupOwnerId: str = None, ToPort: int = None, DryRun: bool = None):
        pass

    async def run_instances(self, MaxCount: int, MinCount: int, BlockDeviceMappings: List = None, ImageId: str = None, InstanceType: str = None, Ipv6AddressCount: int = None, Ipv6Addresses: List = None, KernelId: str = None, KeyName: str = None, Monitoring: Dict = None, Placement: Dict = None, RamdiskId: str = None, SecurityGroupIds: List = None, SecurityGroups: List = None, SubnetId: str = None, UserData: str = None, AdditionalInfo: str = None, ClientToken: str = None, DisableApiTermination: bool = None, DryRun: bool = None, EbsOptimized: bool = None, IamInstanceProfile: Dict = None, InstanceInitiatedShutdownBehavior: str = None, NetworkInterfaces: List = None, PrivateIpAddress: str = None, ElasticGpuSpecification: List = None, ElasticInferenceAccelerators: List = None, TagSpecifications: List = None, LaunchTemplate: Dict = None, InstanceMarketOptions: Dict = None, CreditSpecification: Dict = None, CpuOptions: Dict = None, CapacityReservationSpecification: Dict = None, HibernationOptions: Dict = None, LicenseSpecifications: List = None) -> Dict:
        pass

    async def run_scheduled_instances(self, LaunchSpecification: Dict, ScheduledInstanceId: str, ClientToken: str = None, DryRun: bool = None, InstanceCount: int = None) -> Dict:
        pass

    async def search_transit_gateway_routes(self, TransitGatewayRouteTableId: str, Filters: List, MaxResults: int = None, DryRun: bool = None) -> Dict:
        pass

    async def send_diagnostic_interrupt(self, InstanceId: str, DryRun: bool = None):
        pass

    async def start_instances(self, InstanceIds: List, AdditionalInfo: str = None, DryRun: bool = None) -> Dict:
        pass

    async def stop_instances(self, InstanceIds: List, Hibernate: bool = None, DryRun: bool = None, Force: bool = None) -> Dict:
        pass

    async def terminate_client_vpn_connections(self, ClientVpnEndpointId: str, ConnectionId: str = None, Username: str = None, DryRun: bool = None) -> Dict:
        pass

    async def terminate_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    async def unassign_ipv6_addresses(self, Ipv6Addresses: List, NetworkInterfaceId: str) -> Dict:
        pass

    async def unassign_private_ip_addresses(self, NetworkInterfaceId: str, PrivateIpAddresses: List):
        pass

    async def unmonitor_instances(self, InstanceIds: List, DryRun: bool = None) -> Dict:
        pass

    async def update_security_group_rule_descriptions_egress(self, IpPermissions: List, DryRun: bool = None, GroupId: str = None, GroupName: str = None) -> Dict:
        pass

    async def update_security_group_rule_descriptions_ingress(self, IpPermissions: List, DryRun: bool = None, GroupId: str = None, GroupName: str = None) -> Dict:
        pass

    async def withdraw_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> Dict:
        pass
