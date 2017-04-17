# -*- coding: utf-8 -*-

ip = 'http://192.168.10.10'
base = ip + ":"

# ports
neutron = '9696'
keystone = '35357'

# services url
neutron_url = base + neutron
keystone_url = base + keystone + "/v2.0/tokens"
metering_label_list_url = neutron_url + "/v2.0/metering/metering-labels{query}"
network_list_url = neutron_url + "/v2.0/networks{query}"
