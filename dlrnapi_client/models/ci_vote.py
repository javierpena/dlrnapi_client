# coding: utf-8

"""
    DLRN API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CIVote(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, job_id=None, commit_hash=None, distro_hash=None, url=None, timestamp=None, in_progress=None, success=None, notes=None):
        """
        CIVote - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job_id': 'str',
            'commit_hash': 'str',
            'distro_hash': 'str',
            'url': 'str',
            'timestamp': 'int',
            'in_progress': 'bool',
            'success': 'bool',
            'notes': 'str'
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'commit_hash': 'commit_hash',
            'distro_hash': 'distro_hash',
            'url': 'url',
            'timestamp': 'timestamp',
            'in_progress': 'in_progress',
            'success': 'success',
            'notes': 'notes'
        }

        self._job_id = job_id
        self._commit_hash = commit_hash
        self._distro_hash = distro_hash
        self._url = url
        self._timestamp = timestamp
        self._in_progress = in_progress
        self._success = success
        self._notes = notes

    @property
    def job_id(self):
        """
        Gets the job_id of this CIVote.
        name of the CI sending the vote

        :return: The job_id of this CIVote.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this CIVote.
        name of the CI sending the vote

        :param job_id: The job_id of this CIVote.
        :type: str
        """

        self._job_id = job_id

    @property
    def commit_hash(self):
        """
        Gets the commit_hash of this CIVote.
        commit_hash of tested repo

        :return: The commit_hash of this CIVote.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """
        Sets the commit_hash of this CIVote.
        commit_hash of tested repo

        :param commit_hash: The commit_hash of this CIVote.
        :type: str
        """

        self._commit_hash = commit_hash

    @property
    def distro_hash(self):
        """
        Gets the distro_hash of this CIVote.
        distro_hash of tested repo

        :return: The distro_hash of this CIVote.
        :rtype: str
        """
        return self._distro_hash

    @distro_hash.setter
    def distro_hash(self, distro_hash):
        """
        Sets the distro_hash of this CIVote.
        distro_hash of tested repo

        :param distro_hash: The distro_hash of this CIVote.
        :type: str
        """

        self._distro_hash = distro_hash

    @property
    def url(self):
        """
        Gets the url of this CIVote.
        URL where to find additional information from the CI execution

        :return: The url of this CIVote.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CIVote.
        URL where to find additional information from the CI execution

        :param url: The url of this CIVote.
        :type: str
        """

        self._url = url

    @property
    def timestamp(self):
        """
        Gets the timestamp of this CIVote.
        Timestamp (in seconds since the epoch)

        :return: The timestamp of this CIVote.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this CIVote.
        Timestamp (in seconds since the epoch)

        :param timestamp: The timestamp of this CIVote.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def in_progress(self):
        """
        Gets the in_progress of this CIVote.
        is this CI job still in-progress?

        :return: The in_progress of this CIVote.
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """
        Sets the in_progress of this CIVote.
        is this CI job still in-progress?

        :param in_progress: The in_progress of this CIVote.
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def success(self):
        """
        Gets the success of this CIVote.
        Was the CI execution successful?

        :return: The success of this CIVote.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this CIVote.
        Was the CI execution successful?

        :param success: The success of this CIVote.
        :type: bool
        """

        self._success = success

    @property
    def notes(self):
        """
        Gets the notes of this CIVote.
        additional notes

        :return: The notes of this CIVote.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this CIVote.
        additional notes

        :param notes: The notes of this CIVote.
        :type: str
        """

        self._notes = notes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CIVote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
