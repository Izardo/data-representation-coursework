# Get private info from github
import requests
import json

# Private github token
apiKey = '<token here>'
url = 'https://api.github.com/repos/izardo/aprivateone'

# Get json from private repo w/ token
response = requests.get(url, auth=('token', apiKey))
repoJSON = response.json()
#print (response.json())
file = open('get_private_github.json', 'w')
json.dump(repoJSON, file, indent=4)

print (response.status_code)