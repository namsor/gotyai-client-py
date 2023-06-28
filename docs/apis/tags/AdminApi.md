<a id="__pageTop"></a>
# gotyai_client.apis.tags.admin_api.AdminApi

All URIs are relative to *http://ns3044521.ip-91-121-222.eu:8080/gotyai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abuse_name_patterns**](#abuse_name_patterns) | **get** /api2/json/nameBlacklistPatterns | List blacklist name pattern.
[**add_credits**](#add_credits) | **get** /api2/json/addCredits/{apiKey}/{usageCredits}/{userMessage} | Add usage credits to an API Key.
[**api_key_info**](#api_key_info) | **get** /api2/json/apiKeyInfo | Read API Key info.
[**api_usage**](#api_usage) | **get** /api2/json/apiUsage | Print current API usage.
[**api_usage_history**](#api_usage_history) | **get** /api2/json/apiUsageHistory | Print historical API usage.
[**api_usage_history_aggregate**](#api_usage_history_aggregate) | **get** /api2/json/apiUsageHistoryAggregate | Print historical API usage (in an aggregated view, by service, by day/hour/min).
[**available_plans**](#available_plans) | **get** /api2/json/availablePlans | List all available plans in the default currency (usd).
[**available_plans1**](#available_plans1) | **get** /api2/json/availablePlans/{token} | List all available plans in the user&#x27;s preferred currency.
[**billing_currencies**](#billing_currencies) | **get** /api2/json/billingCurrencies | List possible currency options for billing (USD, EUR, GBP, ...)
[**billing_history**](#billing_history) | **get** /api2/json/billingHistory/{token} | Read the history billing information (invoices paid via Stripe or manually).
[**billing_info**](#billing_info) | **get** /api2/json/billingInfo/{token} | Read the billing information (company name, address, phone, vat ID)
[**charge_new**](#charge_new) | **get** /api2/json/chargeNew/{stripeToken}/{stripeEmail} | Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.
[**corporate_key**](#corporate_key) | **get** /api2/json/corporateKey/{apiKey}/{corporate} | Setting an API Key to a corporate status.
[**count_spam_non_spam**](#count_spam_non_spam) | **get** /api2/json/countSpamNonSpam/{durationMillis} | Get email spam statistics over custom duration.
[**count_spam_non_spam1**](#count_spam_non_spam1) | **get** /api2/json/countSpamNonSpam | Email spam statistics.
[**debug_level**](#debug_level) | **get** /api2/json/debugLevel/{logger}/{level} | Update debug level for a classifier
[**disable**](#disable) | **get** /api2/json/disable/{source}/{disabled} | Activate/deactivate an API Key.
[**email_blacklist_pattern_add**](#email_blacklist_pattern_add) | **get** /api2/json/emailBlacklistPatternAdd/{pattern} | Add blacklist email pattern.
[**email_blacklist_pattern_remove**](#email_blacklist_pattern_remove) | **get** /api2/json/emailBlacklistPatternRemove/{pattern} | Remove blacklist email pattern.
[**email_blacklist_patterns**](#email_blacklist_patterns) | **get** /api2/json/emailBlacklistPatterns | List all blacklist email patterns.
[**explainability**](#explainability) | **get** /api2/json/explainability/{source}/{explainable} | Activate/deactivate explainability for a source.
[**flush**](#flush) | **get** /api2/json/flush | Flush counters.
[**gotya_counter**](#gotya_counter) | **get** /api2/json/namsorCounter | Get the overall API counter
[**invalidate_cache**](#invalidate_cache) | **get** /api2/json/invalidateCache | Invalidate system caches.
[**ip_addresses_blacklist_candidates**](#ip_addresses_blacklist_candidates) | **get** /api2/json/ipAddressesBlacklistCandidates | List IP blacklist candidates.
[**name_blacklist_pattern_add**](#name_blacklist_pattern_add) | **get** /api2/json/nameBlacklistPatternAdd/{pattern} | Add blacklist name pattern.
[**name_blacklist_pattern_remove**](#name_blacklist_pattern_remove) | **get** /api2/json/nameBlacklistPatternRemove/{pattern} | Remove blacklist name pattern.
[**payment_info**](#payment_info) | **get** /api2/json/paymentInfo/{token} | Get the Stripe payment information associated with the current google auth session token.
[**procure_key**](#procure_key) | **get** /api2/json/procureKey/{token}/{recaptchav2} | Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.
[**procure_key1**](#procure_key1) | **get** /api2/json/procureKey/{token} | [compatibility] Retrieve the user&#x27;s API Key, based on an auth token. Keep your API Key secret.
[**remove_payment**](#remove_payment) | **get** /api2/json/removePayment/{sourceId}/{token} | Remove Stripe card associated with the current google auth session token.
[**remove_user_account**](#remove_user_account) | **get** /api2/json/removeUserAccount/{token} | Remove the user account.
[**remove_user_account_on_behalf**](#remove_user_account_on_behalf) | **get** /api2/json/removeUserAccountOnBehalf/{apiKey} | Remove (on behalf) a user account.
[**resend_key**](#resend_key) | **get** /api2/json/resendKey/{token}/{recaptchav2} | Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.
[**retrieve_key**](#retrieve_key) | **get** /api2/json/retrieveKey/{token} | Retrieve the user&#x27;s API Key, based on an auth token. Keep your API Key secret.
[**shutdown**](#shutdown) | **get** /api2/json/shutdown | Stop learning and shutdown system.
[**signups**](#signups) | **get** /api2/json/signups/{ipAddress} | List userID signups by IP address.
[**software_version**](#software_version) | **get** /api2/json/softwareVersion | Get the current software version
[**spamsurge**](#spamsurge) | **get** /api2/json/spamsurge/{blockDisposableEmails} | Activate/deactivate blocking of disposable emails in case of spam surge.
[**stats**](#stats) | **get** /api2/json/stats | Print basic system statistics.
[**subscribe_plan**](#subscribe_plan) | **get** /api2/json/subscribePlan/{planName}/{token} | Subscribe to a give API plan, using the user&#x27;s preferred or default currency.
[**subscribe_plan_on_behalf**](#subscribe_plan_on_behalf) | **get** /api2/json/subscribePlanOnBehalf/{planName}/{apiKey} | Subscribe to a give API plan, using the user&#x27;s preferred or default currency (admin only).
[**switch_default_api_key_active**](#switch_default_api_key_active) | **get** /api2/json/switchDefaultAPIKeyActive/{defaultBlocked} | Switch defaullt API Key as blocked (need email verif) or active.
[**update_billing_info**](#update_billing_info) | **post** /api2/json/updateBillingInfo/{token} | Sets or update the billing information (company name, address, phone, vat ID)
[**update_limit**](#update_limit) | **get** /api2/json/updateLimit/{usageLimit}/{hardOrSoft}/{token} | Modifies the hard/soft limit on the API plan&#x27;s overages (default is 0$ soft limit).
[**update_payment_default**](#update_payment_default) | **get** /api2/json/updatePaymentDefault/{defautSourceId}/{token} | Update the default Stripe card associated with the current google auth session token.
[**update_user_info**](#update_user_info) | **get** /api2/json/updateUserInfo/{email}/{displayName}/{token} | Sets or update the user email and name information
[**user_info**](#user_info) | **get** /api2/json/userInfo/{token} | Get the user profile associated with the current google auth session token.
[**verify_email**](#verify_email) | **get** /api2/json/verifyEmail/{emailToken} | Verifies an email, based on token sent to that email
[**verify_remove_email**](#verify_remove_email) | **get** /api2/json/verifyRemoveEmail/{emailToken} | Verifies an email, based on token sent to that email

# **abuse_name_patterns**
<a id="abuse_name_patterns"></a>
> abuse_name_patterns()

List blacklist name pattern.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List blacklist name pattern.
        api_response = api_instance.abuse_name_patterns()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->abuse_name_patterns: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#abuse_name_patterns.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#abuse_name_patterns.ApiResponseFor401) | Missing or incorrect API Key

#### abuse_name_patterns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### abuse_name_patterns.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_credits**
<a id="add_credits"></a>
> APIPeriodUsageOut add_credits(api_keyusage_creditsuser_message)

Add usage credits to an API Key.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_period_usage_out import APIPeriodUsageOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'apiKey': "apiKey_example",
        'usageCredits': 1,
        'userMessage': "userMessage_example",
    }
    try:
        # Add usage credits to an API Key.
        api_response = api_instance.add_credits(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->add_credits: %s\n" % e)
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
apiKey | ApiKeySchema | | 
usageCredits | UsageCreditsSchema | | 
userMessage | UserMessageSchema | | 

# ApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UsageCreditsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# UserMessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_credits.ApiResponseFor200) | Estimate new after applying credits.
401 | [ApiResponseFor401](#add_credits.ApiResponseFor401) | Missing or incorrect API Key

#### add_credits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPeriodUsageOut**](../../models/APIPeriodUsageOut.md) |  | 


#### add_credits.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_key_info**
<a id="api_key_info"></a>
> APIKeyOut api_key_info()

Read API Key info.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Read API Key info.
        api_response = api_instance.api_key_info()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->api_key_info: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_key_info.ApiResponseFor200) | Read API Key (uncached, i.e. DB read)
401 | [ApiResponseFor401](#api_key_info.ApiResponseFor401) | Missing or incorrect API Key

#### api_key_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### api_key_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage**
<a id="api_usage"></a>
> APIPeriodUsageOut api_usage()

Print current API usage.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_period_usage_out import APIPeriodUsageOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print current API usage.
        api_response = api_instance.api_usage()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage.ApiResponseFor200) | Print current API usage.
401 | [ApiResponseFor401](#api_usage.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPeriodUsageOut**](../../models/APIPeriodUsageOut.md) |  | 


#### api_usage.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage_history**
<a id="api_usage_history"></a>
> APIUsageHistoryOut api_usage_history()

Print historical API usage.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_usage_history_out import APIUsageHistoryOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print historical API usage.
        api_response = api_instance.api_usage_history()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage_history: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage_history.ApiResponseFor200) | Print historical API usage (NB. new output format form v2.0.15)
401 | [ApiResponseFor401](#api_usage_history.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIUsageHistoryOut**](../../models/APIUsageHistoryOut.md) |  | 


#### api_usage_history.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_usage_history_aggregate**
<a id="api_usage_history_aggregate"></a>
> APIUsageAggregatedOut api_usage_history_aggregate()

Print historical API usage (in an aggregated view, by service, by day/hour/min).

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_usage_aggregated_out import APIUsageAggregatedOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print historical API usage (in an aggregated view, by service, by day/hour/min).
        api_response = api_instance.api_usage_history_aggregate()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->api_usage_history_aggregate: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_usage_history_aggregate.ApiResponseFor200) | Print historical API usage.
401 | [ApiResponseFor401](#api_usage_history_aggregate.ApiResponseFor401) | Missing or incorrect API Key

#### api_usage_history_aggregate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIUsageAggregatedOut**](../../models/APIUsageAggregatedOut.md) |  | 


#### api_usage_history_aggregate.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **available_plans**
<a id="available_plans"></a>
> APIPlansOut available_plans()

List all available plans in the default currency (usd).

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plans_out import APIPlansOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all available plans in the default currency (usd).
        api_response = api_instance.available_plans()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->available_plans: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#available_plans.ApiResponseFor200) | Available plans
401 | [ApiResponseFor401](#available_plans.ApiResponseFor401) | Missing or incorrect token

#### available_plans.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlansOut**](../../models/APIPlansOut.md) |  | 


#### available_plans.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **available_plans1**
<a id="available_plans1"></a>
> APIPlansOut available_plans1(token)

List all available plans in the user's preferred currency.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plans_out import APIPlansOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # List all available plans in the user's preferred currency.
        api_response = api_instance.available_plans1(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->available_plans1: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#available_plans1.ApiResponseFor200) | Available plans
401 | [ApiResponseFor401](#available_plans1.ApiResponseFor401) | Missing or incorrect token

#### available_plans1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlansOut**](../../models/APIPlansOut.md) |  | 


#### available_plans1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **billing_currencies**
<a id="billing_currencies"></a>
> CurrenciesOut billing_currencies()

List possible currency options for billing (USD, EUR, GBP, ...)

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.currencies_out import CurrenciesOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List possible currency options for billing (USD, EUR, GBP, ...)
        api_response = api_instance.billing_currencies()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->billing_currencies: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#billing_currencies.ApiResponseFor200) | The supported billing currencies.
401 | [ApiResponseFor401](#billing_currencies.ApiResponseFor401) | Missing or incorrect token

#### billing_currencies.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CurrenciesOut**](../../models/CurrenciesOut.md) |  | 


#### billing_currencies.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **billing_history**
<a id="billing_history"></a>
> BillingHistoryOut billing_history(token)

Read the history billing information (invoices paid via Stripe or manually).

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.billing_history_out import BillingHistoryOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Read the history billing information (invoices paid via Stripe or manually).
        api_response = api_instance.billing_history(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->billing_history: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#billing_history.ApiResponseFor200) | The billing history
401 | [ApiResponseFor401](#billing_history.ApiResponseFor401) | Missing or incorrect token

#### billing_history.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BillingHistoryOut**](../../models/BillingHistoryOut.md) |  | 


#### billing_history.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **billing_info**
<a id="billing_info"></a>
> BillingInfoInOut billing_info(token)

Read the billing information (company name, address, phone, vat ID)

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.billing_info_in_out import BillingInfoInOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Read the billing information (company name, address, phone, vat ID)
        api_response = api_instance.billing_info(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->billing_info: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#billing_info.ApiResponseFor200) | The current billing info
401 | [ApiResponseFor401](#billing_info.ApiResponseFor401) | Missing or incorrect token

#### billing_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BillingInfoInOut**](../../models/BillingInfoInOut.md) |  | 


#### billing_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **charge_new**
<a id="charge_new"></a>
> charge_new(stripe_tokenstripe_email)

Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.stripe_customer_out import StripeCustomerOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'stripeToken': "stripeToken_example",
        'stripeEmail': "stripeEmail_example",
    }
    try:
        # Create a Stripe Customer V2, based on a payment card token (from secure StripeJS) and email.
        api_response = api_instance.charge_new(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->charge_new: %s\n" % e)
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
stripeToken | StripeTokenSchema | | 
stripeEmail | StripeEmailSchema | | 

# StripeTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StripeEmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#charge_new.ApiResponseFor401) | Missing or incorrect email or payment token, or issue with payment card.

#### charge_new.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StripeCustomerOut**](../../models/StripeCustomerOut.md) |  | 


### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **corporate_key**
<a id="corporate_key"></a>
> corporate_key(api_keycorporate)

Setting an API Key to a corporate status.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'apiKey': "apiKey_example",
        'corporate': True,
    }
    try:
        # Setting an API Key to a corporate status.
        api_response = api_instance.corporate_key(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->corporate_key: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
apiKey | ApiKeySchema | | 
corporate | CorporateSchema | | 

# ApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CorporateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#corporate_key.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#corporate_key.ApiResponseFor401) | Missing or incorrect API Key

#### corporate_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### corporate_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **count_spam_non_spam**
<a id="count_spam_non_spam"></a>
> SpamStatsOut count_spam_non_spam(duration_millis)

Get email spam statistics over custom duration.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.spam_stats_out import SpamStatsOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'durationMillis': 1,
    }
    try:
        # Get email spam statistics over custom duration.
        api_response = api_instance.count_spam_non_spam(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->count_spam_non_spam: %s\n" % e)
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
durationMillis | DurationMillisSchema | | 

# DurationMillisSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_spam_non_spam.ApiResponseFor200) | Get email spam statistics over custom duration.
401 | [ApiResponseFor401](#count_spam_non_spam.ApiResponseFor401) | Missing or incorrect API Key

#### count_spam_non_spam.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SpamStatsOut**](../../models/SpamStatsOut.md) |  | 


#### count_spam_non_spam.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **count_spam_non_spam1**
<a id="count_spam_non_spam1"></a>
> SpamStatsOut count_spam_non_spam1()

Email spam statistics.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.spam_stats_out import SpamStatsOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Email spam statistics.
        api_response = api_instance.count_spam_non_spam1()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->count_spam_non_spam1: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_spam_non_spam1.ApiResponseFor200) | Get email spam statistics.
401 | [ApiResponseFor401](#count_spam_non_spam1.ApiResponseFor401) | Missing or incorrect API Key

#### count_spam_non_spam1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SpamStatsOut**](../../models/SpamStatsOut.md) |  | 


#### count_spam_non_spam1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **debug_level**
<a id="debug_level"></a>
> debug_level(loggerlevel)

Update debug level for a classifier

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'logger': "logger_example",
        'level': "level_example",
    }
    try:
        # Update debug level for a classifier
        api_response = api_instance.debug_level(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->debug_level: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
logger | LoggerSchema | | 
level | LevelSchema | | 

# LoggerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#debug_level.ApiResponseFor200) | Updated debug level
401 | [ApiResponseFor401](#debug_level.ApiResponseFor401) | Missing or incorrect API Key

#### debug_level.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### debug_level.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **disable**
<a id="disable"></a>
> disable(sourcedisabled)

Activate/deactivate an API Key.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'disabled': True,
    }
    try:
        # Activate/deactivate an API Key.
        api_response = api_instance.disable(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->disable: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | 
disabled | DisabledSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DisabledSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#disable.ApiResponseFor200) | Disabled the API Key.
401 | [ApiResponseFor401](#disable.ApiResponseFor401) | Missing or incorrect API Key

#### disable.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### disable.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **email_blacklist_pattern_add**
<a id="email_blacklist_pattern_add"></a>
> email_blacklist_pattern_add(pattern)

Add blacklist email pattern.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pattern': "pattern_example",
    }
    try:
        # Add blacklist email pattern.
        api_response = api_instance.email_blacklist_pattern_add(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->email_blacklist_pattern_add: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pattern | PatternSchema | | 

# PatternSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#email_blacklist_pattern_add.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#email_blacklist_pattern_add.ApiResponseFor401) | Missing or incorrect API Key

#### email_blacklist_pattern_add.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### email_blacklist_pattern_add.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **email_blacklist_pattern_remove**
<a id="email_blacklist_pattern_remove"></a>
> email_blacklist_pattern_remove(pattern)

Remove blacklist email pattern.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pattern': "pattern_example",
    }
    try:
        # Remove blacklist email pattern.
        api_response = api_instance.email_blacklist_pattern_remove(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->email_blacklist_pattern_remove: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pattern | PatternSchema | | 

# PatternSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#email_blacklist_pattern_remove.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#email_blacklist_pattern_remove.ApiResponseFor401) | Missing or incorrect API Key

#### email_blacklist_pattern_remove.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### email_blacklist_pattern_remove.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **email_blacklist_patterns**
<a id="email_blacklist_patterns"></a>
> email_blacklist_patterns()

List all blacklist email patterns.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all blacklist email patterns.
        api_response = api_instance.email_blacklist_patterns()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->email_blacklist_patterns: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#email_blacklist_patterns.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#email_blacklist_patterns.ApiResponseFor401) | Missing or incorrect API Key

#### email_blacklist_patterns.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### email_blacklist_patterns.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **explainability**
<a id="explainability"></a>
> explainability(sourceexplainable)

Activate/deactivate explainability for a source.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'source': "source_example",
        'explainable': True,
    }
    try:
        # Activate/deactivate explainability for a source.
        api_response = api_instance.explainability(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->explainability: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
source | SourceSchema | | 
explainable | ExplainableSchema | | 

# SourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ExplainableSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#explainability.ApiResponseFor200) | Explainability of a source.
401 | [ApiResponseFor401](#explainability.ApiResponseFor401) | Missing or incorrect API Key

#### explainability.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### explainability.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **flush**
<a id="flush"></a>
> flush()

Flush counters.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Flush counters.
        api_response = api_instance.flush()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->flush: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#flush.ApiResponseFor200) | Flush API Key caches.
401 | [ApiResponseFor401](#flush.ApiResponseFor401) | Missing or incorrect API Key

#### flush.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### flush.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **gotya_counter**
<a id="gotya_counter"></a>
> GotyaCounterOut gotya_counter()

Get the overall API counter

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.gotya_counter_out import GotyaCounterOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the overall API counter
        api_response = api_instance.gotya_counter()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->gotya_counter: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#gotya_counter.ApiResponseFor200) | The overall API counter
401 | [ApiResponseFor401](#gotya_counter.ApiResponseFor401) | Missing or incorrect token

#### gotya_counter.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GotyaCounterOut**](../../models/GotyaCounterOut.md) |  | 


#### gotya_counter.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **invalidate_cache**
<a id="invalidate_cache"></a>
> invalidate_cache()

Invalidate system caches.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Invalidate system caches.
        api_response = api_instance.invalidate_cache()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->invalidate_cache: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#invalidate_cache.ApiResponseFor200) | Clear caches.
401 | [ApiResponseFor401](#invalidate_cache.ApiResponseFor401) | Missing or incorrect API Key

#### invalidate_cache.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### invalidate_cache.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **ip_addresses_blacklist_candidates**
<a id="ip_addresses_blacklist_candidates"></a>
> ip_addresses_blacklist_candidates()

List IP blacklist candidates.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IP blacklist candidates.
        api_response = api_instance.ip_addresses_blacklist_candidates()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->ip_addresses_blacklist_candidates: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ip_addresses_blacklist_candidates.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#ip_addresses_blacklist_candidates.ApiResponseFor401) | Missing or incorrect API Key

#### ip_addresses_blacklist_candidates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ip_addresses_blacklist_candidates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **name_blacklist_pattern_add**
<a id="name_blacklist_pattern_add"></a>
> name_blacklist_pattern_add(pattern)

Add blacklist name pattern.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pattern': "pattern_example",
    }
    try:
        # Add blacklist name pattern.
        api_response = api_instance.name_blacklist_pattern_add(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->name_blacklist_pattern_add: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pattern | PatternSchema | | 

# PatternSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#name_blacklist_pattern_add.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#name_blacklist_pattern_add.ApiResponseFor401) | Missing or incorrect API Key

#### name_blacklist_pattern_add.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### name_blacklist_pattern_add.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **name_blacklist_pattern_remove**
<a id="name_blacklist_pattern_remove"></a>
> name_blacklist_pattern_remove(pattern)

Remove blacklist name pattern.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pattern': "pattern_example",
    }
    try:
        # Remove blacklist name pattern.
        api_response = api_instance.name_blacklist_pattern_remove(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->name_blacklist_pattern_remove: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pattern | PatternSchema | | 

# PatternSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#name_blacklist_pattern_remove.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#name_blacklist_pattern_remove.ApiResponseFor401) | Missing or incorrect API Key

#### name_blacklist_pattern_remove.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### name_blacklist_pattern_remove.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **payment_info**
<a id="payment_info"></a>
> StripeCustomerOut payment_info(token)

Get the Stripe payment information associated with the current google auth session token.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.stripe_customer_out import StripeCustomerOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Get the Stripe payment information associated with the current google auth session token.
        api_response = api_instance.payment_info(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->payment_info: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#payment_info.ApiResponseFor200) | A stripe customer info
401 | [ApiResponseFor401](#payment_info.ApiResponseFor401) | Missing or incorrect token

#### payment_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StripeCustomerOut**](../../models/StripeCustomerOut.md) |  | 


#### payment_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **procure_key**
<a id="procure_key"></a>
> APIKeyOut procure_key(tokenrecaptchav2)

Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
        'recaptchav2': "recaptchav2_example",
    }
    try:
        # Procure an API Key (sent via Email), based on an auth token and a recaptcha. Keep your API Key secret.
        api_response = api_instance.procure_key(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->procure_key: %s\n" % e)
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
token | TokenSchema | | 
recaptchav2 | Recaptchav2Schema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Recaptchav2Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#procure_key.ApiResponseFor200) | An API Key
401 | [ApiResponseFor401](#procure_key.ApiResponseFor401) | Missing or incorrect token

#### procure_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### procure_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **procure_key1**
<a id="procure_key1"></a>
> APIKeyOut procure_key1(token)

[compatibility] Retrieve the user's API Key, based on an auth token. Keep your API Key secret.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # [compatibility] Retrieve the user's API Key, based on an auth token. Keep your API Key secret.
        api_response = api_instance.procure_key1(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->procure_key1: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#procure_key1.ApiResponseFor200) | An API Key
401 | [ApiResponseFor401](#procure_key1.ApiResponseFor401) | Missing or incorrect token

#### procure_key1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### procure_key1.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_payment**
<a id="remove_payment"></a>
> StripeCustomerOut remove_payment(source_idtoken)

Remove Stripe card associated with the current google auth session token.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.stripe_customer_out import StripeCustomerOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'sourceId': "sourceId_example",
        'token': "token_example",
    }
    try:
        # Remove Stripe card associated with the current google auth session token.
        api_response = api_instance.remove_payment(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->remove_payment: %s\n" % e)
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
sourceId | SourceIdSchema | | 
token | TokenSchema | | 

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_payment.ApiResponseFor200) | A stripe customer info
401 | [ApiResponseFor401](#remove_payment.ApiResponseFor401) | Missing or incorrect token

#### remove_payment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StripeCustomerOut**](../../models/StripeCustomerOut.md) |  | 


#### remove_payment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_user_account**
<a id="remove_user_account"></a>
> APIPlanSubscriptionOut remove_user_account(token)

Remove the user account.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plan_subscription_out import APIPlanSubscriptionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Remove the user account.
        api_response = api_instance.remove_user_account(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->remove_user_account: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_user_account.ApiResponseFor200) | An API subscription
401 | [ApiResponseFor401](#remove_user_account.ApiResponseFor401) | Missing or incorrect token

#### remove_user_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlanSubscriptionOut**](../../models/APIPlanSubscriptionOut.md) |  | 


#### remove_user_account.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_user_account_on_behalf**
<a id="remove_user_account_on_behalf"></a>
> APIPlanSubscriptionOut remove_user_account_on_behalf(api_key)

Remove (on behalf) a user account.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plan_subscription_out import APIPlanSubscriptionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'apiKey': "apiKey_example",
    }
    try:
        # Remove (on behalf) a user account.
        api_response = api_instance.remove_user_account_on_behalf(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->remove_user_account_on_behalf: %s\n" % e)
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
apiKey | ApiKeySchema | | 

# ApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_user_account_on_behalf.ApiResponseFor200) | An API subscription
401 | [ApiResponseFor401](#remove_user_account_on_behalf.ApiResponseFor401) | Missing or incorrect token

#### remove_user_account_on_behalf.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlanSubscriptionOut**](../../models/APIPlanSubscriptionOut.md) |  | 


#### remove_user_account_on_behalf.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **resend_key**
<a id="resend_key"></a>
> APIKeyOut resend_key(tokenrecaptchav2)

Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
        'recaptchav2': "recaptchav2_example",
    }
    try:
        # Resend an API Key (sent via Email), based on an auth token and a recaptcha as well as verification link. Keep your API Key secret.
        api_response = api_instance.resend_key(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->resend_key: %s\n" % e)
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
token | TokenSchema | | 
recaptchav2 | Recaptchav2Schema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Recaptchav2Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#resend_key.ApiResponseFor200) | An API Key
401 | [ApiResponseFor401](#resend_key.ApiResponseFor401) | Missing or incorrect token

#### resend_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### resend_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **retrieve_key**
<a id="retrieve_key"></a>
> APIKeyOut retrieve_key(token)

Retrieve the user's API Key, based on an auth token. Keep your API Key secret.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_key_out import APIKeyOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Retrieve the user's API Key, based on an auth token. Keep your API Key secret.
        api_response = api_instance.retrieve_key(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->retrieve_key: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_key.ApiResponseFor200) | An API Key
401 | [ApiResponseFor401](#retrieve_key.ApiResponseFor401) | Missing or incorrect token

#### retrieve_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIKeyOut**](../../models/APIKeyOut.md) |  | 


#### retrieve_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **shutdown**
<a id="shutdown"></a>
> shutdown()

Stop learning and shutdown system.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Stop learning and shutdown system.
        api_response = api_instance.shutdown()
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->shutdown: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#shutdown.ApiResponseFor200) | Shutdown AI.
401 | [ApiResponseFor401](#shutdown.ApiResponseFor401) | Missing or incorrect API Key

#### shutdown.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### shutdown.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **signups**
<a id="signups"></a>
> signups(ip_address)

List userID signups by IP address.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ipAddress': "ipAddress_example",
    }
    try:
        # List userID signups by IP address.
        api_response = api_instance.signups(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->signups: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ipAddress | IpAddressSchema | | 

# IpAddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#signups.ApiResponseFor200) | API Key set to a corporate status.
401 | [ApiResponseFor401](#signups.ApiResponseFor401) | Missing or incorrect API Key

#### signups.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### signups.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **software_version**
<a id="software_version"></a>
> SoftwareVersionOut software_version()

Get the current software version

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.software_version_out import SoftwareVersionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current software version
        api_response = api_instance.software_version()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->software_version: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#software_version.ApiResponseFor200) | The current software version
401 | [ApiResponseFor401](#software_version.ApiResponseFor401) | Missing or incorrect token

#### software_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SoftwareVersionOut**](../../models/SoftwareVersionOut.md) |  | 


#### software_version.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **spamsurge**
<a id="spamsurge"></a>
> spamsurge(block_disposable_emails)

Activate/deactivate blocking of disposable emails in case of spam surge.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'blockDisposableEmails': True,
    }
    try:
        # Activate/deactivate blocking of disposable emails in case of spam surge.
        api_response = api_instance.spamsurge(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->spamsurge: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
blockDisposableEmails | BlockDisposableEmailsSchema | | 

# BlockDisposableEmailsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#spamsurge.ApiResponseFor200) | Set blocking during spam surge.
401 | [ApiResponseFor401](#spamsurge.ApiResponseFor401) | Missing or incorrect API Key

#### spamsurge.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### spamsurge.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **stats**
<a id="stats"></a>
> SystemMetricsOut stats()

Print basic system statistics.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.system_metrics_out import SystemMetricsOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Print basic system statistics.
        api_response = api_instance.stats()
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->stats: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#stats.ApiResponseFor200) | Current system status.
401 | [ApiResponseFor401](#stats.ApiResponseFor401) | Missing or incorrect API Key

#### stats.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SystemMetricsOut**](../../models/SystemMetricsOut.md) |  | 


#### stats.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subscribe_plan**
<a id="subscribe_plan"></a>
> APIPlanSubscriptionOut subscribe_plan(plan_nametoken)

Subscribe to a give API plan, using the user's preferred or default currency.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plan_subscription_out import APIPlanSubscriptionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'planName': "planName_example",
        'token': "token_example",
    }
    try:
        # Subscribe to a give API plan, using the user's preferred or default currency.
        api_response = api_instance.subscribe_plan(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->subscribe_plan: %s\n" % e)
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
planName | PlanNameSchema | | 
token | TokenSchema | | 

# PlanNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subscribe_plan.ApiResponseFor200) | An API subscription
401 | [ApiResponseFor401](#subscribe_plan.ApiResponseFor401) | Missing or incorrect token

#### subscribe_plan.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlanSubscriptionOut**](../../models/APIPlanSubscriptionOut.md) |  | 


#### subscribe_plan.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **subscribe_plan_on_behalf**
<a id="subscribe_plan_on_behalf"></a>
> APIPlanSubscriptionOut subscribe_plan_on_behalf(plan_nameapi_key)

Subscribe to a give API plan, using the user's preferred or default currency (admin only).

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_plan_subscription_out import APIPlanSubscriptionOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'planName': "planName_example",
        'apiKey': "apiKey_example",
    }
    try:
        # Subscribe to a give API plan, using the user's preferred or default currency (admin only).
        api_response = api_instance.subscribe_plan_on_behalf(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->subscribe_plan_on_behalf: %s\n" % e)
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
planName | PlanNameSchema | | 
apiKey | ApiKeySchema | | 

# PlanNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#subscribe_plan_on_behalf.ApiResponseFor200) | An API subscription
401 | [ApiResponseFor401](#subscribe_plan_on_behalf.ApiResponseFor401) | Missing or incorrect token

#### subscribe_plan_on_behalf.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPlanSubscriptionOut**](../../models/APIPlanSubscriptionOut.md) |  | 


#### subscribe_plan_on_behalf.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **switch_default_api_key_active**
<a id="switch_default_api_key_active"></a>
> switch_default_api_key_active(default_blocked)

Switch defaullt API Key as blocked (need email verif) or active.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'defaultBlocked': True,
    }
    try:
        # Switch defaullt API Key as blocked (need email verif) or active.
        api_response = api_instance.switch_default_api_key_active(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->switch_default_api_key_active: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
defaultBlocked | DefaultBlockedSchema | | 

# DefaultBlockedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#switch_default_api_key_active.ApiResponseFor200) | API Key default switched.
401 | [ApiResponseFor401](#switch_default_api_key_active.ApiResponseFor401) | Missing or incorrect API Key

#### switch_default_api_key_active.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### switch_default_api_key_active.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_billing_info**
<a id="update_billing_info"></a>
> BillingInfoInOut update_billing_info(token)

Sets or update the billing information (company name, address, phone, vat ID)

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.billing_info_in_out import BillingInfoInOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Sets or update the billing information (company name, address, phone, vat ID)
        api_response = api_instance.update_billing_info(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->update_billing_info: %s\n" % e)

    # example passing only optional values
    path_params = {
        'token': "token_example",
    }
    body = BillingInfoInOut(
        billing_email="billing_email_example",
        preferred_currency="preferred_currency_example",
        customer_name="customer_name_example",
        customer_phone="customer_phone_example",
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        address_city="address_city_example",
        address_postal_code="address_postal_code_example",
        address_state="address_state_example",
        address_country="address_country_example",
        vat_id="vat_id_example",
    )
    try:
        # Sets or update the billing information (company name, address, phone, vat ID)
        api_response = api_instance.update_billing_info(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->update_billing_info: %s\n" % e)
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
[**BillingInfoInOut**](../../models/BillingInfoInOut.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_billing_info.ApiResponseFor200) | The updated billing info
401 | [ApiResponseFor401](#update_billing_info.ApiResponseFor401) | Missing or incorrect token

#### update_billing_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BillingInfoInOut**](../../models/BillingInfoInOut.md) |  | 


#### update_billing_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_limit**
<a id="update_limit"></a>
> APIPeriodUsageOut update_limit(usage_limithard_or_softtoken)

Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.api_period_usage_out import APIPeriodUsageOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'usageLimit': 1,
        'hardOrSoft': True,
        'token': "token_example",
    }
    try:
        # Modifies the hard/soft limit on the API plan's overages (default is 0$ soft limit).
        api_response = api_instance.update_limit(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->update_limit: %s\n" % e)
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
usageLimit | UsageLimitSchema | | 
hardOrSoft | HardOrSoftSchema | | 
token | TokenSchema | | 

# UsageLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# HardOrSoftSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_limit.ApiResponseFor200) | An API subscription
401 | [ApiResponseFor401](#update_limit.ApiResponseFor401) | Missing or incorrect token

#### update_limit.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIPeriodUsageOut**](../../models/APIPeriodUsageOut.md) |  | 


#### update_limit.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_payment_default**
<a id="update_payment_default"></a>
> StripeCustomerOut update_payment_default(defaut_source_idtoken)

Update the default Stripe card associated with the current google auth session token.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.stripe_customer_out import StripeCustomerOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'defautSourceId': "defautSourceId_example",
        'token': "token_example",
    }
    try:
        # Update the default Stripe card associated with the current google auth session token.
        api_response = api_instance.update_payment_default(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->update_payment_default: %s\n" % e)
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
defautSourceId | DefautSourceIdSchema | | 
token | TokenSchema | | 

# DefautSourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_payment_default.ApiResponseFor200) | A stripe customer info
401 | [ApiResponseFor401](#update_payment_default.ApiResponseFor401) | Missing or incorrect token

#### update_payment_default.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StripeCustomerOut**](../../models/StripeCustomerOut.md) |  | 


#### update_payment_default.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user_info**
<a id="update_user_info"></a>
> UserInfoOut update_user_info(emaildisplay_nametoken)

Sets or update the user email and name information

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.user_info_out import UserInfoOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'email': "email_example",
        'displayName': "displayName_example",
        'token': "token_example",
    }
    try:
        # Sets or update the user email and name information
        api_response = api_instance.update_user_info(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->update_user_info: %s\n" % e)
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
email | EmailSchema | | 
displayName | DisplayNameSchema | | 
token | TokenSchema | | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DisplayNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_user_info.ApiResponseFor200) | The updated user info
401 | [ApiResponseFor401](#update_user_info.ApiResponseFor401) | Missing or incorrect token

#### update_user_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserInfoOut**](../../models/UserInfoOut.md) |  | 


#### update_user_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **user_info**
<a id="user_info"></a>
> UserInfoOut user_info(token)

Get the user profile associated with the current google auth session token.

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
from gotyai_client.model.user_info_out import UserInfoOut
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'token': "token_example",
    }
    try:
        # Get the user profile associated with the current google auth session token.
        api_response = api_instance.user_info(
            path_params=path_params,
        )
        pprint(api_response)
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->user_info: %s\n" % e)
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
token | TokenSchema | | 

# TokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#user_info.ApiResponseFor200) | User Information
401 | [ApiResponseFor401](#user_info.ApiResponseFor401) | Missing or incorrect token

#### user_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserInfoOut**](../../models/UserInfoOut.md) |  | 


#### user_info.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_email**
<a id="verify_email"></a>
> verify_email(email_token)

Verifies an email, based on token sent to that email

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'emailToken': "emailToken_example",
    }
    try:
        # Verifies an email, based on token sent to that email
        api_response = api_instance.verify_email(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->verify_email: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
emailToken | EmailTokenSchema | | 

# EmailTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#verify_email.ApiResponseFor401) | Missing or incorrect token

#### verify_email.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_remove_email**
<a id="verify_remove_email"></a>
> verify_remove_email(email_token)

Verifies an email, based on token sent to that email

### Example

* Api Key Authentication (api_key):
```python
import gotyai_client
from gotyai_client.apis.tags import admin_api
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
    api_instance = admin_api.AdminApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'emailToken': "emailToken_example",
    }
    try:
        # Verifies an email, based on token sent to that email
        api_response = api_instance.verify_remove_email(
            path_params=path_params,
        )
    except gotyai_client.ApiException as e:
        print("Exception when calling AdminApi->verify_remove_email: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
emailToken | EmailTokenSchema | | 

# EmailTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
401 | [ApiResponseFor401](#verify_remove_email.ApiResponseFor401) | Missing or incorrect token

#### verify_remove_email.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

