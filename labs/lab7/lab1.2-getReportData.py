import requests
import json
import xlsxwriter

# URl to access.
#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2021-11-28"
# Send GET request.
response = requests.get(url)
# Parses data as JSON.
data = response.json()

# Create list of items in data.
listOfReports = []
for item in data["items"]:
    listOfReports.append(item["ResourceName"])

# Write data to excel file. 
# https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/
w = xlsxwriter.Workbook('balance.xls')
ws = w.add_worksheet()
rowNum = 0

# Write the first rowNum.
ws.write(rowNum, 0, 'StartTime')
ws.write(rowNum, 1, 'EndTime')
ws.write(rowNum, 2, "ImbalanceVolume")
ws.write(rowNum, 3, 'ImbalancePrice')
ws.write(rowNum, 4, 'ImbalanceCost')
rowNum += 1

# Get URLs for each report.

for ReportName in listOfReports:
    #print(ReportName)
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName
    #print(url)
    response = requests.get(url)
    aReport = response.json()
    for row in aReport["rows"]:
        col = 0
        # Write data to subsequent rows.
        ws.write(rowNum, col, row["StartTime"])
        ws.write(rowNum, col+1, row["EndTime"])
        # ws.write(rowNum, col+2, row["ImbalanceVolume"])
        # ws.write(rowNum, col+3, row["ImbalancePrice"])
        # ws.write(rowNum, col+4, row["ImbalanceCost"])
        rowNum += 1
w.close()
# Save to file.
filename = 'allreports.json'
# Writing JSON data.
f = open(filename, 'w')
# Converts data to JSON objects.
json.dump(data, f, indent=4)