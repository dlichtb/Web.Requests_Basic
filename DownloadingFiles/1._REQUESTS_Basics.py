#!/usr/bin/env python

#	Simple REQUEST1:		Downloads an image from 'url' and saves it in a local-directory

import requests

url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/DownloadedDatasets/google.ico', 'wb').write(r.content)



#	Simple REQUEST2:		Downloads a Youtube-Page from 'url' and saves it in a local-directory

#import requests

url = 'https://www.youtube.com/watch?v=9bZkp7q19f0'
r = requests.get(url, allow_redirects=True)
open('/home/dlichtblau/Desktop/python/machineLearning/ch.2/DownloadingFiles/DownloadedDatasets/youtubeVid.ico', 'wb').write(r.content)




#	To avoid downloading an entire page, below procedure fetches the headers of a url before actually downloading it. This allows us to skip downloading files which weren't meant to be downloaded

#import requests

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

print is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0')
# >> False
print is_downloadable('http://google.com/favicon.ico')
# >> True
