"""
tree = ET.parse('RecyclingCenters.kml')
root = tree.getroot()

def StripTag(tag):
	return tag[len('{http://www.opengis.net/kml/2.2}'):]

def func(node):
	# print(node.tag[len('{http://www.opengis.net/kml/2.2}'):])
	tag = StripTag(node.tag)
	print(repr(tag))
	if tag == "Placemark":
		print(node)
		for child in node:
			# print(child.data)
			print(child)
	else:
		for child in node:
			# print(child.data)
			func(child)

func(root)
"""

import googlemaps
from datetime import datetime
import xml.etree.ElementTree as ET

gmaps = googlemaps.Client(key='AIzaSyCA5qvG7xhHRlnoXGgqWuSSbTwIjui_fm4')

def getRecyclingCenters():
	geocode_result = gmaps.geocode('Recycling Center, Barcelona')
	# print(len(geocode_result))
	if len(geocode_result) > 0:
		result = geocode_result[0]
		location = result['geometry']['location']
		reverse_geocode_result = gmaps.reverse_geocode((location['lat'], location['lng']))
		# print(reverse_geocode_result)
		return reverse_geocode_result[0]

# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall", "Parramatta, NSW", mode="transit", departure_time=now)

#print(getRecyclingCenter())