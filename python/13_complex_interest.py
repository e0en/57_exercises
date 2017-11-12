#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil, pow

def calculate_complex_interest(principal, rate, time, year):
    worth = principal * pow((1 + rate / 100 / time), time * year) 
    return ceil(worth * 100) / 100


principal = int(input("What is the principal amount? "))
rate = float(input("What is the rate: "))
year = int(input("What is the number of years: "))
time_msg = "What is the number of times the interest\nis compounded per year: "
time = int(input(time_msg))

for y in range(1, year + 1):
    worth = calculate_complex_interest(principal, rate, time, y)

    msg = f"After {y} years at {rate}%, " + \
        f"the investment will be worth ${worth:g}"
    print(msg)
