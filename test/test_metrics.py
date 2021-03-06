# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.metrics import Metrics
from dlrnapi_client.models.metrics import MetricsRequest


class TestMetricsRequest(unittest.TestCase):
    """MetricsRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricsRequest(self):
        """Test MetricsRequest """
        model = MetricsRequest()
        expected = {'start_date': None, 'end_date': None,
                    'package_name': None}
        self.assertEqual(model.to_dict(), expected)


class TestMetrics(unittest.TestCase):
    """Metrics unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetrics(self):
        """Test Metrics """
        model = Metrics()
        expected = {'succeeded': None, 'failed': None,
                    'total': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
