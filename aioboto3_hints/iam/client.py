from __future__ import annotations

from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def add_client_id_to_open_id_connect_provider(self, OpenIDConnectProviderArn: str, ClientID: str) -> None:
        pass

    async def add_role_to_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        pass

    async def add_user_to_group(self, GroupName: str, UserName: str) -> None:
        pass

    async def attach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        pass

    async def attach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        pass

    async def attach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        pass

    async def can_paginate(self, operation_name: str = None) -> bool:
        pass

    async def change_password(self, OldPassword: str, NewPassword: str) -> None:
        pass

    async def create_access_key(self, UserName: str = None) -> Dict:
        pass

    async def create_account_alias(self, AccountAlias: str) -> None:
        pass

    async def create_group(self, GroupName: str, Path: str = None) -> Dict:
        pass

    async def create_instance_profile(self, InstanceProfileName: str, Path: str = None, Tags: List = None) -> Dict:
        pass

    async def create_login_profile(self, UserName: str, Password: str, PasswordResetRequired: bool = None) -> Dict:
        pass

    async def create_open_id_connect_provider(self, Url: str, ThumbprintList: List, ClientIDList: List = None, Tags: List = None) -> Dict:
        pass

    async def create_policy(self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None, Tags: List = None) -> Dict:
        pass

    async def create_policy_version(self, PolicyArn: str, PolicyDocument: str, SetAsDefault: bool = None) -> Dict:
        pass

    async def create_role(self, RoleName: str, AssumeRolePolicyDocument: str, Path: str = None, Description: str = None, MaxSessionDuration: int = None, PermissionsBoundary: str = None, Tags: List = None) -> Dict:
        pass

    async def create_saml_provider(self, SAMLMetadataDocument: str, Name: str, Tags: List = None) -> Dict:
        pass

    async def create_service_linked_role(self, AWSServiceName: str, Description: str = None, CustomSuffix: str = None) -> Dict:
        pass

    async def create_service_specific_credential(self, UserName: str, ServiceName: str) -> Dict:
        pass

    async def create_user(self, UserName: str, Path: str = None, PermissionsBoundary: str = None, Tags: List = None) -> Dict:
        pass

    async def create_virtual_mfa_device(self, VirtualMFADeviceName: str, Path: str = None, Tags: List = None) -> Dict:
        pass

    async def deactivate_mfa_device(self, UserName: str, SerialNumber: str) -> None:
        pass

    async def delete_access_key(self, AccessKeyId: str, UserName: str = None) -> None:
        pass

    async def delete_account_alias(self, AccountAlias: str) -> None:
        pass

    async def delete_account_password_policy(self) -> None:
        pass

    async def delete_group(self, GroupName: str) -> None:
        pass

    async def delete_group_policy(self, GroupName: str, PolicyName: str) -> None:
        pass

    async def delete_instance_profile(self, InstanceProfileName: str) -> None:
        pass

    async def delete_login_profile(self, UserName: str) -> None:
        pass

    async def delete_open_id_connect_provider(self, OpenIDConnectProviderArn: str) -> None:
        pass

    async def delete_policy(self, PolicyArn: str) -> None:
        pass

    async def delete_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        pass

    async def delete_role(self, RoleName: str) -> None:
        pass

    async def delete_role_permissions_boundary(self, RoleName: str) -> None:
        pass

    async def delete_role_policy(self, RoleName: str, PolicyName: str) -> None:
        pass

    async def delete_saml_provider(self, SAMLProviderArn: str) -> None:
        pass

    async def delete_server_certificate(self, ServerCertificateName: str) -> None:
        pass

    async def delete_service_linked_role(self, RoleName: str) -> Dict:
        pass

    async def delete_service_specific_credential(self, ServiceSpecificCredentialId: str, UserName: str = None) -> None:
        pass

    async def delete_signing_certificate(self, CertificateId: str, UserName: str = None) -> None:
        pass

    async def delete_ssh_public_key(self, UserName: str, SSHPublicKeyId: str) -> None:
        pass

    async def delete_user(self, UserName: str) -> None:
        pass

    async def delete_user_permissions_boundary(self, UserName: str) -> None:
        pass

    async def delete_user_policy(self, UserName: str, PolicyName: str) -> None:
        pass

    async def delete_virtual_mfa_device(self, SerialNumber: str) -> None:
        pass

    async def detach_group_policy(self, GroupName: str, PolicyArn: str) -> None:
        pass

    async def detach_role_policy(self, RoleName: str, PolicyArn: str) -> None:
        pass

    async def detach_user_policy(self, UserName: str, PolicyArn: str) -> None:
        pass

    async def enable_mfa_device(self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass

    async def generate_credential_report(self) -> Dict:
        pass

    async def generate_organizations_access_report(self, EntityPath: str, OrganizationsPolicyId: str = None) -> Dict:
        pass

    async def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None) -> str:
        pass

    async def generate_service_last_accessed_details(self, Arn: str, Granularity: str = None) -> Dict:
        pass

    async def get_access_key_last_used(self, AccessKeyId: str) -> Dict:
        pass

    async def get_account_authorization_details(self, Filter: List = None, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    async def get_account_password_policy(self) -> Dict:
        pass

    async def get_account_summary(self) -> Dict:
        pass

    async def get_context_keys_for_custom_policy(self, PolicyInputList: List) -> Dict:
        pass

    async def get_context_keys_for_principal_policy(self, PolicySourceArn: str, PolicyInputList: List = None) -> Dict:
        pass

    async def get_credential_report(self) -> Dict:
        pass

    async def get_group(self, GroupName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def get_group_policy(self, GroupName: str, PolicyName: str) -> Dict:
        pass

    async def get_instance_profile(self, InstanceProfileName: str) -> Dict:
        pass

    async def get_login_profile(self, UserName: str) -> Dict:
        pass

    async def get_open_id_connect_provider(self, OpenIDConnectProviderArn: str) -> Dict:
        pass

    async def get_organizations_access_report(self, JobId: str, MaxItems: int = None, Marker: str = None, SortKey: str = None) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_policy(self, PolicyArn: str) -> Dict:
        pass

    async def get_policy_version(self, PolicyArn: str, VersionId: str) -> Dict:
        pass

    async def get_role(self, RoleName: str) -> Dict:
        pass

    async def get_role_policy(self, RoleName: str, PolicyName: str) -> Dict:
        pass

    async def get_saml_provider(self, SAMLProviderArn: str) -> Dict:
        pass

    async def get_server_certificate(self, ServerCertificateName: str) -> Dict:
        pass

    async def get_service_last_accessed_details(self, JobId: str, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    async def get_service_last_accessed_details_with_entities(self, JobId: str, ServiceNamespace: str, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    async def get_service_linked_role_deletion_status(self, DeletionTaskId: str) -> Dict:
        pass

    async def get_ssh_public_key(self, UserName: str, SSHPublicKeyId: str, Encoding: str) -> Dict:
        pass

    async def get_user(self, UserName: str = None) -> Dict:
        pass

    async def get_user_policy(self, UserName: str, PolicyName: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def list_access_keys(self, UserName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_account_aliases(self, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_attached_group_policies(self, GroupName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_attached_role_policies(self, RoleName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_attached_user_policies(self, UserName: str, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_entities_for_policy(self, PolicyArn: str, EntityFilter: str = None, PathPrefix: str = None, PolicyUsageFilter: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_group_policies(self, GroupName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_groups(self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_groups_for_user(self, UserName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_instance_profile_tags(self, InstanceProfileName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_instance_profiles(self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_instance_profiles_for_role(self, RoleName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_mfa_device_tags(self, SerialNumber: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_mfa_devices(self, UserName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_open_id_connect_provider_tags(self, OpenIDConnectProviderArn: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_open_id_connect_providers(self) -> Dict:
        pass

    async def list_policies(self, Scope: str = None, OnlyAttached: bool = None, PathPrefix: str = None, PolicyUsageFilter: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_policies_granting_service_access(self, Arn: str, ServiceNamespaces: List, Marker: str = None) -> Dict:
        pass

    async def list_policy_tags(self, PolicyArn: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_policy_versions(self, PolicyArn: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_role_policies(self, RoleName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_role_tags(self, RoleName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_roles(self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_saml_provider_tags(self, SAMLProviderArn: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_saml_providers(self) -> Dict:
        pass

    async def list_server_certificate_tags(self, ServerCertificateName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_server_certificates(self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_service_specific_credentials(self, UserName: str = None, ServiceName: str = None) -> Dict:
        pass

    async def list_signing_certificates(self, UserName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_ssh_public_keys(self, UserName: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_user_policies(self, UserName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_user_tags(self, UserName: str, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_users(self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def list_virtual_mfa_devices(self, AssignmentStatus: str = None, Marker: str = None, MaxItems: int = None) -> Dict:
        pass

    async def put_group_policy(self, GroupName: str, PolicyName: str, PolicyDocument: str) -> None:
        pass

    async def put_role_permissions_boundary(self, RoleName: str, PermissionsBoundary: str) -> None:
        pass

    async def put_role_policy(self, RoleName: str, PolicyName: str, PolicyDocument: str) -> None:
        pass

    async def put_user_permissions_boundary(self, UserName: str, PermissionsBoundary: str) -> None:
        pass

    async def put_user_policy(self, UserName: str, PolicyName: str, PolicyDocument: str) -> None:
        pass

    async def remove_client_id_from_open_id_connect_provider(self, OpenIDConnectProviderArn: str, ClientID: str) -> None:
        pass

    async def remove_role_from_instance_profile(self, InstanceProfileName: str, RoleName: str) -> None:
        pass

    async def remove_user_from_group(self, GroupName: str, UserName: str) -> None:
        pass

    async def reset_service_specific_credential(self, ServiceSpecificCredentialId: str, UserName: str = None) -> Dict:
        pass

    async def resync_mfa_device(self, UserName: str, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        pass

    async def set_default_policy_version(self, PolicyArn: str, VersionId: str) -> None:
        pass

    async def set_security_token_service_preferences(self, GlobalEndpointTokenVersion: str) -> None:
        pass

    async def simulate_custom_policy(self, PolicyInputList: List, ActionNames: List, PermissionsBoundaryPolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    async def simulate_principal_policy(self, PolicySourceArn: str, ActionNames: List, PolicyInputList: List = None, PermissionsBoundaryPolicyInputList: List = None, ResourceArns: List = None, ResourcePolicy: str = None, ResourceOwner: str = None, CallerArn: str = None, ContextEntries: List = None, ResourceHandlingOption: str = None, MaxItems: int = None, Marker: str = None) -> Dict:
        pass

    async def tag_instance_profile(self, InstanceProfileName: str, Tags: List) -> None:
        pass

    async def tag_mfa_device(self, SerialNumber: str, Tags: List) -> None:
        pass

    async def tag_open_id_connect_provider(self, OpenIDConnectProviderArn: str, Tags: List) -> None:
        pass

    async def tag_policy(self, PolicyArn: str, Tags: List) -> None:
        pass

    async def tag_role(self, RoleName: str, Tags: List) -> None:
        pass

    async def tag_saml_provider(self, SAMLProviderArn: str, Tags: List) -> None:
        pass

    async def tag_server_certificate(self, ServerCertificateName: str, Tags: List) -> None:
        pass

    async def tag_user(self, UserName: str, Tags: List) -> None:
        pass

    async def untag_instance_profile(self, InstanceProfileName: str, TagKeys: List) -> None:
        pass

    async def untag_mfa_device(self, SerialNumber: str, TagKeys: List) -> None:
        pass

    async def untag_open_id_connect_provider(self, OpenIDConnectProviderArn: str, TagKeys: List) -> None:
        pass

    async def untag_policy(self, PolicyArn: str, TagKeys: List) -> None:
        pass

    async def untag_role(self, RoleName: str, TagKeys: List) -> None:
        pass

    async def untag_saml_provider(self, SAMLProviderArn: str, TagKeys: List) -> None:
        pass

    async def untag_server_certificate(self, ServerCertificateName: str, TagKeys: List) -> None:
        pass

    async def untag_user(self, UserName: str, TagKeys: List) -> None:
        pass

    async def update_access_key(self, AccessKeyId: str, Status: str, UserName: str = None) -> None:
        pass

    async def update_account_password_policy(self, MinimumPasswordLength: int = None, RequireSymbols: bool = None, RequireNumbers: bool = None, RequireUppercaseCharacters: bool = None, RequireLowercaseCharacters: bool = None, AllowUsersToChangePassword: bool = None, MaxPasswordAge: int = None, PasswordReusePrevention: int = None, HardExpiry: bool = None) -> None:
        pass

    async def update_assume_role_policy(self, RoleName: str, PolicyDocument: str) -> None:
        pass

    async def update_group(self, GroupName: str, NewPath: str = None, NewGroupName: str = None) -> None:
        pass

    async def update_login_profile(self, UserName: str, Password: str = None, PasswordResetRequired: bool = None) -> None:
        pass

    async def update_open_id_connect_provider_thumbprint(self, OpenIDConnectProviderArn: str, ThumbprintList: List) -> None:
        pass

    async def update_role(self, RoleName: str, Description: str = None, MaxSessionDuration: int = None) -> Dict:
        pass

    async def update_role_description(self, RoleName: str, Description: str) -> Dict:
        pass

    async def update_saml_provider(self, SAMLMetadataDocument: str, SAMLProviderArn: str) -> Dict:
        pass

    async def update_server_certificate(self, ServerCertificateName: str, NewPath: str = None, NewServerCertificateName: str = None) -> None:
        pass

    async def update_service_specific_credential(self, ServiceSpecificCredentialId: str, Status: str, UserName: str = None) -> None:
        pass

    async def update_signing_certificate(self, CertificateId: str, Status: str, UserName: str = None) -> None:
        pass

    async def update_ssh_public_key(self, UserName: str, SSHPublicKeyId: str, Status: str) -> None:
        pass

    async def update_user(self, UserName: str, NewPath: str = None, NewUserName: str = None) -> None:
        pass

    async def upload_server_certificate(self, ServerCertificateName: str, CertificateBody: str, PrivateKey: str, Path: str = None, CertificateChain: str = None, Tags: List = None) -> Dict:
        pass

    async def upload_signing_certificate(self, CertificateBody: str, UserName: str = None) -> Dict:
        pass

    async def upload_ssh_public_key(self, UserName: str, SSHPublicKeyBody: str) -> Dict:
        pass

