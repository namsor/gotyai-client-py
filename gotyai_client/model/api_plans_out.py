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


class APIPlansOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            usageRatioForDupplicates = schemas.Int64Schema
            currencyIso3 = schemas.StrSchema
            currencySymbol = schemas.StrSchema
            
            
            class plans(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['APIPlanOut']:
                        return APIPlanOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['APIPlanOut'], typing.List['APIPlanOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'plans':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'APIPlanOut':
                    return super().__getitem__(i)
            __annotations__ = {
                "usageRatioForDupplicates": usageRatioForDupplicates,
                "currencyIso3": currencyIso3,
                "currencySymbol": currencySymbol,
                "plans": plans,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usageRatioForDupplicates"]) -> MetaOapg.properties.usageRatioForDupplicates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyIso3"]) -> MetaOapg.properties.currencyIso3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencySymbol"]) -> MetaOapg.properties.currencySymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plans"]) -> MetaOapg.properties.plans: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["usageRatioForDupplicates", "currencyIso3", "currencySymbol", "plans", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usageRatioForDupplicates"]) -> typing.Union[MetaOapg.properties.usageRatioForDupplicates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyIso3"]) -> typing.Union[MetaOapg.properties.currencyIso3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencySymbol"]) -> typing.Union[MetaOapg.properties.currencySymbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plans"]) -> typing.Union[MetaOapg.properties.plans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["usageRatioForDupplicates", "currencyIso3", "currencySymbol", "plans", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        usageRatioForDupplicates: typing.Union[MetaOapg.properties.usageRatioForDupplicates, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currencyIso3: typing.Union[MetaOapg.properties.currencyIso3, str, schemas.Unset] = schemas.unset,
        currencySymbol: typing.Union[MetaOapg.properties.currencySymbol, str, schemas.Unset] = schemas.unset,
        plans: typing.Union[MetaOapg.properties.plans, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIPlansOut':
        return super().__new__(
            cls,
            *_args,
            usageRatioForDupplicates=usageRatioForDupplicates,
            currencyIso3=currencyIso3,
            currencySymbol=currencySymbol,
            plans=plans,
            _configuration=_configuration,
            **kwargs,
        )

from gotyai_client.model.api_plan_out import APIPlanOut