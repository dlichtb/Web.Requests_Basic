#!/usr/bin/env python

import urllib.request
import requests
import os, sys

f = FacebookAPI(client_id = '*your app key*', client_secret = '*your app secret*'. redirect_uri = 'https://www.facebook.com')
auth_url = f.get_auth_url(scope = ['publish_stream', 'user_photos', 'user_status'])
print('connect with Facebook via: %s', % auth_url)
