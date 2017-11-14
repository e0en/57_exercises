#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

names = []
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    else:
        names += [name]

winner = random.choice(names)
print(f"THe winner is... {winner}.")
