#!/usr/bin/env python

#	To avoid downloading an entire page, below procedure fetches the headers of a url before actually downloading it. This allows us to skip downloading files which weren't meant to be downloaded

import requests

#	FUNCTION:	Fetches HEADERs of a url before actually downloading it >> determines if HEADER(Content-Type) = TEXT/HTML.	(TEXT=FALSE, HTML=TRUE)
#					- This allows us to skip downloading files which weren't meant to be downloaded
def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

    content_length = header.get('content-length', None)
    if content_length and content_length > 2e8:  # 200 mb approx
        return False

print(is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0'))
# >> False
print(is_downloadable('http://google.com/favicon.ico'))
# >> True
