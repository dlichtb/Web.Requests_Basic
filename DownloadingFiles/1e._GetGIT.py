#!/usr/bin/env python

import os, sys

download_dir = input(str("Enter directory to download repository into [ /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/]: "))
type(download_dir)
print("You chose to make a GIT-Repository in the following directory:	/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/", download_dir)
#download_dir_path = "/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/" + download_dir
os.makedirs(download_dir)
#move_to_download_dir = os.chdir(download_dir)
#os.chdir(download_dir_path)

#1a. Configure github-UserName:
#-----------------------------
#########################git config --global user.name "danlich88"

#1b. Configure github-UserEmail:
#------------------------------
#%git config --global user.email danlich88@gmail.com

#2. Start GitHub-Repository:
#--------------------------
#########################git init

#3a. Create a working copy of a local repository:
#-----------------------------------------------
#%cd /home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/git1_1stProject
#########################url = 'https://github.com/jivoi/awesome-ml-for-cybersecurity.git'
#########################git clone https://$url $download_directory

#3b. For Accessing a Remote-Server:
#---------------------------------
#%git clone username@host:/path/to/repository

#4.	ADDING FILES:
#--------------------
#	A)	%git add <filename>
#	B)	%git add *
