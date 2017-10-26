# dlrnapi-client

This is a Python client and command-line interface for the [DLRN](https://github.com/openstack-packages/DLRN) API.

It has been automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

-   API version: 1.0.0
-   Package version: 1.0.0
-   Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

You can install directly from Github

```sh
pip install git+https://github.com/javierpena/dlrnapi_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/javierpena/dlrnapi_client.git`)

Then import the package:
```python
import dlrnapi_client
```

Or you can run the client directly:

```bash
$ dlrnapi -h
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dlrnapi_client
```

Or you can run the client directly:

```bash
$ dlrnapi -h
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import dlrnapi_client
from dlrnapi_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = dlrnapi_client.DefaultApi()
params = dlrnapi_client.Params() # Params | The JSON params to post

try:
    api_response = api_instance.api_last_tested_repo_get(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_last_tested_repo_get: %s\n" % e)

```

## Documentation for command-line
-   [dlrnapi](docs/command-line.md)

## Documentation for API Endpoints

All URIs are relative to <http://127.0.0.1:5000>

Class |Method |HTTP request |Description
------------ | ------------- | ------------- | -------------
*DefaultApi*|[**api_last_tested_repo_get**](docs/DefaultApi.md#api_last_tested_repo_get)|**GET** /api/last_tested_repo|
*DefaultApi*|[**api_last_tested_repo_post**](docs/DefaultApi.md#api_last_tested_repo_post)|**POST** /api/last_tested_repo|
*DefaultApi*|[**api_promote_post**](docs/DefaultApi.md#api_promote_post)|**POST** /api/promote|
*DefaultApi*|[**api_promotions_get**](docs/DefaultApi.md#api_promotions_get)|**POST** /api/promotions|
*DefaultApi*|[**api_remote_import_post**](docs/DefaultApi.md#api_remote_import_post)|**POST** /api/remote/import|
*DefaultApi*|[**api_repo_status_get**](docs/DefaultApi.md#api_repo_status_get)|**GET** /api/repo_status|
*DefaultApi*|[**api_report_result_post**](docs/DefaultApi.md#api_report_result_post)|**POST**/api/report_result|


## Documentation For Models

-   [CIVote](docs/CIVote.md)
-   [Import](docs/ModelImport.md)
-   [Params](docs/Params.md)
-   [Params1](docs/Params1.md)
-   [Params2](docs/Params2.md)
-   [Params3](docs/Params3.md)
-   [Promotion](docs/Promotion.md)
-   [Repo](docs/Repo.md)


## Documentation For Authorization


## basicAuth

-   **Type**: HTTP basic authentication


## Author

Javier Peña (jpena@redhat.com)


This is just a test
