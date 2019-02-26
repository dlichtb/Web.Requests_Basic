#!/usr/bin/env python

from io import StringIO

import pandas as pd
import requests
import os, sys

download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
type(download_dir)
print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
#download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
os.makedirs(download_dir)
#move_to_download_dir = os.chdir(download_dir)
#os.chdir(download_dir_path)

#url='https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
url2 = 'https://data.world/fivethirtyeight/nfl-ticket-prices/2014-average-ticket-price.csv'
s=requests.get(url2).text

#dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
resp = requests.get(url2)
with open('nfl_ticketPrices.csv', 'wb') as output:
    output.write(resp.content)
#output.close()

#os.system("sudo mv countries.csv /$download_dir")

#########################################################
#	df = pd.read_csv("/path/to/CSV-Dataset/.csv")	#
#########################################################
#c=pd.read_csv(StringIO(s))

#print(c)
