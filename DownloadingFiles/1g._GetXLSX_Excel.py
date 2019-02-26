#!/usr/bin/env python

from io import StringIO

import pandas as pd
import requests

import zipfile
import os, sys

download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
type(download_dir)
print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
#download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
os.makedirs(download_dir)
#move_to_download_dir = os.chdir(download_dir)
#os.chdir(download_dir_path)

###########################################################################
###	Loads <SHEET-NAME> FROM '.xlsx' dataset into 'df'-dataframe	###
###########################################################################
df = pd.read_excel("/Path/to/XLSX-Dataset/.xlsx", sheetname = "<SHEET-NAME>")

print(df)
