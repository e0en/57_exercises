#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil

def calculate_simple_interest(principal, rate, year):
    return ceil(principal * (1 + rate / 100 * year) * 100) / 100


principal = int(input("Enter the principal: "))
rate = float(input("Enter the rate of interest: "))
year = int(input("Enter the number of years: "))

for y in range(1, year + 1):
    worth = calculate_simple_interest(principal, rate, y)

    msg = f"After {y} years at {rate}%, " + \
        f"the investment will be worth ${worth:g}"
    print(msg)
