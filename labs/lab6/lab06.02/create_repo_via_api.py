## Program updates a repo name on github
## Good tutorial: https://realpython.com/python-requests/

import requests
import json

# Private github token & url
apiKey = '<token here>'
url = 'https://api.github.com/repos/izardo/aprivateone'

# Changes name of repo
payload = '{"name" : "HERRO"}'
response = requests.post(url, auth=('token', apiKey), data = payload)

repoJSON = response.json()
print (response.json())
#file = open('get_private_github.json', 'w')
#json.dump(repoJSON, file, indent=4)

print (response.status_code)