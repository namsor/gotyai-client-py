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


class UserInfoOut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            uid = schemas.StrSchema
            email = schemas.StrSchema
            phoneNumber = schemas.StrSchema
            emailVerified = schemas.BoolSchema
            displayName = schemas.StrSchema
            photoUrl = schemas.StrSchema
            disabled = schemas.BoolSchema
            firstKnownIpAddress = schemas.StrSchema
            emailVerifiedIpAddress = schemas.StrSchema
            providerId = schemas.StrSchema
            timeStamp = schemas.Int64Schema
            verifyToken = schemas.StrSchema
            apiKey = schemas.StrSchema
            stripePerishableKey = schemas.StrSchema
            stripeCustomerId = schemas.StrSchema
            
            
            class otherInfos(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserInfoOut']:
                        return UserInfoOut
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['UserInfoOut'], typing.List['UserInfoOut']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'otherInfos':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserInfoOut':
                    return super().__getitem__(i)
            disposableEmail = schemas.BoolSchema
            __annotations__ = {
                "uid": uid,
                "email": email,
                "phoneNumber": phoneNumber,
                "emailVerified": emailVerified,
                "displayName": displayName,
                "photoUrl": photoUrl,
                "disabled": disabled,
                "firstKnownIpAddress": firstKnownIpAddress,
                "emailVerifiedIpAddress": emailVerifiedIpAddress,
                "providerId": providerId,
                "timeStamp": timeStamp,
                "verifyToken": verifyToken,
                "apiKey": apiKey,
                "stripePerishableKey": stripePerishableKey,
                "stripeCustomerId": stripeCustomerId,
                "otherInfos": otherInfos,
                "disposableEmail": disposableEmail,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uid"]) -> MetaOapg.properties.uid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailVerified"]) -> MetaOapg.properties.emailVerified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photoUrl"]) -> MetaOapg.properties.photoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disabled"]) -> MetaOapg.properties.disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstKnownIpAddress"]) -> MetaOapg.properties.firstKnownIpAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailVerifiedIpAddress"]) -> MetaOapg.properties.emailVerifiedIpAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerId"]) -> MetaOapg.properties.providerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeStamp"]) -> MetaOapg.properties.timeStamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verifyToken"]) -> MetaOapg.properties.verifyToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKey"]) -> MetaOapg.properties.apiKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripePerishableKey"]) -> MetaOapg.properties.stripePerishableKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stripeCustomerId"]) -> MetaOapg.properties.stripeCustomerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherInfos"]) -> MetaOapg.properties.otherInfos: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disposableEmail"]) -> MetaOapg.properties.disposableEmail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uid", "email", "phoneNumber", "emailVerified", "displayName", "photoUrl", "disabled", "firstKnownIpAddress", "emailVerifiedIpAddress", "providerId", "timeStamp", "verifyToken", "apiKey", "stripePerishableKey", "stripeCustomerId", "otherInfos", "disposableEmail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uid"]) -> typing.Union[MetaOapg.properties.uid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailVerified"]) -> typing.Union[MetaOapg.properties.emailVerified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["photoUrl"]) -> typing.Union[MetaOapg.properties.photoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disabled"]) -> typing.Union[MetaOapg.properties.disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstKnownIpAddress"]) -> typing.Union[MetaOapg.properties.firstKnownIpAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailVerifiedIpAddress"]) -> typing.Union[MetaOapg.properties.emailVerifiedIpAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerId"]) -> typing.Union[MetaOapg.properties.providerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeStamp"]) -> typing.Union[MetaOapg.properties.timeStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verifyToken"]) -> typing.Union[MetaOapg.properties.verifyToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKey"]) -> typing.Union[MetaOapg.properties.apiKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripePerishableKey"]) -> typing.Union[MetaOapg.properties.stripePerishableKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stripeCustomerId"]) -> typing.Union[MetaOapg.properties.stripeCustomerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherInfos"]) -> typing.Union[MetaOapg.properties.otherInfos, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disposableEmail"]) -> typing.Union[MetaOapg.properties.disposableEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uid", "email", "phoneNumber", "emailVerified", "displayName", "photoUrl", "disabled", "firstKnownIpAddress", "emailVerifiedIpAddress", "providerId", "timeStamp", "verifyToken", "apiKey", "stripePerishableKey", "stripeCustomerId", "otherInfos", "disposableEmail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uid: typing.Union[MetaOapg.properties.uid, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        emailVerified: typing.Union[MetaOapg.properties.emailVerified, bool, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        photoUrl: typing.Union[MetaOapg.properties.photoUrl, str, schemas.Unset] = schemas.unset,
        disabled: typing.Union[MetaOapg.properties.disabled, bool, schemas.Unset] = schemas.unset,
        firstKnownIpAddress: typing.Union[MetaOapg.properties.firstKnownIpAddress, str, schemas.Unset] = schemas.unset,
        emailVerifiedIpAddress: typing.Union[MetaOapg.properties.emailVerifiedIpAddress, str, schemas.Unset] = schemas.unset,
        providerId: typing.Union[MetaOapg.properties.providerId, str, schemas.Unset] = schemas.unset,
        timeStamp: typing.Union[MetaOapg.properties.timeStamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        verifyToken: typing.Union[MetaOapg.properties.verifyToken, str, schemas.Unset] = schemas.unset,
        apiKey: typing.Union[MetaOapg.properties.apiKey, str, schemas.Unset] = schemas.unset,
        stripePerishableKey: typing.Union[MetaOapg.properties.stripePerishableKey, str, schemas.Unset] = schemas.unset,
        stripeCustomerId: typing.Union[MetaOapg.properties.stripeCustomerId, str, schemas.Unset] = schemas.unset,
        otherInfos: typing.Union[MetaOapg.properties.otherInfos, list, tuple, schemas.Unset] = schemas.unset,
        disposableEmail: typing.Union[MetaOapg.properties.disposableEmail, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserInfoOut':
        return super().__new__(
            cls,
            *_args,
            uid=uid,
            email=email,
            phoneNumber=phoneNumber,
            emailVerified=emailVerified,
            displayName=displayName,
            photoUrl=photoUrl,
            disabled=disabled,
            firstKnownIpAddress=firstKnownIpAddress,
            emailVerifiedIpAddress=emailVerifiedIpAddress,
            providerId=providerId,
            timeStamp=timeStamp,
            verifyToken=verifyToken,
            apiKey=apiKey,
            stripePerishableKey=stripePerishableKey,
            stripeCustomerId=stripeCustomerId,
            otherInfos=otherInfos,
            disposableEmail=disposableEmail,
            _configuration=_configuration,
            **kwargs,
        )
