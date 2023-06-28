# gotyai_client.model.invoice_out.InvoiceOut

List of Corporate invoices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of Corporate invoices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[items](#items)** | list, tuple,  | tuple,  | The invoice items | [optional] 
**userId** | str,  | str,  | The user id. | [optional] 
**invoiceId** | str,  | str,  | The invoice ID. | [optional] 
**isStriped** | bool,  | BoolClass,  | If user is striped. | [optional] 
**stripeCustomerId** | str,  | str,  | The Stripe customer ID. | [optional] 
**amountDue** | decimal.Decimal, int,  | decimal.Decimal,  | The total amount due. | [optional] value must be a 64 bit integer
**amountPaid** | decimal.Decimal, int,  | decimal.Decimal,  | The total amount paid. | [optional] value must be a 64 bit integer
**amountRemaining** | decimal.Decimal, int,  | decimal.Decimal,  | The total amount remaining. | [optional] value must be a 64 bit integer
**attempted** | bool,  | BoolClass,  | The payment was attempted. | [optional] 
**currency** | str,  | str,  | The currency. | [optional] 
**invoiceDate** | str, datetime,  | str,  | The invoice date. | [optional] value must conform to RFC-3339 date-time
**dueDate** | str, datetime,  | str,  | The invoice due date. | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | The invoice description. | [optional] 
**invoicePdf** | str,  | str,  | The link to the invoice PDF. | [optional] 
**periodStart** | str, datetime,  | str,  | The API plan period start date. | [optional] value must conform to RFC-3339 date-time
**periodEnd** | str, datetime,  | str,  | The API plan period end date. | [optional] value must conform to RFC-3339 date-time
**receiptNumber** | str,  | str,  | The payment receipt number. | [optional] 
**invoiceStatus** | str,  | str,  | The invoice status. | [optional] 
**subTotal** | decimal.Decimal, int,  | decimal.Decimal,  | The invoice subtotal before tax. | [optional] value must be a 64 bit integer
**tax** | decimal.Decimal, int,  | decimal.Decimal,  | The invoice tax amount. | [optional] value must be a 64 bit integer
**taxPercent** | decimal.Decimal, int,  | decimal.Decimal,  | The invoice tax percentage. | [optional] value must be a 64 bit integer
**total** | decimal.Decimal, int,  | decimal.Decimal,  | The invoice total amount. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

The invoice items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The invoice items | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InvoiceItemOut**](InvoiceItemOut.md) | [**InvoiceItemOut**](InvoiceItemOut.md) | [**InvoiceItemOut**](InvoiceItemOut.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

