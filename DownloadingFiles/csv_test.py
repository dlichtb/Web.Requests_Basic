#!/usr/bin/env python

# Load CSV from Online-URL via Python Standard Library
######################################################
import csv
import numpy

filename = "_____.csv"
raw_data = open(filename, 'rt')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)

################################################################################
#
# Load a locally-stored-CSV
###########################
#import numpy
#
#filename = "_____.csv"
#raw_data = open(filename, 'rt')
#data = numpy.loadtxt(raw_data, delimiter = ",")
#print(data.shape)
#
#######################################
#
# Load CSV from Online-URL
##########################
#from numpy import loadtext
#from urllib.request import urlopen
#
#url = ""
#
#raw_data = urlopen(url)
#dataset = loadtext(raw_data, delimiter = ",")
#print(dataset.shape)
