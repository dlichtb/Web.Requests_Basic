#!/usr/bin/python3

import requests as req
import os
import sys

resp = req.get("https://www.nfl.com/")

print(resp.text)
