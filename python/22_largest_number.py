#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num 


numbers = []

while True:
    try:
        number = int(input("Enter the number: "))
        if number in numbers:
            print(f"{number} is already used.")
        else:
            numbers += [number]
    except:
        max_num = find_max(numbers)
        print(f"The largest number is {max_num}")
        break
