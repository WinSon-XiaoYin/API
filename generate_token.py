import os
import requests
import json

def fetch_token():
	url = "http://192.168.1.53:35357/v2.0/tokens"
	auth = {'auth': {'tenantName': os.environ['OS_TENANT_NAME'], 'passwordCredentials': {'username': os.environ['OS_USERNAME'], 'password': os.environ['OS_PASSWORD']}}}

	response = requests.post(url, data=json.dumps(auth))
	content = json.loads(response.content)
	token = content['access']['token']['id']
	return token

def main():
	token()

if __name__ == '__main__':
	main()

