import requests
import json
from generate_token import keystoneManager

headers = {"Accept": "application/json"}


class RequestMethod(object):
    """
    HTTP request method
    """

    @classmethod
    def get(cls, url):
        """
        GET method
        :param url: the service url
        :return: response
        """
        headers = cls.header_add_token()
        print "req: GET %s" % url
        response = requests.get(url, headers=headers)
        return response

    @classmethod
    def post(cls, url, data=None):
        """
        POST method
        :param url: the service url
        :param data: post data
        :return: response
        """
        headers = cls.header_add_token()
        print "req: POST %s" % url
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    @classmethod
    def put(cls, url, data=None):
        """
        PUT method
        :param url: the service url
        :param data: post data
        :return: response
        """
        headers = cls.header_add_token()
        print "req: PUT %s" % url
        response = requests.put(url, headers=headers, data=json.dumps(data))
        return response

    @classmethod
    def delete(cls, url):
        """
        DELETE method
        :param url: the service url
        :return: response
        """
        headers = cls.header_add_token()
        print "req: DELETE %s" % url
        response = requests.delete(url, headers=headers)
        return response

    @staticmethod
    def header_add_token():
        """
        fetch a token
        """
        token = keystoneManager.fetch_token()
        headers['X-Auth-Token'] = token
        return headers

