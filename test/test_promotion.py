# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from dlrnapi_client.models.promotion import Promotion


class TestPromotion(unittest.TestCase):
    """Promotion unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPromotion(self):
        """Test Promotion """
        model = Promotion()
        expected = {'promote_name': None, 'commit_hash': None,
                    'distro_hash': None, 'timestamp': None, 'user': None}
        self.assertEqual(model.to_dict(), expected)


if __name__ == '__main__':
    unittest.main()
