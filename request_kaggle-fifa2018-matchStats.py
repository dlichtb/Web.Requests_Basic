#!/usr/bin/env python

import urllib.request
import urllib.parse

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
    url = 'https://www.kaggle.com/mathan/fifa-2018-match-statistics#FIFA%202018%20Statistics.csv'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open('kaggle_fifa2018-matchStats.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

