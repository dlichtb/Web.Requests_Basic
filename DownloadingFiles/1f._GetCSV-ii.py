#!/usr/bin/env python

#from io import StringIO

#import pandas as pd
#import requests
#import os, sys
import wget

#download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
#type(download_dir)
#print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
#download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
#os.makedirs(download_dir)
#move_to_download_dir = os.chdir(download_dir)
#os.chdir(download_dir_path)

#url='https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
url2 = 'https://data.world/fivethirtyeight/nfl-ticket-prices/2014-average-ticket-price.csv'
filename = wget.download(url)
