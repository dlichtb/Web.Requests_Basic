#!/usr/bin/env python

###################################################
###	Generates REQUESTs for:			###
###				- https://	###
###				- http://	###
###				- ftp://	###
###				- file://	###
###				- etc		###
###################################################

import urllib.parse
import urllib.request

request_url = input(str("Please input a website to send your request to: "))
type(request_url)
#request_url_comfirmation = print("You chose to send a request to the following url: ", request_url), "	-	PRESS <Y/y or N/n: ")
#type(request_url_comfirmation)
print("");
print("You chose to send a request to: ", request_url)
print("	>>	Sending a request via PYTHON3-urllib to: ", request_url)

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
req = urllib.request.Request(request_url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
