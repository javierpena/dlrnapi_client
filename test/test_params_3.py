# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.params_3 import Params3


class TestParams3(unittest.TestCase):
    """Params3 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParams3(self):
        """Test Params3 """
        model = Params3()
        expected = {'job_id': None, 'success': None, 'url': None,
                    'timestamp': None, 'notes': None, 'distro_hash': None,
                    'commit_hash': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
