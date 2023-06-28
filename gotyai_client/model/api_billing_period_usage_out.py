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


class APIBillingPeriodUsageOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The current billing period.
    """


    class MetaOapg:
        
        class properties:
            apiKey = schemas.StrSchema
            subscriptionStarted = schemas.Int64Schema
            periodStarted = schemas.Int64Schema
            periodEnded = schemas.Int64Schema
            stripeCurrentPeriodEnd = schemas.Int64Schema
            stripeCurrentPeriodStart = schemas.Int64Schema
            billingStatus = schemas.StrSchema
            usage = schemas.Int64Schema
            softLimit = schemas.Int64Schema
            hardLimit = schemas.Int64Schema
            __annotations__ = {
                "apiKey": apiKey,
                "subscriptionStarted": subscriptionStarted,
                "periodStarted": periodStarted,
                "periodEnded": periodEnded,
                "stripeCurrentPeriodEnd": stripeCurrentPeriodEnd,
                "stripeCurrentPeriodStart": stripeCurrentPeriodStart,
                "billingStatus": billingStatus,
                "usage": usage,
                "softLimit": softLimit,
                "hardLimit": hardLimit,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriptionStarted"]) -> MetaOapg.properties.subscriptionStarted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodStarted"]) -> MetaOapg.properties.periodStarted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodEnded"]) -> MetaOapg.properties.periodEnded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeCurrentPeriodEnd"]) -> MetaOapg.properties.stripeCurrentPeriodEnd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeCurrentPeriodStart"]) -> MetaOapg.properties.stripeCurrentPeriodStart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingStatus"]) -> MetaOapg.properties.billingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usage"]) -> MetaOapg.properties.usage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["softLimit"]) -> MetaOapg.properties.softLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hardLimit"]) -> MetaOapg.properties.hardLimit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiKey", "subscriptionStarted", "periodStarted", "periodEnded", "stripeCurrentPeriodEnd", "stripeCurrentPeriodStart", "billingStatus", "usage", "softLimit", "hardLimit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> typing.Union[MetaOapg.properties.apiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriptionStarted"]) -> typing.Union[MetaOapg.properties.subscriptionStarted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodStarted"]) -> typing.Union[MetaOapg.properties.periodStarted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodEnded"]) -> typing.Union[MetaOapg.properties.periodEnded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeCurrentPeriodEnd"]) -> typing.Union[MetaOapg.properties.stripeCurrentPeriodEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeCurrentPeriodStart"]) -> typing.Union[MetaOapg.properties.stripeCurrentPeriodStart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingStatus"]) -> typing.Union[MetaOapg.properties.billingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usage"]) -> typing.Union[MetaOapg.properties.usage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["softLimit"]) -> typing.Union[MetaOapg.properties.softLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hardLimit"]) -> typing.Union[MetaOapg.properties.hardLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiKey", "subscriptionStarted", "periodStarted", "periodEnded", "stripeCurrentPeriodEnd", "stripeCurrentPeriodStart", "billingStatus", "usage", "softLimit", "hardLimit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, schemas.Unset] = schemas.unset,
        subscriptionStarted: typing.Union[MetaOapg.properties.subscriptionStarted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        periodStarted: typing.Union[MetaOapg.properties.periodStarted, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        periodEnded: typing.Union[MetaOapg.properties.periodEnded, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stripeCurrentPeriodEnd: typing.Union[MetaOapg.properties.stripeCurrentPeriodEnd, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stripeCurrentPeriodStart: typing.Union[MetaOapg.properties.stripeCurrentPeriodStart, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        billingStatus: typing.Union[MetaOapg.properties.billingStatus, str, schemas.Unset] = schemas.unset,
        usage: typing.Union[MetaOapg.properties.usage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        softLimit: typing.Union[MetaOapg.properties.softLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hardLimit: typing.Union[MetaOapg.properties.hardLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIBillingPeriodUsageOut':
        return super().__new__(
            cls,
            *_args,
            apiKey=apiKey,
            subscriptionStarted=subscriptionStarted,
            periodStarted=periodStarted,
            periodEnded=periodEnded,
            stripeCurrentPeriodEnd=stripeCurrentPeriodEnd,
            stripeCurrentPeriodStart=stripeCurrentPeriodStart,
            billingStatus=billingStatus,
            usage=usage,
            softLimit=softLimit,
            hardLimit=hardLimit,
            _configuration=_configuration,
            **kwargs,
        )