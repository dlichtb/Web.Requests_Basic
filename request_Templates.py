###########################
###	GET REQUESTS	###
###########################

import urllib.request

# Create a variable(x) to send n HttpRequest to a url(https://www.google.com):	DEFAULT-Request = GET
x = urllib.request.urlopen('https://www.google.com')

# Prints out a read of the HttpRequest (return source code for url)
print(x.read())

###########################
###	POST REQUESTS	###
###########################

# Enables parsing of values for POST-HttpRequests
import urllib.parse

# variable defining url to be requested
url = 'http://pythonprogramming.net'

# variable defining a dictionary	KEYWORD/VARIABLE:VALUE
#	1 VARIABLE IN DICTIONARY:
#		variable1: s = basic
values = {'q':'basic'}

#	2+ VARIABLES IN DICTIONARY:
#		variable1: s 	  = basic
#		variable2: submit = search
#values = {'q':'basic',
#	  'submit':'search'}

# Parse url and Encodes values, using 'urlencode' to encode values as they are in url-code(UTF-8)
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

# Send request for specified url AND specified variables
req = urllib.request.Request(url, data)

# Visit & Get response
resp = urllib.request.urlopen(req)

# Reads
respData = resp.read()

print(respData)

#################################################
#################################################
#################################################

###########################
###	EXAMPLE		###
###########################

# Test a search for a url(https://www.google.com) (i.e. HttpRequest), with variabl1(q = query for google) = 'test'
#	- Equivalent to going to www.google.com, typing 'test' in search bar
try:
	x = urllib.request.urlopen('https://www.google.com/search?q=test'

	print(x.read())
# 	Exception to print out exceptions if HttpRequest fails (HTTP ERROR 403)(website recognizes code instead of legit user and blocks request - bypass this with an API when possible)
except Exception as e:
	print(str(e))


try:
	url = 'https://www.google.com/search?q=test'

	headers = {}
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req = urllib.request.Request(url, headers = headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	saveFile = open('withHeaders.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()
except Exception as e:
	print(str(e))
