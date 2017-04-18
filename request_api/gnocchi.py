# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json
import settings


def format_url(service_url='', param=''):
    url = settings.protocol + "://" + settings.ip + ":" \
          + settings.gnocchi + service_url.format(query=param)
    return url


def resource_list(param=''):
    url = format_url(service_url=settings.resource_list_url, param=param)
    response = RequestMethod.get(url=url)
    print "status_code: %s" % response.status_code
    content = json.loads(response.content)
    return content


def main():
    pass


if __name__ == '__mian__':
    main()
