#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil

euros = int(input("How many Euros are you exchanging? "))
rate = float(input("What is the exchange rate? "))

dollars = ceil(euros * rate) / 100
msg = f"{euros} Euros at an exchange rate of {rate:.2f} is" +\
    f"\n{dollars:.2f} dollars"

print(msg)
