# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    The version of the OpenAPI document: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gotyai_client import schemas  # noqa: F401


class BillingInfoInOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            billingEmail = schemas.StrSchema
            preferredCurrency = schemas.StrSchema
            customerName = schemas.StrSchema
            customerPhone = schemas.StrSchema
            addressLine1 = schemas.StrSchema
            addressLine2 = schemas.StrSchema
            addressCity = schemas.StrSchema
            addressPostalCode = schemas.StrSchema
            addressState = schemas.StrSchema
            addressCountry = schemas.StrSchema
            vatID = schemas.StrSchema
            __annotations__ = {
                "billingEmail": billingEmail,
                "preferredCurrency": preferredCurrency,
                "customerName": customerName,
                "customerPhone": customerPhone,
                "addressLine1": addressLine1,
                "addressLine2": addressLine2,
                "addressCity": addressCity,
                "addressPostalCode": addressPostalCode,
                "addressState": addressState,
                "addressCountry": addressCountry,
                "vatID": vatID,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingEmail"]) -> MetaOapg.properties.billingEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferredCurrency"]) -> MetaOapg.properties.preferredCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerName"]) -> MetaOapg.properties.customerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerPhone"]) -> MetaOapg.properties.customerPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine1"]) -> MetaOapg.properties.addressLine1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLine2"]) -> MetaOapg.properties.addressLine2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressCity"]) -> MetaOapg.properties.addressCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressPostalCode"]) -> MetaOapg.properties.addressPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressState"]) -> MetaOapg.properties.addressState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressCountry"]) -> MetaOapg.properties.addressCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vatID"]) -> MetaOapg.properties.vatID: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["billingEmail", "preferredCurrency", "customerName", "customerPhone", "addressLine1", "addressLine2", "addressCity", "addressPostalCode", "addressState", "addressCountry", "vatID", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingEmail"]) -> typing.Union[MetaOapg.properties.billingEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferredCurrency"]) -> typing.Union[MetaOapg.properties.preferredCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerName"]) -> typing.Union[MetaOapg.properties.customerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerPhone"]) -> typing.Union[MetaOapg.properties.customerPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine1"]) -> typing.Union[MetaOapg.properties.addressLine1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLine2"]) -> typing.Union[MetaOapg.properties.addressLine2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressCity"]) -> typing.Union[MetaOapg.properties.addressCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressPostalCode"]) -> typing.Union[MetaOapg.properties.addressPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressState"]) -> typing.Union[MetaOapg.properties.addressState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressCountry"]) -> typing.Union[MetaOapg.properties.addressCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vatID"]) -> typing.Union[MetaOapg.properties.vatID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["billingEmail", "preferredCurrency", "customerName", "customerPhone", "addressLine1", "addressLine2", "addressCity", "addressPostalCode", "addressState", "addressCountry", "vatID", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        billingEmail: typing.Union[MetaOapg.properties.billingEmail, str, schemas.Unset] = schemas.unset,
        preferredCurrency: typing.Union[MetaOapg.properties.preferredCurrency, str, schemas.Unset] = schemas.unset,
        customerName: typing.Union[MetaOapg.properties.customerName, str, schemas.Unset] = schemas.unset,
        customerPhone: typing.Union[MetaOapg.properties.customerPhone, str, schemas.Unset] = schemas.unset,
        addressLine1: typing.Union[MetaOapg.properties.addressLine1, str, schemas.Unset] = schemas.unset,
        addressLine2: typing.Union[MetaOapg.properties.addressLine2, str, schemas.Unset] = schemas.unset,
        addressCity: typing.Union[MetaOapg.properties.addressCity, str, schemas.Unset] = schemas.unset,
        addressPostalCode: typing.Union[MetaOapg.properties.addressPostalCode, str, schemas.Unset] = schemas.unset,
        addressState: typing.Union[MetaOapg.properties.addressState, str, schemas.Unset] = schemas.unset,
        addressCountry: typing.Union[MetaOapg.properties.addressCountry, str, schemas.Unset] = schemas.unset,
        vatID: typing.Union[MetaOapg.properties.vatID, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BillingInfoInOut':
        return super().__new__(
            cls,
            *_args,
            billingEmail=billingEmail,
            preferredCurrency=preferredCurrency,
            customerName=customerName,
            customerPhone=customerPhone,
            addressLine1=addressLine1,
            addressLine2=addressLine2,
            addressCity=addressCity,
            addressPostalCode=addressPostalCode,
            addressState=addressState,
            addressCountry=addressCountry,
            vatID=vatID,
            _configuration=_configuration,
            **kwargs,
        )
