# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gotyai_client
from gotyai_client.paths.api2_json_spamsurge_block_disposable_emails import get  # noqa: E501
from gotyai_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonSpamsurgeBlockDisposableEmails(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonSpamsurgeBlockDisposableEmails unit test stubs
        Activate/deactivate blocking of disposable emails in case of spam surge.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()