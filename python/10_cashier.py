#!/usr/bin/env python
# -*- coding: utf-8 -*-

item_index = 0
items = []
while True:
    try:
        item_index += 1
        price = int(input(f"Price of item {item_index}: "))
        quantity = int(input(f"Quantity of item {item_index}: "))
        items += [(price, quantity)]
    except:
        break


subtotal = 0
for q in [x * y for x, y in items]:
    subtotal += q

tax = subtotal * 0.055
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Total: ${total:.2f}")
