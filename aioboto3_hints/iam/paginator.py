from __future__ import annotations

from typing import AsyncIterator, Dict, List

from aiobotocore.paginate import AioPaginator


class GetAccountAuthorizationDetails(AioPaginator):
    async def paginate(self, Filter: List = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class GetGroup(AioPaginator):
    async def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListAccessKeys(AioPaginator):
    async def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListAccountAliases(AioPaginator):
    async def paginate(self, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListAttachedGroupPolicies(AioPaginator):
    async def paginate(self, GroupName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListAttachedRolePolicies(AioPaginator):
    async def paginate(self, RoleName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListAttachedUserPolicies(AioPaginator):
    async def paginate(self, UserName: str, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListEntitiesForPolicy(AioPaginator):
    async def paginate(self, PolicyArn: str, EntityFilter: str = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListGroupPolicies(AioPaginator):
    async def paginate(self, GroupName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListGroups(AioPaginator):
    async def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListGroupsForUser(AioPaginator):
    async def paginate(self, UserName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListInstanceProfiles(AioPaginator):
    async def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListInstanceProfilesForRole(AioPaginator):
    async def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListMFADevices(AioPaginator):
    async def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListPolicies(AioPaginator):
    async def paginate(self, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListPolicyVersions(AioPaginator):
    async def paginate(self, PolicyArn: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListRolePolicies(AioPaginator):
    async def paginate(self, RoleName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListRoles(AioPaginator):
    async def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListSSHPublicKeys(AioPaginator):
    async def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListServerCertificates(AioPaginator):
    async def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListSigningCertificates(AioPaginator):
    async def paginate(self, UserName: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListUserPolicies(AioPaginator):
    async def paginate(self, UserName: str, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListUsers(AioPaginator):
    async def paginate(self, PathPrefix: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class ListVirtualMFADevices(AioPaginator):
    async def paginate(self, AssignmentStatus: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class SimulateCustomPolicy(AioPaginator):
    async def paginate(self, PolicyInputList: List, ActionNames: List, PermissionsBoundaryPolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass



class SimulatePrincipalPolicy(AioPaginator):
    async def paginate(self, PolicySourceArn: str, ActionNames: List, PolicyInputList: List = None, PermissionsBoundaryPolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, PaginationConfig: Dict = None) -> AsyncIterator[Dict]:
        pass

