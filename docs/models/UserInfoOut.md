# gotyai_client.model.user_info_out.UserInfoOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uid** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**phoneNumber** | str,  | str,  |  | [optional] 
**emailVerified** | bool,  | BoolClass,  |  | [optional] 
**displayName** | str,  | str,  |  | [optional] 
**photoUrl** | str,  | str,  |  | [optional] 
**disabled** | bool,  | BoolClass,  |  | [optional] 
**firstKnownIpAddress** | str,  | str,  |  | [optional] 
**emailVerifiedIpAddress** | str,  | str,  |  | [optional] 
**providerId** | str,  | str,  |  | [optional] 
**timeStamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**verifyToken** | str,  | str,  |  | [optional] 
**apiKey** | str,  | str,  |  | [optional] 
**stripePerishableKey** | str,  | str,  |  | [optional] 
**stripeCustomerId** | str,  | str,  |  | [optional] 
**[otherInfos](#otherInfos)** | list, tuple,  | tuple,  |  | [optional] 
**disposableEmail** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# otherInfos

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserInfoOut**](UserInfoOut.md) | [**UserInfoOut**](UserInfoOut.md) | [**UserInfoOut**](UserInfoOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

