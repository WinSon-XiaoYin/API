import os
import requests
import json
from generate_token import fetch_token

headers = {"Accept": "application/json"}

class RequestMethod(object):
	"""
	HTTP request method
	"""

	@classmethod
	def get(cls, url, param=None):
		headers = cls.header_add_token()
		if param:
			url = url + '/' + param
		response = requests.get(url, headers=headers)
		return response

	@classmethod
	def post(cls, url, param=None, data=None):
		headers = cls.header_add_token()
		if param:
			url = url + '/' + param
		response = requests.post(url, headers=headers, data=json.dumps(data))
		return response

	@classmethod
	def put(cls, url, param=None, data=None):
		headers = cls.header_add_token()
		if param:
			url = url + '/' + param
		response = requests.put(url, headers=headers, data=json.dumps(data))
		return response

	@classmethod
	def delete(cls, url, param=None):
		headers = cls.header_add_token()
		if param:
			url = url + '/' + param
		response = requests.delete(url, headers=headers)
		return response

	@staticmethod
	def header_add_token():
		"""
		fetch a token
		"""
		token = fetch_token()
		headers['X-Auth-Token'] = token
		return headers

def main():
	pass

if __name__ == "__mian__":
	main()
