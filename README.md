# aioboto3 type hints

Forked from https://github.com/terrycain/aioboto3-hints

Many monkey patches were done to make this thing working

## Installation

```bash
git clone https://github.com/Bondifuzz/aioboto3-hints.git
pip install aioboto3-hints
```

## Usage

Regardless of which deployment package you install, you'll still import the same package, `aioboto3_hints`.
Its constituent packages and modules can be used to declare the type of `aioboto3` objects. For instance, everybody's
favorite, S3:

```python
import asyncio
import boto3
from aioboto3_hints.s3 import Client, ServiceResource
from aioboto3_hints.s3.waiter import BucketExists
from aioboto3_hints.s3.paginator import ListObjectsV2

# With type annotations
async def main():
    client: Client = boto3.client('s3')
    await client.create_bucket(Bucket='foo')  # Not only does your IDE knows the name of this method,
                                              # it knows the type of the `Bucket` argument too!
                                              # It also, knows that `Bucket` is required, but `ACL` isn't!

    # Waiters and paginators and defined also...
    waiter: BucketExists = client.get_waiter('bucket_exists')
    await waiter.wait('foo')

    paginator: ListObjectsV2 = client.get_paginator('list_objects_v2')
    async for response in paginator.paginate(Bucket='foo'):
        print(response)

    await client.close()

    # Along with service resources.
    resource: ServiceResource = boto3.resource('s3')
    bucket = resource.Bucket('bar')
    await bucket.create()

    await resource.close()

    # With type comments
    async with boto3.client('s3') as client:  # type: Client
        response = await client.get_object(Bucket='foo', Key='bar')

    # This should also work
    client: Client
    async with boto3.client('s3') as client:
        response = await client.get_object(Bucket='foo', Key='bar')


asyncio.run(main())

# In docstrings
class Foo:
    def __init__(self, client):
        """
        :param client: It's an S3 Client and the IDE is gonna know what it is!
        :type client: Client
        """
        self.client = client

    async def bar(self):
        """
        :rtype: Client
        """
        await self.client.delete_object(Bucket='foo', Key='bar')
        return self.client
```
