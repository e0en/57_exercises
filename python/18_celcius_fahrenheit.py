#!/usr/bin/env python
# -*- coding: utf-8 -*-

def conv_message(unit1, unit2):
    return f"Press {unit2[0]} to convert from {unit1} to {unit2}."


def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return (c * 9 / 5) + 32


from_unit = "Fahrenheit"
to_unit = "Celcius"

print(conv_message(from_unit, to_unit))
print(conv_message(to_unit, from_unit))
choice = input("Your choice: ").upper()

if choice == 'F':
    (from_unit, to_unit) = (to_unit, from_unit)

from_temp = int(input(f"\nPlease enter the temperature in {from_unit}: "))
to_temp = c_to_f(from_temp) if choice == 'F' else f_to_c(from_temp)

print(f"The temperature in {to_unit} is {to_temp}.")

