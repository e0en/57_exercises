#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prompt import int_input


weight = int_input("Your weight in pounds: ")
gender = input("Your gender (m/f): ").strip().lower()
hours = int_input("Hours after drink: ")
amount = int_input("Amount of drink in ounces: ")

absorbtion_ratio = 0.73 if gender == 'm' else 0.6

bac = (amount * 5.14 / weight * absorbtion_ratio) - 0.15 * hours

not_str = ""
if bac >= 0.08:
    not_str = "not "

print(f"Your BAC is {bac}")
print(f"It is {not_str}legal for you to drive")
