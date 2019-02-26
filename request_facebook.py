#!/usr/bin/env python

import urllib.request
import urllib.parse
import zipfile

#url = 'http://pythonprogramming.net'
#values = {'q':'basic',
#'submit':'search'}
#
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#
#req = urllib.request.Request(url, data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()
#print(respData)

try:
    url = 'http://ipython.rossant.net/'
    filename = 'facebook.zip'
    headers = {}
#    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
    req = urllib.request.Request(url, headers = headers)
#    downloaded = urllib.request.Request(url + filename)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open('facebook_respData.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

