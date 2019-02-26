#!/usr/bin/env python

#	GETTING A ZIP-FILE FROM A URL

#import urllib
#import urllib2
import requests
import os, sys

download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
type(download_dir)
print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
#download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
os.makedirs(download_dir)
#move_to_download_dir = os.chdir(download_dir)
#os.chdir(download_dir_path)

#url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
url2 = 'https://github.com/ryurko/nflscrapR-data.git'

print("downloading with {requests}")
r = requests.get(url2)
#with open("url_www.blog.pythonlibrary.org.zip", "wb") as code:# for url
with open("github_nfl.zip", "wb") as code:# for url2
    code.write(r.content)

###########################################
###	Read the .zip into Python	###
###########################################
#import zipfile
#archive = zipfile.ZipFile('<FILENAME>.zip', 'r')
#df = archive.read('<FILENAME>.csv')

#	{urllib}:
#	 ------
#print("downloading with {urllib}")
#urllib.urlretrieve(url, "code.zip")
#
#urllib.urlretrieve(url, "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/DownloadedDatasets/code.zip")


#	{urllib2}:	open the url and then read it and write the data out
#	 -------
#print("downloading with {urllib2}")
#f = urllib2.urlopen(url)
#with open("code.zip", "wb") as code:
#    code.write(f.read())
#
#with open("/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/DownloadedDatasets/code2.zip", "wb") as code:
#    code.write(f.read())

#	{request}:	library method is:	GET(HTTP GET)	-->	Call REQUESTed-Object(Content-Property) to get Desired-File	-->	withopen(filename, "wb") as...)
#	 -------		1. GET(REQUESTed-Object)
#				  2. Call REQUESTed-Object(Content-Property)	--> Gets the desired data
#		  		    3. 'with open()'
#
#			- better to read 'filename' in pieces/segments:
#									- by passing read(<size>) Functionality
