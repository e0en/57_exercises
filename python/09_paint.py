#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil

SQUARE_METERS_PER_LITER = 9

length = int(input("Length in meters? "))
width = int(input("Width in meters? "))

square_meters = length * width
liters = ceil(square_meters / SQUARE_METERS_PER_LITER)

print(f"You will need to purchase {liters} liters of")
print(f"paint to cover {square_meters} square meters.")
