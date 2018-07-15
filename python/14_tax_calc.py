#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_state_tax(amount):
    rate = 0.055
    return rate * amount


amount = int(input('What is the order amount? '))
state = input('What is the state? ').lower()

tax = calc_state_tax(amount)
total = amount + tax

if state.startswith('wi'):
    print(f'The subtotal is ${amount:.2f}')
    print(f'The tax is ${tax:.2f}')

print(f'The total is ${total:.2f}')
