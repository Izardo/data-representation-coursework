''' Write a program that stores the data for all trains in Ireland in a csv file
Use the Irish rail API '''

import requests
import csv
from bs4 import BeautifulSoup

# List of specific data to retrieve
retrieveTags = ["TrainStatus", 
                "TrainLatitude", 
                "TrainLongitude", 
                "TrainCode", 
                "TrainDate", 
                "PublicMessage", 
                "Direction"]

# Sends request to retrieve page
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

# Extracts all XML from page
soup = BeautifulSoup(page.content, 'xml')

# Extracts latitude from XML and stores in CSV file
with open("week3_train.csv", mode="w") as trainFile:
    # I dont know what this line of code means
    train_writer = csv.writer(trainFile, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    
    for listing in listings:
        lat = float(listing.TrainLatitude.string)
        if (lat < 53.4):
            entryList = []
            # Adds Train latitude data to list
            for tag in retrieveTags:
                entryList.append(listing.find(tag).string)
            train_writer.writerow(entryList)
