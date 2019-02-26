#!/usr/bin/env python

###################################################
###	DOWNLOADING & LOADING A DATASET		###
###################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

%cd /home/dlichtblau/Desktop/python/minibook-2nd-code-master/chapter2/

!wget https://raw.githubusercontent.com/ipython-books/minibook-2nd-data/master/nyc_taxi.zip
!unzip nyc_taxi.zip

cd /home/dlichtblau/Desktop/python/minibook-2nd-code-master/chapter2/data

data_filename = 'data/nyc_data.csv'
fare_filename = 'data/nyc_fare.csv'
data = pd.read_csv(data_filename, parse_dates=['pickup_datetime', 'dropoff_datetime'])
fare = pd.read_csv(fare_filename, parse_dates=['pickup_datetime'])

########################################################################################################################################
###########################################################################
###	Making plots with matplotlibMAKING PLOTS W/ MATPLOTLIB		###
###########################################################################
# to SHOW COLUMN-NAMES:
#			data.columns

p_lng = data.pickup_longitude
p_lat = data.pickup_latitude
d_lng = data.dropoff_longitude
d_lat = data.dropoff_latitude

# to SHOW VALUES FOR 'p_lng'/'p_lat'/'d_lng'/'d_lat':
#							p_lng
#							p_lat
#							d_lng
#							d_lat

def lat_lng_to_pixels(lat, lng):
    lat_rad = lat * np.pi / 180.0
    lat_rad = np.log(np.tan((lat_rad + np.pi / 2.0) / 2.0))
    x = 100 * (lng + 180.0) / 360.0
    y = 100 * (lat_rad - np.pi) / (2.0 * np.pi)
    return (x, y)

px, py = lat_lng_to_pixels(p_lat, p_lng)

# to SHOW VALUES FOR 'px'/'py':
#				px
#				py

plt.scatter(px, py)

plt.figure(figsize=(8, 6))
plt.scatter(px, py, s=.1, alpha=.03)
plt.axis('equal')
plt.xlim(29.40, 29.55)
plt.ylim(-37.63, -37.54)
plt.axis('off')

########################################################################################################################################
###########################################################
###	DESCRIPTIVE STATISTICS w/: PANDAS & SEABORN	###
###########################################################
px.count(), px.min(), px.max()

Px.mean(), px.median(), px.std()

# INSTALL:	SEABORN
#			!conda install seaborn -q -y

import seaborn as sns
# to verify SEABORN-Version:
#				sns.__version__

data.trip_distance.hist(bins=np.linspace(0., 10., 100))
