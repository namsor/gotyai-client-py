# gotyai_client.model.system_metrics_out.SystemMetricsOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cacheMetrics](#cacheMetrics)** | list, tuple,  | tuple,  | The list of caching metrics | [optional] 
**totalMem** | decimal.Decimal, int,  | decimal.Decimal,  | The total memory | [optional] value must be a 64 bit integer
**freeMem** | decimal.Decimal, int,  | decimal.Decimal,  | The total free memory | [optional] value must be a 64 bit integer
**maxMem** | decimal.Decimal, int,  | decimal.Decimal,  | The max memory | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cacheMetrics

The list of caching metrics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of caching metrics | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CacheMetricsOut**](CacheMetricsOut.md) | [**CacheMetricsOut**](CacheMetricsOut.md) | [**CacheMetricsOut**](CacheMetricsOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

