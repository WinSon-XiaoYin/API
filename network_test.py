# -*- coding: utf-8 -*-

from http_requests import RequestMethod
from request_api.neutron import *
import json

neutron_url = "http://192.168.1.53:9696/v2.0"

# 网络列表
response = networks_list()
subnets_tmp = {}
subnets_response = RequestMethod.get(url=neutron_url, param="subnets")
subnets = json.loads(subnets_response.content)
for subnet in subnets['subnets']:
	subnets_tmp[subnet['network_id']] = [subnet['id'], subnet['cidr']]
for network in response:
	print network.keys()[0], network.values()[0], subnets_tmp.get(network.keys()[0])

# 创建网络
# data = {"network": {"name": "new_network", "admin_state_up": "true", "shared": "true"}}
# create_network(url=neutron_url, data=data)

# 显示网络详情
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# network_detail(url, param=param)

# 更新网络
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# data = {"network": {"admin_state_up": "true", "shared": "true"}}
# update_network(url=neutron_url, param=param, data=data)

# 删除网络
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# delete_network(url=neutron_url, param=param)
