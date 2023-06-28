# coding: utf-8

"""
    Gotyai API v3

    Gotyai API : the Spartan explainable AI   # noqa: E501

    The version of the OpenAPI document: 3.0.2
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""

from gotyai_client.paths.api2_json_explain_many_classifier_uuid.post import ExplainMany
from gotyai_client.paths.api2_json_explain_one_classifier_uuid.post import ExplainOne
from gotyai_client.paths.api2_json_fit_many_classifier_uuid.post import FitMany
from gotyai_client.paths.api2_json_fit_one_classifier_uuid.post import FitOne
from gotyai_client.paths.api2_json_multinomial_classifier_name.get import Multinomial
from gotyai_client.paths.api2_json_multinomial.get import Multinomial1
from gotyai_client.paths.api2_json_multinomial_create.post import MultinomialCreate
from gotyai_client.paths.api2_json_predict_many_classifier_uuid.post import PredictMany
from gotyai_client.paths.api2_json_predict_one_classifier_uuid.post import PredictOne


class ClassifyApi(
    ExplainMany,
    ExplainOne,
    FitMany,
    FitOne,
    Multinomial,
    Multinomial1,
    MultinomialCreate,
    PredictMany,
    PredictOne,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
