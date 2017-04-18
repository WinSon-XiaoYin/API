# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json
import settings


class GnocchiManger(object):
    @classmethod
    def resource_list(cls, param=None):
        url = cls.format_url() + settings.resource_list_url.format(query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def resource_detail(cls, resource_id=None):
        url = cls.format_url() + settings.resource_detail_url.format(resource_id=resource_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def resource_history(cls, resource_type="generic", resource_id=None, history=None, param=None):
        url = cls.format_url() + settings.resource_history_url.format(resource_type=resource_type,
                                                                      resource_id=resource_id,
                                                                      history=history,
                                                                      query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def metric_list(cls, param=None):
        url = cls.format_url() + settings.metric_list_url.format(query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def metric_detail(cls, metric_id=None):
        url = cls.format_url() + settings.metric_detail_url.format(metric_id=metric_id)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def measure_detail(cls, metric_id=None, param=None):
        url = cls.format_url() + settings.measure_detail_url.format(metric_id=metric_id, query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @classmethod
    def measures_list(cls, resource_id=None, metric_name=None, param=None):
        url = cls.format_url() + settings.measures_list_url.format(resource_id=resource_id,
                                                                   metric_name=metric_name,
                                                                   query=param)
        response = RequestMethod.get(url=url)
        print "status_code: %s" % response.status_code
        content = json.loads(response.content)
        return content

    @staticmethod
    def format_url():
        service = settings.protocol + "://" + settings.ip + ":" + settings.gnocchi
        return service
