<a id="__pageTop"></a>
# gotyai_client.apis.tags.classify_api.ClassifyApi

All URIs are relative to *http://ns3044521.ip-91-121-222.eu:8080/gotyai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explain_many**](#explain_many) | **post** /api2/json/explainMany/{classifierUuid} | Predict a category given the subjet&#x27;s features, with explainability.
[**explain_one**](#explain_one) | **post** /api2/json/explainOne/{classifierUuid} | Predict a category given the subjet&#x27;s features, with explainability.
[**fit_many**](#fit_many) | **post** /api2/json/fitMany/{classifierUuid} | Fit multiple rows in the training sample (up to 100)
[**fit_one**](#fit_one) | **post** /api2/json/fitOne/{classifierUuid} | Fit one row in the training sample.
[**multinomial**](#multinomial) | **get** /api2/json/multinomial/{classifierName} | Get the multinomila classifier by its name.
[**multinomial1**](#multinomial1) | **get** /api2/json/multinomial | Get all the multinomila classifiers.
[**multinomial_create**](#multinomial_create) | **post** /api2/json/multinomialCreate | Create a multinomial classiifer
[**predict_many**](#predict_many) | **post** /api2/json/predictMany/{classifierUuid} | Predict a category given the subjecct&#x27;s features, for up to 100 rows at a time.
[**predict_one**](#predict_one) | **post** /api2/json/predictOne/{classifierUuid} | Predict a category given the subjet&#x27;s features

# **explain_many**
<a id="explain_many"></a>
> BatchPredictOut explain_many(classifier_uuid)

Predict a category given the subjet's features, with explainability.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.batch_predict_in import BatchPredictIn
from gotyai_client.model.batch_predict_out import BatchPredictOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Predict a category given the subjet's features, with explainability.
        api_response = api_instance.explain_many(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->explain_many: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = BatchPredictIn(
        rows=[
            PredictIn(
                x=dict(
                    "key": "key_example",
                ),
            )
        ],
    )
    try:
        # Predict a category given the subjet's features, with explainability.
        api_response = api_instance.explain_many(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->explain_many: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPredictIn**](../../models/BatchPredictIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#explain_many.ApiResponseFor200) | Classifier prediction output, with explainability.
401 | [ApiResponseFor401](#explain_many.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#explain_many.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#explain_many.ApiResponseFor400) | Bad request (ex. too many features)

#### explain_many.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPredictOut**](../../models/BatchPredictOut.md) |  | 


#### explain_many.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### explain_many.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### explain_many.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **explain_one**
<a id="explain_one"></a>
> PredictOut explain_one(classifier_uuid)

Predict a category given the subjet's features, with explainability.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.predict_in import PredictIn
from gotyai_client.model.predict_out import PredictOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Predict a category given the subjet's features, with explainability.
        api_response = api_instance.explain_one(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->explain_one: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = PredictIn(
        x=dict(
            "key": "key_example",
        ),
    )
    try:
        # Predict a category given the subjet's features, with explainability.
        api_response = api_instance.explain_one(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->explain_one: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PredictIn**](../../models/PredictIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#explain_one.ApiResponseFor200) | Classifier prediction output, with explainability.
401 | [ApiResponseFor401](#explain_one.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#explain_one.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#explain_one.ApiResponseFor400) | Bad request (ex. too many features)

#### explain_one.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PredictOut**](../../models/PredictOut.md) |  | 


#### explain_one.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### explain_one.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### explain_one.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fit_many**
<a id="fit_many"></a>
> fit_many(classifier_uuid)

Fit multiple rows in the training sample (up to 100)

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.batch_fit_in import BatchFitIn
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Fit multiple rows in the training sample (up to 100)
        api_response = api_instance.fit_many(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->fit_many: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = BatchFitIn(
        rows=[
            FitIn(
                x=dict(
                    "key": "key_example",
                ),
                y="y_example",
            )
        ],
    )
    try:
        # Fit multiple rows in the training sample (up to 100)
        api_response = api_instance.fit_many(
            path_params=path_params,
            body=body,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->fit_many: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchFitIn**](../../models/BatchFitIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#fit_many.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#fit_many.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#fit_many.ApiResponseFor400) | Bad request (ex. too many features)

#### fit_many.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fit_many.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fit_many.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fit_one**
<a id="fit_one"></a>
> fit_one(classifier_uuid)

Fit one row in the training sample.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.fit_in import FitIn
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Fit one row in the training sample.
        api_response = api_instance.fit_one(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->fit_one: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = FitIn(
        x=dict(
            "key": "key_example",
        ),
        y="y_example",
    )
    try:
        # Fit one row in the training sample.
        api_response = api_instance.fit_one(
            path_params=path_params,
            body=body,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->fit_one: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FitIn**](../../models/FitIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#fit_one.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#fit_one.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#fit_one.ApiResponseFor400) | Bad request (ex. too many features)

#### fit_one.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fit_one.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### fit_one.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **multinomial**
<a id="multinomial"></a>
> ClassifierOut multinomial(classifier_name)

Get the multinomila classifier by its name.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.classifier_out import ClassifierOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierName': "classifierName_example",
    }
    try:
        # Get the multinomila classifier by its name.
        api_response = api_instance.multinomial(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->multinomial: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierName | ClassifierNameSchema | | 

# ClassifierNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#multinomial.ApiResponseFor200) | A genderized name.
401 | [ApiResponseFor401](#multinomial.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#multinomial.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### multinomial.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassifierOut**](../../models/ClassifierOut.md) |  | 


#### multinomial.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### multinomial.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **multinomial1**
<a id="multinomial1"></a>
> ClassifierOut multinomial1()

Get all the multinomila classifiers.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.classifier_out import ClassifierOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all the multinomila classifiers.
        api_response = api_instance.multinomial1()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->multinomial1: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#multinomial1.ApiResponseFor200) | A genderized name.
401 | [ApiResponseFor401](#multinomial1.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#multinomial1.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled

#### multinomial1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassifierOut**](../../models/ClassifierOut.md) |  | 


#### multinomial1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### multinomial1.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **multinomial_create**
<a id="multinomial_create"></a>
> ClassifierOut multinomial_create()

Create a multinomial classiifer

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.classifier_out import ClassifierOut
from gotyai_client.model.classifier_spec_in import ClassifierSpecIn
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only optional values
    body = ClassifierSpecIn(
        categories=[
            "categories_example"
        ],
        classifier_name="classifier_name_example",
    )
    try:
        # Create a multinomial classiifer
        api_response = api_instance.multinomial_create(
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->multinomial_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassifierSpecIn**](../../models/ClassifierSpecIn.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#multinomial_create.ApiResponseFor200) | A classifier.
401 | [ApiResponseFor401](#multinomial_create.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#multinomial_create.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#multinomial_create.ApiResponseFor400) | Bad request (ex. too many names)

#### multinomial_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassifierOut**](../../models/ClassifierOut.md) |  | 


#### multinomial_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### multinomial_create.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### multinomial_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predict_many**
<a id="predict_many"></a>
> BatchPredictOut predict_many(classifier_uuid)

Predict a category given the subjecct's features, for up to 100 rows at a time.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.batch_predict_in import BatchPredictIn
from gotyai_client.model.batch_predict_out import BatchPredictOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Predict a category given the subjecct's features, for up to 100 rows at a time.
        api_response = api_instance.predict_many(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->predict_many: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = BatchPredictIn(
        rows=[
            PredictIn(
                x=dict(
                    "key": "key_example",
                ),
            )
        ],
    )
    try:
        # Predict a category given the subjecct's features, for up to 100 rows at a time.
        api_response = api_instance.predict_many(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->predict_many: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPredictIn**](../../models/BatchPredictIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predict_many.ApiResponseFor200) | Classifier prediction output
401 | [ApiResponseFor401](#predict_many.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#predict_many.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#predict_many.ApiResponseFor400) | Bad request (ex. too many features)

#### predict_many.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchPredictOut**](../../models/BatchPredictOut.md) |  | 


#### predict_many.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### predict_many.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### predict_many.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predict_one**
<a id="predict_one"></a>
> PredictOut predict_one(classifier_uuid)

Predict a category given the subjet's features

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import classify_api
from gotyai_client.model.predict_in import PredictIn
from gotyai_client.model.predict_out import PredictOut
from pprint import pprint
# Defining the host is optional and defaults to http://ns3044521.ip-91-121-222.eu:8080/gotyai
# See configuration.py for a list of all supported configuration parameters.
configuration = gotyai_client.Configuration(
    host = "http://ns3044521.ip-91-121-222.eu:8080/gotyai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with gotyai_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = classify_api.ClassifyApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    try:
        # Predict a category given the subjet's features
        api_response = api_instance.predict_one(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->predict_one: %s\n" % e)

    # example passing only optional values
    path_params = {
        'classifierUuid': "classifierUuid_example",
    }
    body = PredictIn(
        x=dict(
            "key": "key_example",
        ),
    )
    try:
        # Predict a category given the subjet's features
        api_response = api_instance.predict_one(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling ClassifyApi->predict_one: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PredictIn**](../../models/PredictIn.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
classifierUuid | ClassifierUuidSchema | | 

# ClassifierUuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predict_one.ApiResponseFor200) | Classifier prediction output
401 | [ApiResponseFor401](#predict_one.ApiResponseFor401) | Missing or incorrect API Key
403 | [ApiResponseFor403](#predict_one.ApiResponseFor403) | Email not Verified, or API Limit Reached, or API Key Disabled
400 | [ApiResponseFor400](#predict_one.ApiResponseFor400) | Bad request (ex. too many features)

#### predict_one.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PredictOut**](../../models/PredictOut.md) |  | 


#### predict_one.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### predict_one.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### predict_one.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

