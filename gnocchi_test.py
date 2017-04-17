# -*- coding: utf-8 -*-

from request_api.gnocchi import *

gnocchi_url = "http://10.127.2.30:8041/v1/{sub_url}"
resource_url = gnocchi_url.format(sub_url='resource')

response = resource_list(url=resource_url)
print response
