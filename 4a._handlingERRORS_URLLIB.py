#!/usr/bin/env python

###########################################################################
###	Default Python Headers:						###
###				- [User-Agent]:	Python-urllib/x.y	###
###				- 					###
###				- 					###
###				- 					###
###				- 					###
###########################################################################

# Passing a dictionary of Headers along with the REQUEST to trick conceal python-urllib from browser
import urllib.parse
import urllib.request

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
