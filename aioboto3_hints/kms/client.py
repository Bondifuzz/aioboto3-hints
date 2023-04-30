from datetime import datetime
from typing import Dict, List

from aiobotocore.client import AioBaseClient
from aiobotocore.paginate import AioPaginator
from aiobotocore.waiter import AIOWaiter


class Client(AioBaseClient):
    async def can_paginate(self, operation_name: str = None):
        pass

    async def cancel_key_deletion(self, KeyId: str) -> Dict:
        pass

    async def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        pass

    async def create_alias(self, AliasName: str, TargetKeyId: str):
        pass

    async def create_custom_key_store(self, CustomKeyStoreName: str, CloudHsmClusterId: str, TrustAnchorCertificate: str, KeyStorePassword: str) -> Dict:
        pass

    async def create_grant(self, KeyId: str, GranteePrincipal: str, Operations: List, RetiringPrincipal: str = None, Constraints: Dict = None, GrantTokens: List = None, Name: str = None) -> Dict:
        pass

    async def create_key(self, Policy: str = None, Description: str = None, KeyUsage: str = None, Origin: str = None, CustomKeyStoreId: str = None, BypassPolicyLockoutSafetyCheck: bool = None, Tags: List = None) -> Dict:
        pass

    async def decrypt(self, CiphertextBlob: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    async def delete_alias(self, AliasName: str):
        pass

    async def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        pass

    async def delete_imported_key_material(self, KeyId: str):
        pass

    async def describe_custom_key_stores(self, CustomKeyStoreId: str = None, CustomKeyStoreName: str = None, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def describe_key(self, KeyId: str, GrantTokens: List = None) -> Dict:
        pass

    async def disable_key(self, KeyId: str):
        pass

    async def disable_key_rotation(self, KeyId: str):
        pass

    async def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict:
        pass

    async def enable_key(self, KeyId: str):
        pass

    async def enable_key_rotation(self, KeyId: str):
        pass

    async def encrypt(self, KeyId: str, Plaintext: bytes, EncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    async def generate_data_key(self, KeyId: str, EncryptionContext: Dict = None, NumberOfBytes: int = None, KeySpec: str = None, GrantTokens: List = None) -> Dict:
        pass

    async def generate_data_key_without_plaintext(self, KeyId: str, EncryptionContext: Dict = None, KeySpec: str = None, NumberOfBytes: int = None, GrantTokens: List = None) -> Dict:
        pass

    def generate_presigned_url(self, ClientMethod: str = None, Params: Dict = None, ExpiresIn: int = None, HttpMethod: str = None):
        pass

    async def generate_random(self, NumberOfBytes: int = None, CustomKeyStoreId: str = None) -> Dict:
        pass

    async def get_key_policy(self, KeyId: str, PolicyName: str) -> Dict:
        pass

    async def get_key_rotation_status(self, KeyId: str) -> Dict:
        pass

    def get_paginator(self, operation_name: str = None) -> AioPaginator:
        pass

    async def get_parameters_for_import(self, KeyId: str, WrappingAlgorithm: str, WrappingKeySpec: str) -> Dict:
        pass

    def get_waiter(self, waiter_name: str = None) -> AIOWaiter:
        pass

    async def import_key_material(self, KeyId: str, ImportToken: bytes, EncryptedKeyMaterial: bytes, ValidTo: datetime = None, ExpirationModel: str = None) -> Dict:
        pass

    async def list_aliases(self, KeyId: str = None, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def list_grants(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def list_key_policies(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def list_keys(self, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def list_resource_tags(self, KeyId: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def list_retirable_grants(self, RetiringPrincipal: str, Limit: int = None, Marker: str = None) -> Dict:
        pass

    async def put_key_policy(self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None):
        pass

    async def re_encrypt(self, CiphertextBlob: bytes, DestinationKeyId: str, SourceEncryptionContext: Dict = None, DestinationEncryptionContext: Dict = None, GrantTokens: List = None) -> Dict:
        pass

    async def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None):
        pass

    async def revoke_grant(self, KeyId: str, GrantId: str):
        pass

    async def schedule_key_deletion(self, KeyId: str, PendingWindowInDays: int = None) -> Dict:
        pass

    async def tag_resource(self, KeyId: str, Tags: List):
        pass

    async def untag_resource(self, KeyId: str, TagKeys: List):
        pass

    async def update_alias(self, AliasName: str, TargetKeyId: str):
        pass

    async def update_custom_key_store(self, CustomKeyStoreId: str, NewCustomKeyStoreName: str = None, KeyStorePassword: str = None, CloudHsmClusterId: str = None) -> Dict:
        pass

    async def update_key_description(self, KeyId: str, Description: str):
        pass
