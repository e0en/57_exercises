#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = int(input("What is your age? "))
not_str = "" if age >= 16 else "not "

print(f"You are {not_str}old enough to legally drive.")
