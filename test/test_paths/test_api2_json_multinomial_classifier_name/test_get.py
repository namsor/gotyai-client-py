# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gotyai_client
from gotyai_client.paths.api2_json_multinomial_classifier_name import get  # noqa: E501
from gotyai_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonMultinomialClassifierName(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonMultinomialClassifierName unit test stubs
        Get the multinomila classifier by its name.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
