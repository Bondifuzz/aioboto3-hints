from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class DescribeDestinations(AioPaginator):
    async def paginate(self, DestinationNamePrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeExportTasks(AioPaginator):
    async def paginate(self, taskId: str = None, statusCode: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeLogGroups(AioPaginator):
    async def paginate(self, logGroupNamePrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeLogStreams(AioPaginator):
    async def paginate(self, logGroupName: str, logStreamNamePrefix: str = None, orderBy: str = None, descending: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeMetricFilters(AioPaginator):
    async def paginate(self, logGroupName: str = None, filterNamePrefix: str = None, metricName: str = None, metricNamespace: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeQueries(AioPaginator):
    async def paginate(self, logGroupName: str = None, status: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeResourcePolicies(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class DescribeSubscriptionFilters(AioPaginator):
    async def paginate(self, logGroupName: str, filterNamePrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass


class FilterLogEvents(AioPaginator):
    async def paginate(self, logGroupName: str, logStreamNames: List = None, logStreamNamePrefix: str = None, startTime: int = None, endTime: int = None, filterPattern: str = None, interleaved: bool = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass
