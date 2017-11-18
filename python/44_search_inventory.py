#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json


with open(sys.argv[1], "r") as fp:
    json_str = fp.read()
    data = json.loads(json_str)['products']
    data_map = {}
    for e in data:
        data_map[e['name'].lower()] = e

found = False

while not found:
    query = input("What is the product name? ").lower()

    if query in data_map:
        found = True
        e = data_map[query]
        print(f"Name: {e['name']}")
        print(f"Price: ${e['price']:.2f}")
        print(f"Quantity on hand: {e['quantity']}")
    else:
        print("Sorry, that product was not found in our inventory.")
