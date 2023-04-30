from datetime import datetime
from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class DescribeAggregateComplianceByConfigRules(AioPaginator):
    async def paginate(self, ConfigurationAggregatorName: str, Filters: Dict = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeAggregationAuthorizations(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeComplianceByConfigRule(AioPaginator):
    async def paginate(self, ConfigRuleNames: List = None, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeComplianceByResource(AioPaginator):
    async def paginate(self, ResourceType: str = None, ResourceId: str = None, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeConfigRuleEvaluationStatus(AioPaginator):
    async def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeConfigRules(AioPaginator):
    async def paginate(self, ConfigRuleNames: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeConfigurationAggregatorSourcesStatus(AioPaginator):
    async def paginate(self, ConfigurationAggregatorName: str, UpdateStatus: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeConfigurationAggregators(AioPaginator):
    async def paginate(self, ConfigurationAggregatorNames: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribePendingAggregationRequests(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeRemediationExecutionStatus(AioPaginator):
    async def paginate(self, ConfigRuleName: str, ResourceKeys: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeRetentionConfigurations(AioPaginator):
    async def paginate(self, RetentionConfigurationNames: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetAggregateComplianceDetailsByConfigRule(AioPaginator):
    async def paginate(self, ConfigurationAggregatorName: str, ConfigRuleName: str, AccountId: str, AwsRegion: str, ComplianceType: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetComplianceDetailsByConfigRule(AioPaginator):
    async def paginate(self, ConfigRuleName: str, ComplianceTypes: List = None, Limit: int = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetComplianceDetailsByResource(AioPaginator):
    async def paginate(self, ResourceType: str, ResourceId: str, ComplianceTypes: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class GetResourceConfigHistory(AioPaginator):
    async def paginate(self, resourceType: str, resourceId: str, laterTime: datetime = None, earlierTime: datetime = None, chronologicalOrder: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListAggregateDiscoveredResources(AioPaginator):
    async def paginate(self, ConfigurationAggregatorName: str, ResourceType: str, Filters: Dict = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListDiscoveredResources(AioPaginator):
    async def paginate(self, resourceType: str, resourceIds: List = None, resourceName: str = None, limit: int = None, includeDeletedResources: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
