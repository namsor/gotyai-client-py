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


class CacheMetricsOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Simple metrics system caches
    """


    class MetaOapg:
        
        class properties:
            cacheName = schemas.StrSchema
            cacheStats = schemas.StrSchema
            __annotations__ = {
                "cacheName": cacheName,
                "cacheStats": cacheStats,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cacheName"]) -> MetaOapg.properties.cacheName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cacheStats"]) -> MetaOapg.properties.cacheStats: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cacheName", "cacheStats", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cacheName"]) -> typing.Union[MetaOapg.properties.cacheName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cacheStats"]) -> typing.Union[MetaOapg.properties.cacheStats, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cacheName", "cacheStats", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cacheName: typing.Union[MetaOapg.properties.cacheName, str, schemas.Unset] = schemas.unset,
        cacheStats: typing.Union[MetaOapg.properties.cacheStats, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CacheMetricsOut':
        return super().__new__(
            cls,
            *_args,
            cacheName=cacheName,
            cacheStats=cacheStats,
            _configuration=_configuration,
            **kwargs,
        )
