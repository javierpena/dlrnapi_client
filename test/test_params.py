# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.params import Params


class TestParams(unittest.TestCase):
    """Params unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParams(self):
        """Test Params """
        model = Params()
        expected = {'max_age': None, 'sequential_mode': None, 'job_id': None,
                    'success': None, 'previous_job_id': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
