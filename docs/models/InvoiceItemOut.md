# gotyai_client.model.invoice_item_out.InvoiceItemOut

The invoice items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The invoice items | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**itemId** | str,  | str,  | The invoice item. | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | The item amount. | [optional] value must be a 64 bit integer
**currency** | str,  | str,  | The item currency. | [optional] 
**description** | str,  | str,  | The item description. | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | The item quantity. | [optional] value must be a 64 bit integer
**subscription** | str,  | str,  | The subscription. | [optional] 
**subscriptionItem** | str,  | str,  | The subscription item. | [optional] 
**invoiceItemType** | str,  | str,  | The invoice item type. | [optional] 
**planNickname** | str,  | str,  | The API plan nickname. | [optional] 
**planDesc** | str,  | str,  | The API plan desc. | [optional] 
**planName** | str,  | str,  | The API plan name. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

