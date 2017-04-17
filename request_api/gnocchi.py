# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json


def resource_list(url, param='generic'):
    response = RequestMethod.get(url=url, param=param)
    content = json.loads(response.content)
    return content


def main():
    pass


if __name__ == '__mian__':
    main()
