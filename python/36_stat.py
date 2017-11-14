#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt
from statistics import mean, stdev


def average(nums):
    return sum(nums) / max(1, len(nums))


response_times = []
while True:
    rt = input("Enter a number: ")
    if rt == "done":
        break
    elif rt.isnumeric():
        response_times += [int(rt)]
    else:
        print("Input must be an integer or 'done'.")

avg = mean(response_times)
minimum = min(response_times)
maximum = max(response_times)
std = stdev(response_times)

print("Numbers: " + ", ".join([str(x) for x in response_times]))
print(f"The average is {avg}.")
print(f"The minimum is {minimum}.")
print(f"The maximum is {maximum}.")
print(f"The standard deviation is {std}.")
