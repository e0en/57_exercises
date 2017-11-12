#!/usr/bin/env python
# -*- coding: utf-8 -*-
def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Bad input, please type numbers only")
            pass
