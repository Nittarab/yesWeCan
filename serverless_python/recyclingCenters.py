from datetime import datetime
from botocore.vendored import requests
import json

"""
url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCA5qvG7xhHRlnoXGgqWuSSbTwIjui_fm4"
r = requests.post(url)
print(r.json())
"""

def GetRecyclingCenters():
	url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCA5qvG7xhHRlnoXGgqWuSSbTwIjui_fm4"
	location = 'Recycling Center, Barcelona'
	params = {'address':location} 
	r = requests.get(url = url, params = params)
	geocode_result = r.json()
	return geocode_result['results'][0]	