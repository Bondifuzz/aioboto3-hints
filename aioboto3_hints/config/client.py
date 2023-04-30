from datetime import datetime
from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def batch_get_aggregate_resource_config(self, ConfigurationAggregatorName: str, ResourceIdentifiers: List) -> Dict:
        pass

    async def batch_get_resource_config(self, resourceKeys: List) -> Dict:
        pass

    async def can_paginate(self, operation_name: str = None):
        pass

    async def delete_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str):
        pass

    async def delete_config_rule(self, ConfigRuleName: str):
        pass

    async def delete_configuration_aggregator(self, ConfigurationAggregatorName: str):
        pass

    async def delete_configuration_recorder(self, ConfigurationRecorderName: str):
        pass

    async def delete_delivery_channel(self, DeliveryChannelName: str):
        pass

    async def delete_evaluation_results(self, ConfigRuleName: str) -> Dict:
        pass

    async def delete_organization_config_rule(self, OrganizationConfigRuleName: str):
        pass

    async def delete_pending_aggregation_request(self, RequesterAccountId: str, RequesterAwsRegion: str):
        pass

    async def delete_remediation_configuration(self, ConfigRuleName: str, ResourceType: str = None) -> Dict:
        pass

    async def delete_remediation_exceptions(self, ConfigRuleName: str, ResourceKeys: List) -> Dict:
        pass

    async def delete_retention_configuration(self, RetentionConfigurationName: str):
        pass

    async def deliver_config_snapshot(self, deliveryChannelName: str) -> Dict:
        pass

    async def describe_aggregate_compliance_by_config_rules(self, ConfigurationAggregatorName: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_aggregation_authorizations(self, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_compliance_by_config_rule(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        pass

    async def describe_compliance_by_resource(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_config_rule_evaluation_status(self, ConfigRuleNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_config_rules(self, ConfigRuleNames: List = None, NextToken: str = None) -> Dict:
        pass

    async def describe_configuration_aggregator_sources_status(self, ConfigurationAggregatorName: str, UpdateStatus: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_configuration_aggregators(self, ConfigurationAggregatorNames: List = None, NextToken: str = None, Limit: int = None) -> Dict:
        pass

    async def describe_configuration_recorder_status(self, ConfigurationRecorderNames: List = None) -> Dict:
        pass

    async def describe_configuration_recorders(self, ConfigurationRecorderNames: List = None) -> Dict:
        pass

    async def describe_delivery_channel_status(self, DeliveryChannelNames: List = None) -> Dict:
        pass

    async def describe_delivery_channels(self, DeliveryChannelNames: List = None) -> Dict:
        pass

    async def describe_organization_config_rule_statuses(self, OrganizationConfigRuleNames: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_organization_config_rules(self, OrganizationConfigRuleNames: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_pending_aggregation_requests(self, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_remediation_configurations(self, ConfigRuleNames: List) -> Dict:
        pass

    async def describe_remediation_exceptions(self, ConfigRuleName: str, ResourceKeys: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_remediation_execution_status(self, ConfigRuleName: str, ResourceKeys: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def describe_retention_configurations(self, RetentionConfigurationNames: List = None, NextToken: str = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def get_aggregate_compliance_details_by_config_rule(self, ConfigurationAggregatorName: str, ConfigRuleName: str, AccountId: str, AwsRegion: str, ComplianceType: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def get_aggregate_config_rule_compliance_summary(self, ConfigurationAggregatorName: str, Filters: Dict = None, GroupByKey: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def get_aggregate_discovered_resource_counts(self, ConfigurationAggregatorName: str, Filters: Dict = None, GroupByKey: str = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def get_aggregate_resource_config(self, ConfigurationAggregatorName: str, ResourceIdentifier: Dict) -> Dict:
        pass

    async def get_compliance_details_by_config_rule(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def get_compliance_details_by_resource(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, NextToken: str = None) -> Dict:
        pass

    async def get_compliance_summary_by_config_rule(self) -> Dict:
        pass

    async def get_compliance_summary_by_resource_type(self, ResourceTypes: List = None) -> Dict:
        pass

    async def get_discovered_resource_counts(self, resourceTypes: List = None, limit: int = None, nextToken: str = None) -> Dict:
        pass

    async def get_organization_config_rule_detailed_status(self, OrganizationConfigRuleName: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_resource_config_history(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, limit: int = None, nextToken: str = None) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_aggregate_discovered_resources(self, ConfigurationAggregatorName: str, ResourceType: str, Filters: Dict = None, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def list_discovered_resources(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, nextToken: str = None) -> Dict:
        pass

    async def list_tags_for_resource(self, ResourceArn: str, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def put_aggregation_authorization(self, AuthorizedAccountId: str, AuthorizedAwsRegion: str, Tags: List = None) -> Dict:
        pass

    async def put_config_rule(self, ConfigRule: Dict, Tags: List = None):
        pass

    async def put_configuration_aggregator(self, ConfigurationAggregatorName: str, AccountAggregationSources: List = None, OrganizationAggregationSource: Dict = None, Tags: List = None) -> Dict:
        pass

    async def put_configuration_recorder(self, ConfigurationRecorder: Dict):
        pass

    async def put_delivery_channel(self, DeliveryChannel: Dict):
        pass

    async def put_evaluations(self, ResultToken: str, Evaluations: List = None, TestMode: bool = None) -> Dict:
        pass

    async def put_organization_config_rule(self, OrganizationConfigRuleName: str, OrganizationManagedRuleMetadata: Dict = None, OrganizationCustomRuleMetadata: Dict = None, ExcludedAccounts: List = None) -> Dict:
        pass

    async def put_remediation_configurations(self, RemediationConfigurations: List) -> Dict:
        pass

    async def put_remediation_exceptions(self, ConfigRuleName: str, ResourceKeys: List, Message: str = None, ExpirationTime: datetime = None) -> Dict:
        pass

    async def put_retention_configuration(self, RetentionPeriodInDays: int) -> Dict:
        pass

    async def select_resource_config(self, Expression: str, Limit: int = None, NextToken: str = None) -> Dict:
        pass

    async def start_config_rules_evaluation(self, ConfigRuleNames: List = None) -> Dict:
        pass

    async def start_configuration_recorder(self, ConfigurationRecorderName: str):
        pass

    async def start_remediation_execution(self, ConfigRuleName: str, ResourceKeys: List) -> Dict:
        pass

    async def stop_configuration_recorder(self, ConfigurationRecorderName: str):
        pass

    async def tag_resource(self, ResourceArn: str, Tags: List):
        pass

    async def untag_resource(self, ResourceArn: str, TagKeys: List):
        pass
