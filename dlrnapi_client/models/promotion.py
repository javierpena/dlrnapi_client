# coding: utf-8

"""
    DLRN API

    DLRN API client

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems


class Promotion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, commit_hash=None, distro_hash=None, extended_hash=None,
                 aggregate_hash=None, promote_name=None, timestamp=None,
                 user=None, repo_hash=None, repo_url=None, component=None):
        """Promotion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'commit_hash': 'str',
            'distro_hash': 'str',
            'extended_hash': 'str',
            'aggregate_hash': 'str',
            'promote_name': 'str',
            'timestamp': 'int',
            'user': 'str',
            'repo_hash': 'str',
            'repo_url': 'str',
            'component': 'str',
        }

        self.attribute_map = {
            'commit_hash': 'commit_hash',
            'distro_hash': 'distro_hash',
            'extended_hash': 'extended_hash',
            'aggregate_hash': 'aggregate_hash',
            'promote_name': 'promote_name',
            'timestamp': 'timestamp',
            'user': 'user',
            'repo_hash': 'repo_hash',
            'repo_url': 'repo_url',
            'component': 'component',
        }

        self._commit_hash = commit_hash
        self._distro_hash = distro_hash
        self._extended_hash = extended_hash
        self._aggregate_hash = aggregate_hash
        self._promote_name = promote_name
        self._timestamp = timestamp
        self._user = user
        self._repo_hash = repo_hash
        self._repo_url = repo_url
        self._component = component

    @property
    def commit_hash(self):
        """Gets the commit_hash of this Promotion.

        commit_hash of promoted repo

        :return: The commit_hash of this Promotion.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this Promotion.

        commit_hash of promoted repo

        :param commit_hash: The commit_hash of this Promotion.
        :type: str
        """

        self._commit_hash = commit_hash

    @property
    def distro_hash(self):
        """Gets the distro_hash of this Promotion.

        distro_hash of promoted repo

        :return: The distro_hash of this Promotion.
        :rtype: str
        """
        return self._distro_hash

    @distro_hash.setter
    def distro_hash(self, distro_hash):
        """Sets the distro_hash of this Promotion.

        distro_hash of promoted repo

        :param distro_hash: The distro_hash of this Promotion.
        :type: str
        """

        self._distro_hash = distro_hash

    @property
    def extended_hash(self):
        """Gets the extended_hash of this Promotion Query.

        distro_hash of promoted repo

        :return: The extended_hash of this Promotion Query.
        :rtype: str
        """
        return self._extended_hash

    @extended_hash.setter
    def extended_hash(self, extended_hash):
        """Sets the extended_hash of this Promotion Query.

        extended_hash of promoted repo

        :param extended_hash: The extended_hash of this Promotion Query.
        :type: str
        """

        self._extended_hash = extended_hash

    @property
    def aggregate_hash(self):
        """Gets the aggregate_hash of this Promotion.

        aggregate_hash of promoted repo

        :return: The aggregate_hash of this Promotion.
        :rtype: str
        """
        return self._aggregate_hash

    @aggregate_hash.setter
    def aggregate_hash(self, aggregate_hash):
        """Sets the aggregate_hash of this Promotion.

        aggregate_hash of promoted repo

        :param aggregate_hash: The aggregate_hash of this Promotion.
        :type: str
        """

        self._aggregate_hash = aggregate_hash

    @property
    def promote_name(self):
        """Gets the promote_name of this Promotion.

        name used for the promotion

        :return: The promote_name of this Promotion.
        :rtype: str
        """
        return self._promote_name

    @promote_name.setter
    def promote_name(self, promote_name):
        """Sets the promote_name of this Promotion.

        name used for the promotion

        :param promote_name: The promote_name of this Promotion.
        :type: str
        """

        self._promote_name = promote_name

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
        """Gets the user of this Promotion Query.

        User who created this promotion

        :return: The user.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Promotion Query.

        User who created this promotion

        :param user: The user.
        :type: int
        """

        self._user = user

    @property
    def repo_hash(self):
        """Gets the repo_hash of this Promotion.

        repo_hash of promoted repo

        :return: The repo_hash of this Promotion.
        :rtype: str
        """
        return self._repo_hash

    @repo_hash.setter
    def repo_hash(self, repo_hash):
        """Sets the repo_hash of this Promotion.

        repo_hash of promoted repo

        :param repo_hash: The repo_hash of this Promotion.
        :type: str
        """

        self._repo_hash = repo_hash

    @property
    def repo_url(self):
        """Gets the repo_url of this Promotion.

        repo_url of promoted repo

        :return: The repo_url of this Promotion.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this Promotion.

        repo_url of promoted repo

        :param repo_url: The repo_url of this Promotion.
        :type: str
        """

        self._repo_url = repo_url

    @property
    def component(self):
        """Gets the component of this Promotion.

        component of promoted repo

        :return: The component of this Promotion.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Promotion.

        component of promoted repo

        :param component: The component of this Promotion.
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
        if not isinstance(other, Promotion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal """
        return not self == other
