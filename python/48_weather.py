#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urllib import request, parse
import json

api_key = sys.argv[1]
base_url = f"http://api.openweathermap.org/data/2.5/"

city = input("Where are you? ")
print(f"{city} weather:")

city_query = parse.quote(city)
url = base_url + f"weather?"

values = { 'q': city, 'appid': api_key }
data = parse.urlencode(values)
response = request.urlopen(url + data).read().decode('utf-8')

data = json.loads(response)
celcius = round(float(data['main']['temp']) - 273.15)

print(f"{celcius} degrees celcius")
