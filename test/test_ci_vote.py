# coding: utf-8

"""
    DLRN API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import dlrnapi_client
from dlrnapi_client.rest import ApiException
from dlrnapi_client.models.ci_vote import CIVote


class TestCIVote(unittest.TestCase):
    """ CIVote unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCIVote(self):
        """
        Test CIVote
        """
        model = dlrnapi_client.models.ci_vote.CIVote()


if __name__ == '__main__':
    unittest.main()
