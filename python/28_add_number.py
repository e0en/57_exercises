#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input("Enter the number of inputs: "))

numbers = []
for i in range(n):
    try:
        num = int(input("Enter a number: "))
        numbers += [num]
    except:
        pass

print(f"The total is {sum(numbers)}.")

