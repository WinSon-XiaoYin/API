# -*- coding: utf-8 -*-

import json
from http_requests import RequestMethod

base_url = "http://10.127.2.30:8041/v1/{sub_url}"
resource_url = base_url.format(sub_url='resource')

def resource_list(url, param='generic'):
	response = RequestMethod.get(url=url, param=param)
	content = json.loads(response.content)
	return content

response = resource_list(url=resource_url)
print response
