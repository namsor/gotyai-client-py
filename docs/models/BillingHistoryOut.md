# gotyai_client.model.billing_history_out.BillingHistoryOut

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[stripeInvoices](#stripeInvoices)** | list, tuple,  | tuple,  | List of Stripe invoices | [optional] 
**[corporateInvoices](#corporateInvoices)** | list, tuple,  | tuple,  | List of Corporate invoices | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stripeInvoices

List of Stripe invoices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Stripe invoices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InvoiceOut**](InvoiceOut.md) | [**InvoiceOut**](InvoiceOut.md) | [**InvoiceOut**](InvoiceOut.md) |  | 

# corporateInvoices

List of Corporate invoices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Corporate invoices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InvoiceOut**](InvoiceOut.md) | [**InvoiceOut**](InvoiceOut.md) | [**InvoiceOut**](InvoiceOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

