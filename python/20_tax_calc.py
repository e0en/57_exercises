#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_state_tax(amount, state):
    rate = 0.055
    if state == "illinois":
        rate = 0.08
    return rate * amount


def calc_county_tax(amount, county):
    rate = 0.0
    if state == "wisconsin":
        if county == "eau claire":
            rate += 0.005
        elif county == "dunn":
            rate += 0.004
    return rate * amount


amount = int(input("What is the order amount? "))
state = input("What state do you live in? ").lower()
county = input("What county do you live in? ").lower()

state_tax = calc_state_tax(amount, state)
county_tax = calc_county_tax(amount, county)
total_tax = state_tax + county_tax
total = amount + total_tax

msg = f"The total is ${total:.2f}"

if state == "illinois" or state == "wisconsin":
    tax_msgs = [
        f"The state tax is ${state_tax:.2f}.",
        f"The county tax is ${county_tax:.2f}.",
        f"The total tax is ${total_tax:.2f}.",
        ]
    msg = "\n".join(tax_msgs) + "\n" + msg

print(msg)
