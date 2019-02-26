#!/usr/bin/env python

#import urllib

#dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
#urllib.urlretrieve(dls, "text.xls")

import requests

dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
resp = requests.get(dls)
with open('te.xls', 'wb') as output:
    output.write(resp.content)
#output.close()
