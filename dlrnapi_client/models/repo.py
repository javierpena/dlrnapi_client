# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems


class Repo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 success=None, job_id=None, in_progress=None, timestamp=None,
                 user=None, component=None):
        """Repo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'success': 'bool',
            'job_id': 'str',
            'in_progress': 'bool',
            'timestamp': 'int',
            'user': 'str',
            'component': 'str'
        }

        self.attribute_map = {
            'commit_hash': 'commit_hash',
            'distro_hash': 'distro_hash',
            'extended_hash': 'extended_hash',
            'success': 'success',
            'job_id': 'job_id',
            'in_progress': 'in_progress',
            'timestamp': 'timestamp',
            'user': 'user',
            'component': 'component'
        }

        self._commit_hash = commit_hash
        self._distro_hash = distro_hash
        self._extended_hash = extended_hash
        self._success = success
        self._job_id = job_id
        self._in_progress = in_progress
        self._timestamp = timestamp
        self._user = user
        self._component = component

    @property
    def commit_hash(self):
        """Gets the commit_hash of this Repo.

        commit_hash of tested repo

        :return: The commit_hash of this Repo.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this Repo.

        commit_hash of tested repo

        :param commit_hash: The commit_hash of this Repo.
        :type: str
        """

        self._commit_hash = commit_hash

    @property
    def distro_hash(self):
        """Gets the distro_hash of this Repo.

        distro_hash of tested repo

        :return: The distro_hash of this Repo.
        :rtype: str
        """
        return self._distro_hash

    @distro_hash.setter
    def distro_hash(self, distro_hash):
        """Sets the distro_hash of this Repo.

        distro_hash of tested repo

        :param distro_hash: The distro_hash of this Repo.
        :type: str
        """

        self._distro_hash = distro_hash

    @property
    def extended_hash(self):
        """Gets the extended_hash of this Repo.

        extended_hash of tested repo

        :return: The extended_hash of this Repo.
        :rtype: str
        """
        return self._extended_hash

    @extended_hash.setter
    def extended_hash(self, extended_hash):
        """Sets the extended_hash of this Repo.

        extended_hash of tested repo

        :param extended_hash: The extended_hash of this Repo.
        :type: str
        """

        self._extended_hash = extended_hash

    @property
    def success(self):
        """Gets the success of this Repo.

        whether the test was successful or not

        :return: The success of this Repo.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Repo.

        whether the test was successful or not

        :param success: The success of this Repo.
        :type: bool
        """

        self._success = success

    @property
    def job_id(self):
        """Gets the job_id of this Repo.

        name of the CI sending the vote

        :return: The job_id of this Repo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Repo.

        name of the CI sending the vote

        :param job_id: The job_id of this Repo.
        :type: str
        """

        self._job_id = job_id

    @property
    def in_progress(self):
        """Gets the in_progress of this Repo.

        is this CI job still in-progress?

        :return: The in_progress of this Repo.
        :rtype: bool
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this Repo.

        is this CI job still in-progress?

        :param in_progress: The in_progress of this Repo.
        :type: bool
        """

        self._in_progress = in_progress

    @property
    def timestamp(self):
        """Gets the timestamp of this Repo.

        Timestamp for this CI Vote (taken from the DLRN system time)

        :return: The timestamp of this Repo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Repo.

        Timestamp for this CI Vote (taken from the DLRN system time)

        :param timestamp: The timestamp of this Repo.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def user(self):
        """Gets the user of this Repo.

        User who created the vote

        :return: The user of this Repo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the notes of this Repo.

        User who created the vote

        :param user: The user of this Repo.
        :type: str
        """

        self._user = user

    @property
    def component(self):
        """Gets the component of this Repo.

        additional notes

        :return: The component of this Repo.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Repo.

        additional notes

        :param component: The component of this Repo.
        :type: str
        """

        self._component = component

    def to_dict(self):
        """Returns the model properties as a dict """
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
        """Returns the string representation of the model """
        return pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint` """
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal """
        if not isinstance(other, Repo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other
