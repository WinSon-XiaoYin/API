import os
import requests
import json
import settings


class keystoneManager(object):
    @classmethod
    def fetch_token(cls):
        auth = {'auth': {'tenantName': os.environ['OS_TENANT_NAME'],
                         'passwordCredentials': {'username': os.environ['OS_USERNAME'],
                                                 'password': os.environ['OS_PASSWORD']}}}

        url = cls.format_url(service_url=settings.token_url)
        print "req: POST %s" % url
        response = requests.post(url=url, data=json.dumps(auth))
        content = json.loads(response.content)
        token = content['access']['token']['id']
        return token

    @staticmethod
    def format_url(service_url=None):
        url = settings.protocol + "://" + settings.ip + ":" \
              + settings.keystone + service_url
        return url
