from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from aioboto3.resources.base import AIOBoto3ServiceResource
from boto3.resources.collection import ResourceCollection


from boto3.resources.base import ResourceMeta as _ResourceMeta
from .client import Client

class ResourceMeta(_ResourceMeta):
    client: Optional[Client]

class ServiceResource(AIOBoto3ServiceResource):
    meta: Optional[ResourceMeta]

    groups: groups
    instance_profiles: instance_profiles
    policies: policies
    roles: roles
    saml_providers: saml_providers
    server_certificates: server_certificates
    users: users
    virtual_mfa_devices: virtual_mfa_devices

    async def AccessKey(self, user_name: str = None, id: str = None) -> AccessKey:
        pass

    async def AccessKeyPair(self, user_name: str = None, id: str = None, secret: str = None) -> AccessKeyPair:
        pass

    async def AccountPasswordPolicy(self) -> AccountPasswordPolicy:
        pass

    async def AccountSummary(self) -> AccountSummary:
        pass

    async def AssumeRolePolicy(self, role_name: str = None) -> AssumeRolePolicy:
        pass

    async def CurrentUser(self) -> CurrentUser:
        pass

    async def Group(self, name: str = None) -> Group:
        pass

    async def GroupPolicy(self, group_name: str = None, name: str = None) -> GroupPolicy:
        pass

    async def InstanceProfile(self, name: str = None) -> InstanceProfile:
        pass

    async def LoginProfile(self, user_name: str = None) -> LoginProfile:
        pass

    async def MfaDevice(self, user_name: str = None, serial_number: str = None) -> MfaDevice:
        pass

    async def Policy(self, policy_arn: str = None) -> Policy:
        pass

    async def PolicyVersion(self, arn: str = None, version_id: str = None) -> PolicyVersion:
        pass

    async def Role(self, name: str = None) -> Role:
        pass

    async def RolePolicy(self, role_name: str = None, name: str = None) -> RolePolicy:
        pass

    async def SamlProvider(self, arn: str = None) -> SamlProvider:
        pass

    async def ServerCertificate(self, name: str = None) -> ServerCertificate:
        pass

    async def SigningCertificate(self, user_name: str = None, id: str = None) -> SigningCertificate:
        pass

    async def User(self, name: str = None) -> User:
        pass

    async def UserPolicy(self, user_name: str = None, name: str = None) -> UserPolicy:
        pass

    async def VirtualMfaDevice(self, serial_number: str = None) -> VirtualMfaDevice:
        pass

    async def change_password(self, OldPassword: str, NewPassword: str) -> None:
        pass

    async def create_account_alias(self, AccountAlias: str) -> None:
        pass

    async def create_account_password_policy(self, MinimumPasswordLength: int = None, RequireSymbols: bool = None, RequireNumbers: bool = None, RequireUppercaseCharacters: bool = None, RequireLowercaseCharacters: bool = None, AllowUsersToChangePassword: bool = None, MaxPasswordAge: int = None, PasswordReusePrevention: int = None, HardExpiry: bool = None) -> AccountPasswordPolicy:
        pass

    async def create_group(self, GroupName: str, Path: str = None) -> List[Group]:
        pass

    async def create_instance_profile(self, InstanceProfileName: str, Path: str = None, Tags: List = None) -> InstanceProfile:
        pass

    async def create_policy(self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None, Tags: List = None) -> Policy:
        pass

    async def create_role(self, RoleName: str, AssumeRolePolicyDocument: str, Path: str = None, Description: str = None, MaxSessionDuration: int = None, PermissionsBoundary: str = None, Tags: List = None) -> Role:
        pass

    async def create_saml_provider(self, SAMLMetadataDocument: str, Name: str, Tags: List = None) -> SamlProvider:
        pass

    async def create_server_certificate(self, ServerCertificateName: str, CertificateBody: str, PrivateKey: str, Path: str = None, CertificateChain: str = None, Tags: List = None) -> ServerCertificate:
        pass

    async def create_signing_certificate(self, CertificateBody: str, UserName: str = None) -> SigningCertificate:
        pass

    async def create_user(self, UserName: str, Path: str = None, PermissionsBoundary: str = None, Tags: List = None) -> User:
        pass

    async def create_virtual_mfa_device(self, VirtualMFADeviceName: str, Path: str = None, Tags: List = None) -> VirtualMfaDevice:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class AccessKey(AIOBoto3ServiceResource):
    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    async def User(self) -> User:
        pass

    async def activate(self) -> None:
        pass

    async def deactivate(self) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class AccessKeyPair(AIOBoto3ServiceResource):
    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    async def activate(self) -> None:
        pass

    async def deactivate(self) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class AccountPasswordPolicy(AIOBoto3ServiceResource):
    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def update(self, MinimumPasswordLength: int = None, RequireSymbols: bool = None, RequireNumbers: bool = None, RequireUppercaseCharacters: bool = None, RequireLowercaseCharacters: bool = None, AllowUsersToChangePassword: bool = None, MaxPasswordAge: int = None, PasswordReusePrevention: int = None, HardExpiry: bool = None) -> None:
        pass



class AccountSummary(AIOBoto3ServiceResource):
    summary_map: Dict

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass



class AssumeRolePolicy(AIOBoto3ServiceResource):
    role_name: str

    async def Role(self) -> Role:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def update(self, PolicyDocument: str) -> None:
        pass



class CurrentUser(AIOBoto3ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict
    tags: List
    access_keys: access_keys
    mfa_devices: mfa_devices
    signing_certificates: signing_certificates

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass



class Group(AIOBoto3ServiceResource):
    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: attached_policies
    policies: policies
    users: users

    async def Policy(self, name: str = None) -> GroupPolicy:
        pass

    async def add_user(self, UserName: str) -> None:
        pass

    async def attach_policy(self, PolicyArn: str) -> None:
        pass

    async def create(self, Path: str = None) -> List[Group]:
        pass

    async def create_policy(self, PolicyName: str, PolicyDocument: str) -> GroupPolicy:
        pass

    async def delete(self) -> None:
        pass

    async def detach_policy(self, PolicyArn: str) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def remove_user(self, UserName: str) -> None:
        pass

    async def update(self, NewPath: str = None, NewGroupName: str = None) -> List[Group]:
        pass



class GroupPolicy(AIOBoto3ServiceResource):
    policy_name: str
    policy_document: str
    group_name: str
    name: str

    async def Group(self) -> Group:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, PolicyDocument: str) -> None:
        pass

    async def reload(self) -> None:
        pass



class InstanceProfile(AIOBoto3ServiceResource):
    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List
    tags: List
    name: str

    async def add_role(self, RoleName: str) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def remove_role(self, RoleName: str) -> None:
        pass



class LoginProfile(AIOBoto3ServiceResource):
    create_date: datetime
    password_reset_required: bool
    user_name: str

    async def User(self) -> User:
        pass

    async def create(self, Password: str, PasswordResetRequired: bool = None) -> LoginProfile:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        pass



class MfaDevice(AIOBoto3ServiceResource):
    enable_date: datetime
    user_name: str
    serial_number: str

    async def User(self) -> User:
        pass

    async def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass

    async def disassociate(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass



class Policy(AIOBoto3ServiceResource):
    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    tags: List
    arn: str
    attached_groups: attached_groups
    attached_roles: attached_roles
    attached_users: attached_users
    versions: versions

    async def attach_group(self, GroupName: str) -> None:
        pass

    async def attach_role(self, RoleName: str) -> None:
        pass

    async def attach_user(self, UserName: str) -> None:
        pass

    async def create_version(self, PolicyDocument: str, SetAsDefault: bool = None) -> PolicyVersion:
        pass

    async def delete(self) -> None:
        pass

    async def detach_group(self, GroupName: str) -> None:
        pass

    async def detach_role(self, RoleName: str) -> None:
        pass

    async def detach_user(self, UserName: str) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass



class PolicyVersion(AIOBoto3ServiceResource):
    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def set_as_default(self) -> None:
        pass



class Role(AIOBoto3ServiceResource):
    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict
    tags: List
    role_last_used: Dict
    name: str
    attached_policies: attached_policies
    instance_profiles: instance_profiles
    policies: policies

    async def AssumeRolePolicy(self) -> AssumeRolePolicy:
        pass

    async def Policy(self, name: str = None) -> RolePolicy:
        pass

    async def attach_policy(self, PolicyArn: str) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def detach_policy(self, PolicyArn: str) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass



class RolePolicy(AIOBoto3ServiceResource):
    policy_name: str
    policy_document: str
    role_name: str
    name: str

    async def Role(self) -> Role:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, PolicyDocument: str) -> None:
        pass

    async def reload(self) -> None:
        pass



class SamlProvider(AIOBoto3ServiceResource):
    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    tags: List
    arn: str

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def update(self, SAMLMetadataDocument: str) -> Dict:
        pass



class ServerCertificate(AIOBoto3ServiceResource):
    server_certificate_metadata: Dict
    certificate_body: str
    certificate_chain: str
    tags: List
    name: str

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def update(self, NewPath: str = None, NewServerCertificateName: str = None) -> ServerCertificate:
        pass



class SigningCertificate(AIOBoto3ServiceResource):
    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    async def User(self) -> User:
        pass

    async def activate(self) -> None:
        pass

    async def deactivate(self) -> None:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class User(AIOBoto3ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict
    tags: List
    name: str
    access_keys: access_keys
    attached_policies: attached_policies
    groups: groups
    mfa_devices: mfa_devices
    policies: policies
    signing_certificates: signing_certificates

    async def AccessKey(self, id: str = None) -> AccessKey:
        pass

    async def LoginProfile(self) -> LoginProfile:
        pass

    async def MfaDevice(self, serial_number: str = None) -> MfaDevice:
        pass

    async def Policy(self, name: str = None) -> UserPolicy:
        pass

    async def SigningCertificate(self, id: str = None) -> SigningCertificate:
        pass

    async def add_group(self, GroupName: str) -> None:
        pass

    async def attach_policy(self, PolicyArn: str) -> None:
        pass

    async def create(self, Path: str = None, PermissionsBoundary: str = None, Tags: List = None) -> User:
        pass

    async def create_access_key_pair(self) -> AccessKeyPair:
        pass

    async def create_login_profile(self, Password: str, PasswordResetRequired: bool = None) -> LoginProfile:
        pass

    async def create_policy(self, PolicyName: str, PolicyDocument: str) -> UserPolicy:
        pass

    async def delete(self) -> None:
        pass

    async def detach_policy(self, PolicyArn: str) -> None:
        pass

    async def enable_mfa(self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str) -> MfaDevice:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def reload(self) -> None:
        pass

    async def remove_group(self, GroupName: str) -> None:
        pass

    async def update(self, NewPath: str = None, NewUserName: str = None) -> User:
        pass



class UserPolicy(AIOBoto3ServiceResource):
    policy_name: str
    policy_document: str
    user_name: str
    name: str

    async def User(self) -> User:
        pass

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass

    async def load(self) -> None:
        pass

    async def put(self, PolicyDocument: str) -> None:
        pass

    async def reload(self) -> None:
        pass



class VirtualMfaDevice(AIOBoto3ServiceResource):
    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict
    enable_date: datetime
    tags: List
    serial_number: str

    async def delete(self) -> None:
        pass

    async def get_available_subresources(self) -> List[str]:
        pass



class groups(ResourceCollection):
    @classmethod
    async def all(cls) -> List[Group]:
        pass

    @classmethod
    async def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List[Group]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[Group]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[Group]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class instance_profiles(ResourceCollection):
    @classmethod
    async def all(cls) -> List[InstanceProfile]:
        pass

    @classmethod
    async def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List[InstanceProfile]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[InstanceProfile]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[InstanceProfile]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class policies(ResourceCollection):
    @classmethod
    async def all(cls) -> List[Policy]:
        pass

    @classmethod
    async def filter(cls, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, Marker: str = None, MaxItems: int = None) -> List[Policy]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[Policy]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[Policy]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class roles(ResourceCollection):
    @classmethod
    async def all(cls) -> List[Role]:
        pass

    @classmethod
    async def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List[Role]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[Role]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[Role]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class saml_providers(ResourceCollection):
    @classmethod
    async def all(cls) -> List[SamlProvider]:
        pass

    @classmethod
    async def filter(cls) -> List[SamlProvider]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[SamlProvider]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[SamlProvider]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class server_certificates(ResourceCollection):
    @classmethod
    async def all(cls) -> List[ServerCertificate]:
        pass

    @classmethod
    async def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List[ServerCertificate]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[ServerCertificate]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[ServerCertificate]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class users(ResourceCollection):
    @classmethod
    async def all(cls) -> List[User]:
        pass

    @classmethod
    async def filter(cls, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> List[User]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[User]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[User]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass



class virtual_mfa_devices(ResourceCollection):
    @classmethod
    async def all(cls) -> List[VirtualMfaDevice]:
        pass

    @classmethod
    async def filter(cls, AssignmentStatus: str = None, Marker: str = None, MaxItems: int = None) -> List[VirtualMfaDevice]:
        pass

    @classmethod
    async def iterator(cls) -> ResourceCollection:
        pass

    @classmethod
    async def limit(cls, count: int = None) -> List[VirtualMfaDevice]:
        pass

    @classmethod
    async def page_size(cls, count: int = None) -> List[VirtualMfaDevice]:
        pass

    @classmethod
    async def pages(cls) -> List[AIOBoto3ServiceResource]:
        pass

