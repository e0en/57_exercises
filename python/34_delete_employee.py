#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def print_employees(names):
    is_are = 'is' if len(names) == 1 else 'are'
    s = '' if len(names) == 1 else 's'
    print(f"There {is_are} {len(names)} employee{s}:")
    for name in names:
        print(name)


names = []
filename = sys.argv[1]
with open(filename) as fp:
    line = fp.readline().strip()
    while line:
        if line != "":
            names += [line]
        line = fp.readline().strip()

print_employees(names)

del_name = input("Enter an employee name to remove: ")
updated_names = []
for name in names:
    if name != del_name:
        updated_names += [name]

print_employees(updated_names)

with open(filename, "w") as fp:
    for name in updated_names:
        fp.write(name + "\n")
