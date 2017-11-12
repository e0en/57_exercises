#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nonzero_input(prompt):
    while True:
        result = input(prompt)
        if not result.isnumeric():
            print("Sorry, that is not a valid input.")
        elif int(result) == 0:
            print("Zero is not a valid input.")
        else:
            return int(result)


rate = nonzero_input("What is the rate of return? ")

double_years = 72 // rate
print(f"It will take {double_years} years to double your initial investment.")
