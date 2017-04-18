# -*- coding: utf-8 -*-

from request_api.neutron import NeutronManager

content = NeutronManager.networks_list(param='')
print content
