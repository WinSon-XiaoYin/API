# -*- coding: utf-8 -*-

protocol = 'http'
ip = '192.168.10.10'

# ports
neutron = '9696'
keystone = '35357'
gnocchi = '8041'

# keystone
token_url = "/v2.0/tokens"

# neutron
metering_label_list_url = "/v2.0/metering/metering-labels{query}"
network_list_url = "/v2.0/networks{query}"

# gnocchi
resource_list_url = "/v1/resource{query}"
