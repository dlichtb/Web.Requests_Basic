#!/usr/bin/env python

import urllib.request

request_url = input(str("Please input a website to send your request to: "))
type(request_url)
#request_url_comfirmation = print("You chose to send a request to the following url: ", request_url), "	-	PRESS <Y/y or N/n: ")
#type(request_url_comfirmation)
print("");
print("You chose to send a request to: ", request_url)
print("	>>	Sending a request via PYTHON3-urllib to: ", request_url)

with urllib.request.urlopen(request_url) as response:
    html = response.read()
