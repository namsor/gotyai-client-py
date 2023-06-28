# gotyai_client.model.api_plans_out.APIPlansOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**usageRatioForDupplicates** | decimal.Decimal, int,  | decimal.Decimal,  | Any duplicate names are ignored to the limit of this factor (ex. 20x &#x27;john smith&#x27; count as ONE &#x27;john smith&#x27;) | [optional] value must be a 64 bit integer
**currencyIso3** | str,  | str,  | The currency ISO3 code for the plan selection | [optional] 
**currencySymbol** | str,  | str,  | The currency symbol for the plan selection | [optional] 
**[plans](#plans)** | list, tuple,  | tuple,  | The list of available API Plans. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plans

The list of available API Plans.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of available API Plans. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**APIPlanOut**](APIPlanOut.md) | [**APIPlanOut**](APIPlanOut.md) | [**APIPlanOut**](APIPlanOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

