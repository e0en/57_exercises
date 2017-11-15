#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_input = input("Enter a list of numbers, seperated by spaces: ")

numbers = [int(x) for x in user_input.strip().split(" ")]

even_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers += [n]
even_str = " ".join([str(x) for x in even_numbers])

print(f"The even numbers are {even_str}.")
