import flask
import requests
import json
from xlwt import *

# Url to communicate with
url = 'http://127.0.0.1:5000/cars'

# Makes request to API
response = requests.get(url)

# Returns data parsed as JSON (will be converted to python's equivalent dict)
data = response.json()

for car in data["cars"]:
    print(car)

# Write data to json file
filename = 'cars.json'
# json.dump dumps json data to file(f) and makes pretty w/ indent
if filename:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Write data to excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0

# Write to first row
ws.write(row, 0, 'reg')
ws.write(row, 1, 'make')
ws.write(row, 2, 'model')
ws.write(row, 3, 'price')
row += 1

# Write data to subsequent rows
for car in data["cars"]:
    ws.write(row, 0, 'reg')
    ws.write(row, 1, 'make')
    ws.write(row, 2, 'model')
    ws.write(row, 3, 'price')
    row += 1

w.save('cars.xls')

