#!/usr/bin/python
# David Kohreidze
# parseSitemap.py

import xml.etree.ElementTree as ET
import urllib2

tree = ET.parse('sitemap.xml')
root = tree.getroot()

print root.tag
print root.attrib
print " "

for url in root.findall('url'):
	loc = url.find('loc').text
	print loc