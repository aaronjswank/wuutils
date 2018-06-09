#!/usr/bin/env python3

''' Push weather data to wunderground '''

import os
import sys
from dotenv import load_dotenv, find_dotenv
from wuutils.wuutils import wupush

# ...........................
# Setup
# ...........................

# Load environment variables stored in .env file
load_dotenv(find_dotenv())

# Get environment variables for credentials
SECRET_ID = os.getenv('SECRET_ID')
SECRET_KEY = os.getenv('SECRET_KEY')


# Check that variables were loaded
if SECRET_ID is None:
    print("Please set environment variable SECRET_ID in .env")
    sys.exit(1)

if SECRET_KEY is None:
    print("Please set environment variable SECRET_KEY in .env")
    sys.exit(1)

# ...........................
# Push Weather Information
# ...........................

# Set Weather Data
# Fields:
# tempf - [temperature F]
# humidity - [%]

wdata = dict()
wdata['humidity'] = 85
wdata['tempf'] = 77.0

# Push the data to wunderground
wupush(station=SECRET_ID, password=SECRET_KEY, wdata=wdata)
