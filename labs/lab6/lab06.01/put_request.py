import requests
import json

data_string = {'make':'Ford','model':'Kuga'}

url = 'http://127.0.0.1:5000/cars/test'

response = requests.put(url, json=data_string)

print(response.status_code)

print(response.text)