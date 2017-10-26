#!/usr/bin/env python
# -*- coding: utf-8 -*-

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

add_str = f"{num1} + {num2} = {num1 + num2}"
sub_str = f"{num1} - {num2} = {num1 - num2}"
mul_str = f"{num1} * {num2} = {num1 * num2}"
div_str = f"{num1} / {num2} = {num1 // num2}"

print("\n".join([add_str, sub_str, mul_str, div_str]))
