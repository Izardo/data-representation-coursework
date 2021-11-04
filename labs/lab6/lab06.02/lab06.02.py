# 1.Write a python program that will read in a html page from a file 
#   and prints it out again 

import requests
import json

# html = '<h1>hello world</h1>This is html'
f = open("../car_viewer.html", "r")
html = f.read()
#print (html)

# 2.Modify the script to use the html2pdf.app api with the key:
#   46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad
#   6d4f1c4. The script should print out the status code of the response

# You can create an api key with an app online (as in video wk 6 lab 2)
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'
data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)
print (response.status_code)

# 3. Modify the program to write the binary data returned to a file .pdf
newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)