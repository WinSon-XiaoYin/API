import os
import requests
import json
from settings import keystone_url


def fetch_token():
    auth = {'auth': {'tenantName': os.environ['OS_TENANT_NAME'],
                     'passwordCredentials': {'username': os.environ['OS_USERNAME'],
                                             'password': os.environ['OS_PASSWORD']}}}

    print "req: POST %s" % keystone_url
    response = requests.post(url=keystone_url, data=json.dumps(auth))
    content = json.loads(response.content)
    token = content['access']['token']['id']
    return token


def main():
    pass


if __name__ == '__main__':
    main()
