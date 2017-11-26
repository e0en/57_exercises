#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request
import xml.etree.ElementTree as ET
import re
import webbrowser
import os


base_url = "https://api.flickr.com/services/feeds/photos_public.gne?tags="

tag = input("Query? ")

feed = request.urlopen(base_url + tag).read().decode('utf-8')
feed = re.sub(' xmlns="[^"]+"', '', feed, count=1)
root = ET.fromstring(feed)

all_img_urls = []
for child in root.findall('entry'):
    items =\
        [x for x in child.findall('link') if x.get('type') == 'image/jpeg']
    img_urls = [x.get('href') for x in items]
    all_img_urls += img_urls

html = "<html><head></head><body>"
html += f'<p>Photos about "{tag}"</p>'

for url in all_img_urls:
    html += f'<img src="{url}" height="150px" />'

html += "</body></html>"

filename = "delete_me.html"
with open(filename, "w") as fp:
    fp.write(html)
webbrowser.open('file://' + os.path.realpath(filename))
# os.remove(filename)
