#!/usr/bin/env python

import os, sys

###################################
###	CREATE SIGNING-KEYS	###
###################################

#	Creating a CA-CERTificate directory
mkdir -p /home/dlichtblau/efi.sign/ca
#	Creating CERTificate-Database
certutil -d /home/dlichtblau/efi.sign/ca -N

#	Create a Self-Signed-CERTificate
efikeygen -d /home/dlichtblau/efi.sign/ca --ca --self.sign --nickname="EUFI Test CA" --common-name="CN=UEFI Test CA, OU=OTC,O=Intel Corporation,C=FI" --url="http://www.intel.com" --serial=00

#	(Creating-CERTificate) & (Signing-CERTificate)
efikeygen -d /home/dlichtblau/efi.sign/ca --signer="UEFI Test CA" --nickname="EUFI Secure Boot Signer" --common-name="CN=UEFI Secure Boot Signer,OU=OTC,O=Intel Corporation,C=FI" --url="http://www.intel.com" --serial=01

###########################################################################
###	Default Python Headers:						###
###				- [User-Agent]:	Python-urllib/x.y	###
###				- 					###
###				- 					###
###				- 					###
###				- 					###
###########################################################################

request_url = input(str("Please input a website to send your request to: "))
type(request_url)
#request_url_comfirmation = print("You chose to send a request to the following url: ", request_url), "	-	PRESS <Y/y or N/n: ")
#type(request_url_comfirmation)
print("");
print("You chose to send a request to: ", request_url)
print("	>>	Sending a request via PYTHON3-urllib to: ", request_url)

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
headers = {"User-Agent": user_agent}
values = {'name' : '<DESIRED_NAME_VALUE', 'location': '<DESIRED_LOCATION_VALUE>', 'language' : '<DESIRED_LANGUAGE_VALUE>'}
###################################################################################################
###	If we wanted to passed data with the request:						###
###						data = {}					###
###						data = ['name'] = '______'			###
###						data = ['location'] = '______'			###
###						data = ['language'] = '______'			###
###						url_values = urllib.parse.urlencode(data)	###
###						print(url_values)				###
###						full_url = url + "?" + url_values		###
###						data = urllib.request.urlopen(full_url)		###
###################################################################################################

data = urllib.parse.urlencode(values)
data = data.encode('ascii')# Data should be in bytes
req = urllib.request.Request(request_url, data, headers)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
