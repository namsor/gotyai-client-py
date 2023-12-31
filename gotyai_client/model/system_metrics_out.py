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


class SystemMetricsOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class cacheMetrics(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CacheMetricsOut']:
                        return CacheMetricsOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CacheMetricsOut'], typing.List['CacheMetricsOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cacheMetrics':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CacheMetricsOut':
                    return super().__getitem__(i)
            totalMem = schemas.Int64Schema
            freeMem = schemas.Int64Schema
            maxMem = schemas.Int64Schema
            __annotations__ = {
                "cacheMetrics": cacheMetrics,
                "totalMem": totalMem,
                "freeMem": freeMem,
                "maxMem": maxMem,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cacheMetrics"]) -> MetaOapg.properties.cacheMetrics: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalMem"]) -> MetaOapg.properties.totalMem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freeMem"]) -> MetaOapg.properties.freeMem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxMem"]) -> MetaOapg.properties.maxMem: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cacheMetrics", "totalMem", "freeMem", "maxMem", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cacheMetrics"]) -> typing.Union[MetaOapg.properties.cacheMetrics, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalMem"]) -> typing.Union[MetaOapg.properties.totalMem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freeMem"]) -> typing.Union[MetaOapg.properties.freeMem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxMem"]) -> typing.Union[MetaOapg.properties.maxMem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cacheMetrics", "totalMem", "freeMem", "maxMem", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cacheMetrics: typing.Union[MetaOapg.properties.cacheMetrics, list, tuple, schemas.Unset] = schemas.unset,
        totalMem: typing.Union[MetaOapg.properties.totalMem, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        freeMem: typing.Union[MetaOapg.properties.freeMem, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxMem: typing.Union[MetaOapg.properties.maxMem, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SystemMetricsOut':
        return super().__new__(
            cls,
            *_args,
            cacheMetrics=cacheMetrics,
            totalMem=totalMem,
            freeMem=freeMem,
            maxMem=maxMem,
            _configuration=_configuration,
            **kwargs,
        )

from gotyai_client.model.cache_metrics_out import CacheMetricsOut
