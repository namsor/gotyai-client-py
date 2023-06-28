# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import gotyai_client
from gotyai_client.paths.api2_json_subscribe_plan_on_behalf_plan_name_api_key import get  # noqa: E501
from gotyai_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApi2JsonSubscribePlanOnBehalfPlanNameApiKey(ApiTestMixin, unittest.TestCase):
    """
    Api2JsonSubscribePlanOnBehalfPlanNameApiKey unit test stubs
        Subscribe to a give API plan, using the user's preferred or default currency (admin only).  # noqa: E501
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
