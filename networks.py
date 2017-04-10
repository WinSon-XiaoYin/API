# -*- coding: utf-8 -*-

import json
from http_requests import RequestMethod

url = "http://192.168.1.53:9696/v2.0"

def networks_list(url=url, param="networks"):
	"""
	list the networks
	"""
	response = RequestMethod.get(url=url, param=param)
	networks = json.loads(response.content)['networks']
	networks_tmp = []
	for network in networks:
		networks_tmp.append({network['id']: network['name']})
	return networks_tmp

def create_network(url=url, param="networks", data=None):
	"""
	create network
	"""
	response = RequestMethod.post(url=url, param=param, data=data)
	print response.status_code
	if response.status_code == 201:
		print "Successfully to create network!"
	else:
		content = json.loads(response.content)
		print "Error:", content['NeutronError']['message']

def network_detail(url, param):
	"""
	show network detail
	"""
	response = RequestMethod.get(url, param)
	return response.content

def update_network(url=url, param="networks", data=None):
	"""
	更新网络
	"""
	response = RequestMethod.put(url=url, param=param, data=data)
	return response.content

def delete_network(url=url, param=None):
	"""
	删除网络
	"""
	response = RequestMethod.delete(url=url, param=param)
	print response.status_code
	if response.status_code == 204:
		print "Successfully to delete network!"
	else:
		content = json.loads(response.content)
		print "Error:", content['NeutronError']['message']

# 网络列表
response = networks_list()
subnets_tmp = {}
subnets_response = RequestMethod.get(url=url, param="subnets")
subnets = json.loads(subnets_response.content)
for subnet in subnets['subnets']:
	subnets_tmp[subnet['network_id']] = [subnet['id'], subnet['cidr']]
for network in response:
	print network.keys()[0], network.values()[0], subnets_tmp.get(network.keys()[0])

# 创建网络
# data = {"network": {"name": "new_network", "admin_state_up": "true", "shared": "true"}}
# create_network(url=url, data=data)

# 显示网络详情
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# network_detail(url, param=param)

# 更新网络
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# data = {"network": {"admin_state_up": "true", "shared": "true"}}
# update_network(url=url, param=param, data=data)

# 删除网络
# network_id = "02b80f83-3696-4a28-a883-fa1d72b1b570"
# param = "networks/{network_id}".format(network_id=network_id)
# delete_network(url=url, param=param)
