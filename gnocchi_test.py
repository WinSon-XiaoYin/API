# -*- coding: utf-8 -*-

from request_api.gnocchi import GnocchiManger

response = GnocchiManger.resource_list(param='')
print response
