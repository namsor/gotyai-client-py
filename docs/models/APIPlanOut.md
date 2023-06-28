# gotyai_client.model.api_plan_out.APIPlanOut

The list of available API Plans.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of available API Plans. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**planName** | str,  | str,  | The API Plan name. | [optional] 
**planQuota** | decimal.Decimal, int,  | decimal.Decimal,  | The API Plan&#x27;s include free quota in number of units (NB/ not in number of names). | [optional] value must be a 64 bit integer
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The API Plan monthly price. | [optional] value must be a 64 bit float
**priceOverage** | decimal.Decimal, int, float,  | decimal.Decimal,  | The API Plan&#x27;s overages (additional cost on top of free quota). | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

