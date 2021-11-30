import requests
import json
import openpyxl

# URl to access.
#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2021-11-28"

# Send GET request.
response = requests.get(url)

# Parses data as JSON.
data = response.json()

# Output to console. 
#print(data)

# Create list of items in data.
listOfReports = []
for item in data["items"]:
    listOfReports.append(item["ResourceName"])

# Get URLs for each report.
for ReportName in listOfReports:
    #print(ReportName)
    url ="https://reports.sem-o.com/api/v1/documents/"+ReportName
    print(url)
    response = requests.get(url)
    aReport = response.json()


# Save to file.
filename = 'allreports.json'

# Writing JSON data.
f = open(filename, 'w')

# Converts data to JSON objects.
json.dump(data, f, indent=4)