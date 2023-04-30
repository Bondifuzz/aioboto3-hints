from datetime import datetime
from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class GetMetricData(AioPaginator):
    async def paginate(self, InstanceId: str, StartTime: datetime, EndTime: datetime, Filters: Dict, HistoricalMetrics: List, Groupings: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListContactFlows(AioPaginator):
    async def paginate(self, InstanceId: str, ContactFlowTypes: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListHoursOfOperations(AioPaginator):
    async def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListPhoneNumbers(AioPaginator):
    async def paginate(self, InstanceId: str, PhoneNumberTypes: List = None, PhoneNumberCountryCodes: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListQueues(AioPaginator):
    async def paginate(self, InstanceId: str, QueueTypes: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListRoutingProfiles(AioPaginator):
    async def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListSecurityProfiles(AioPaginator):
    async def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListUserHierarchyGroups(AioPaginator):
    async def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class ListUsers(AioPaginator):
    async def paginate(self, InstanceId: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
