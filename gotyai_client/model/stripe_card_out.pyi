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


class StripeCardOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            defaultCard = schemas.BoolSchema
            sourceId = schemas.StrSchema
            expMonth = schemas.Int64Schema
            expYear = schemas.Int64Schema
            last4 = schemas.StrSchema
            brand = schemas.StrSchema
            __annotations__ = {
                "defaultCard": defaultCard,
                "sourceId": sourceId,
                "expMonth": expMonth,
                "expYear": expYear,
                "last4": last4,
                "brand": brand,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultCard"]) -> MetaOapg.properties.defaultCard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceId"]) -> MetaOapg.properties.sourceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expMonth"]) -> MetaOapg.properties.expMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expYear"]) -> MetaOapg.properties.expYear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last4"]) -> MetaOapg.properties.last4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand"]) -> MetaOapg.properties.brand: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["defaultCard", "sourceId", "expMonth", "expYear", "last4", "brand", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultCard"]) -> typing.Union[MetaOapg.properties.defaultCard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceId"]) -> typing.Union[MetaOapg.properties.sourceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expMonth"]) -> typing.Union[MetaOapg.properties.expMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expYear"]) -> typing.Union[MetaOapg.properties.expYear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last4"]) -> typing.Union[MetaOapg.properties.last4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand"]) -> typing.Union[MetaOapg.properties.brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["defaultCard", "sourceId", "expMonth", "expYear", "last4", "brand", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        defaultCard: typing.Union[MetaOapg.properties.defaultCard, bool, schemas.Unset] = schemas.unset,
        sourceId: typing.Union[MetaOapg.properties.sourceId, str, schemas.Unset] = schemas.unset,
        expMonth: typing.Union[MetaOapg.properties.expMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expYear: typing.Union[MetaOapg.properties.expYear, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last4: typing.Union[MetaOapg.properties.last4, str, schemas.Unset] = schemas.unset,
        brand: typing.Union[MetaOapg.properties.brand, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StripeCardOut':
        return super().__new__(
            cls,
            *_args,
            defaultCard=defaultCard,
            sourceId=sourceId,
            expMonth=expMonth,
            expYear=expYear,
            last4=last4,
            brand=brand,
            _configuration=_configuration,
            **kwargs,
        )