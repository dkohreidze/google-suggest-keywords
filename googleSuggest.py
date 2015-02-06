#!/usr/bin/python
# David Kohreidze
# googleSuggest.py

import xml.etree.ElementTree as ET
import requests


payload = {	'1': 'keywords+go+here',
			'2': 'keyword+research',
			'3': 'seo'	
		  }

url = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=en"

for i in payload:
	keyword = payload[i]
	r = requests.get(url, params='q='+keyword)
	print 'URL = %s'%r.url

	f = open("workFile.xml", "wb")
	f.write(r.content)
	f.close()

	tree = ET.parse('workFile.xml')
	root = tree.getroot()

	for cs in root.findall('CompleteSuggestion'):
		suggestion = cs.find('suggestion').get('data')
		print suggestion

	print " "