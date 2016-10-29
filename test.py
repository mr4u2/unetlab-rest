import requests
import json

url = 'http://192.168.1.21/api/status'
method = 'GET'
response = requests.request(method, url)
print(response.content.decode("utf-8") )
payload = json.loads(response.content.decode("utf-8"))
print(payload['code'])
