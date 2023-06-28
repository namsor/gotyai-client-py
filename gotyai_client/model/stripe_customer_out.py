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


class StripeCustomerOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            stripeCustomerId = schemas.StrSchema
            sourceCountry = schemas.StrSchema
            sourceCurrency = schemas.StrSchema
            
            
            class stripedCards(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['StripeCardOut']:
                        return StripeCardOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['StripeCardOut'], typing.List['StripeCardOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stripedCards':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'StripeCardOut':
                    return super().__getitem__(i)
            __annotations__ = {
                "stripeCustomerId": stripeCustomerId,
                "sourceCountry": sourceCountry,
                "sourceCurrency": sourceCurrency,
                "stripedCards": stripedCards,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeCustomerId"]) -> MetaOapg.properties.stripeCustomerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCountry"]) -> MetaOapg.properties.sourceCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceCurrency"]) -> MetaOapg.properties.sourceCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripedCards"]) -> MetaOapg.properties.stripedCards: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stripeCustomerId", "sourceCountry", "sourceCurrency", "stripedCards", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeCustomerId"]) -> typing.Union[MetaOapg.properties.stripeCustomerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCountry"]) -> typing.Union[MetaOapg.properties.sourceCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceCurrency"]) -> typing.Union[MetaOapg.properties.sourceCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripedCards"]) -> typing.Union[MetaOapg.properties.stripedCards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stripeCustomerId", "sourceCountry", "sourceCurrency", "stripedCards", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        stripeCustomerId: typing.Union[MetaOapg.properties.stripeCustomerId, str, schemas.Unset] = schemas.unset,
        sourceCountry: typing.Union[MetaOapg.properties.sourceCountry, str, schemas.Unset] = schemas.unset,
        sourceCurrency: typing.Union[MetaOapg.properties.sourceCurrency, str, schemas.Unset] = schemas.unset,
        stripedCards: typing.Union[MetaOapg.properties.stripedCards, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StripeCustomerOut':
        return super().__new__(
            cls,
            *_args,
            stripeCustomerId=stripeCustomerId,
            sourceCountry=sourceCountry,
            sourceCurrency=sourceCurrency,
            stripedCards=stripedCards,
            _configuration=_configuration,
            **kwargs,
        )

from gotyai_client.model.stripe_card_out import StripeCardOut