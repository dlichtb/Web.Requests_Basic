#!/usr/bin/env python

#	GETTING FILENAME FROM A URL
#					- In cases where: Filename-Info !present in the url (i.e. url = http://url.com/download) the 'Content-Disposition'-HEADER contains Filename-Info

import requests
import re

def get_filename_from_ContentDisposition_HEADER(cd):
    """
    Get filename from URL
    """
    #url = 'http://aviaryan.in/images/profile.png'
    if url.find('/'):
        print url.rsplit('/', 1)[1]
    """
    Get filename from HEADER: Content-Disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

url = "http://google.com/favicon.ico"
r = requests.get(url, allow_redirects=True)
filename = get_filename_from_ContentDisposition_HEADER(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)
