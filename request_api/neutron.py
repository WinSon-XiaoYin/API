# -*- coding: utf-8 -*-

from http_requests import RequestMethod
import json

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

def main():
	pass

if __name__ == '__mian__':
	main()