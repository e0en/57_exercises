#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

current_age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like to retire? "))

current_year = date.today().year
retire_year = current_year + retire_age - current_age

print(f"It's {current_year}, so you can retire in {retire_year}")
