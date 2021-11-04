import requests
import json

# Data as dict
data_string = {'reg': '08 C 1234', 'make':'Ford','model':'Galaxy', 'price': 1800}

# Url to send request to 
url = 'http://127.0.0.1:5000/cars'

# Sends post request, converts dict to json
response = requests.post(url, json=data_string)

# Prints server response status code
print(response.status_code)

# Prints text data
print(response.text)