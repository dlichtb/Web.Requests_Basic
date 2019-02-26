#!/usr/bin/env python

###########################################################
###	Load CSV-Files with the Python Standard Library	###
###########################################################

# Use of CSV-Module and reader()-Function to load CSV-file into Python
import csv
# Once loaded, CSV-File data is converted to --> Numpy-Array
import numpy

filename = 'tester_kaggle_fifa2018-matchStats.txt'
raw_data = open(filename, 'rb')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('string')
print(data.shape)

#################################################################################

###########################################
###	Load CSV-Files with NUMPY	###
###########################################

from numpy import loadtxt
from urllib import urlopen
url = '____'
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter = "_")
print(dataset.shape)

#################################################################################

###########################################
###	Load CSV-Files with PANDAS	###
###########################################

from pandas import read_csv
filename '____'
names= ['', '', '', '']# COLUMN-NAMES
data = read_csv(filename, names = names)
print(data.shape)

#################################################################################

###########################################################
###	Load CSV-Files directly from URL with PANDAS	###
###########################################################

from pandas import read_csv
url = '____'
names= ['', '', '', '']# COLUMN-NAMES
data = read_csv(url, names = names)
print(data.shape)


#from io import StringIO

#import pandas as pd
#import requests
#import os, sys

#download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
#type(download_dir)
#print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
##download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
#os.makedirs(download_dir)
##move_to_download_dir = os.chdir(download_dir)
##os.chdir(download_dir_path)

##url='https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
#url2 = 'https://data.world/fivethirtyeight/nfl-ticket-prices/2014-average-ticket-price.csv'
#s=requests.get(url2).text

##dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
#resp = requests.get(url2)
#with open('nfl_ticketPrices.csv', 'wb') as output:
#    output.write(resp.content)
##output.close()

##os.system("sudo mv countries.csv /$download_dir")

#########################################################
#	df = pd.read_csv("/path/to/CSV-Dataset/.csv")	#
#########################################################
##c=pd.read_csv(StringIO(s))

##print(c)
