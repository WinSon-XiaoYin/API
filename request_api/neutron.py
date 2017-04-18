# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json
import settings


class NeutronManager(object):
    @classmethod
    def networks_list(cls, param=None):
        url = cls.format_url() + settings.network_list_url.format(query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def metering_label_list(cls, param=None):
        url = cls.format_url() + settings.metering_label_list_url.format(query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @staticmethod
    def format_url():
        service = settings.protocol + "://" + settings.ip + ":" + settings.neutron
        return service
