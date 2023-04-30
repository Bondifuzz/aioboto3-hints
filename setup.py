from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='aioboto3-hints',
    version='0.0.1',
    packages=find_packages(),
    url='https://rg-git.corp.dsec.ru/BondiFuzz/internal_toolz/aioboto3-hints.git',
    license='MIT License',
    author='Terry Cain',
    author_email='terry@terrys-home.co.uk',
    description='Type annotations for aioboto3. Adds code completion in IDEs such as PyCharm.',
    package_data={'aioboto3_hints': ['py.typed']},
    long_description=long_description,
    long_description_content_type='text/markdown',
)
