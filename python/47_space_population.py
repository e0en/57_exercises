#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request
import json
from records import print_records


url = "http://api.open-notify.org/astros.json"
response = request.urlopen(url)
data = json.loads(response.read())

print(f"There are {data['number']} people in space right now:\n")

print(print_records(data['people'], ['name', 'craft']))
