#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc_bmi(weight, height):
    return weight  / (height ** 2) * 703


weight = float(input("Your weight in pounds: "))
height = float(input("Your height in inches: "))

bmi = calc_bmi(weight, height)

warning_str = "You are {0}weight. You should see your doctor"

if (bmi < 18.5):
    print(warning_str.format("under"))
elif (bmi > 25):
    print(warning_str.format("over"))
else:
    print("You are within the ideal weight range")
