#!/usr/bin/env python
# -*- coding: utf-8 -*-

length_feet = int(input("What is the length of the room in feet? "))
width_feet = int(input("What is the width of the room in feet? "))

square_feets = length_feet * width_feet
square_meters = square_feets * 0.09290304

print(f"You entered dimensions of {length_feet} feet by {width_feet} feet")
print("The area is")
print(f"{square_feets} square feet")
print(f"{square_meters:.3f} square meters")
