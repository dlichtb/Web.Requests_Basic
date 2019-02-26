#!/usr/bin/env python

import urllib.request
import urllib.parse
import csv
#import itertools

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
    saveFile = open('tester_kaggle_fifa2018-matchStats.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
######################################################################
#    txt_file = r"kaggle_fifa2018-matchStats.txt"
#    csv_file = r"kaggle_fifa2018-matchStats.csv"
#
#    in_txt = csv.reader(open(txt_file, "rb"), delimiter = ' ')
#    out_csv = csv.writer(open(csv_file, 'wb'))
#
#    out_csv.writerows(in_txt)
##    print('done! go check your NewProcessedDoc.csv file')
######################################################################
    with open('tester_kaggle_fifa2018-matchStats.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line for line in stripped if line)
#       grouped = itertools.izip(*[lines] * 2)
        grouped = [line.split(' ') for line in lines]
        with open('kaggle_fifa2018-matchStats.csv', 'w') as out_file:
            writer = csv.writer(out_file)
#            writer.writerow(('Name of Issue', 'Issue ID'))
            writer.writerows(grouped)
######################################################################
except Exception as e:
    print(str(e))
