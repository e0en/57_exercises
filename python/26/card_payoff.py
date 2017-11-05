#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log, ceil


def calculate_months_until_paid_off(balance, apr, monthly_payment):
    dpr_plus1 = 1 + apr / 365
    coeff = -1 / 30 
    numerator = log(1 + balance / monthly_payment * (1 - dpr_plus1 ** 30))
    denominator = log(dpr_plus1)

    return ceil(coeff * numerator / denominator)


balance = int(input("What is your balance? "))
apr_percent = float(input("What is the APR on the card (as a percent)? "))
monthly_payment = int(input("What is the monthly payment you can make? "))

months = calculate_months_until_paid_off(
        balance, apr_percent / 100, monthly_payment)

print(f"It will take you {months} months to pay off this card.")
