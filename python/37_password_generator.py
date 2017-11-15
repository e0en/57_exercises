#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random


def generate_password(length, sp_count, num_count):
    alpha_count = max(length - sp_count - num_count, 0)

    special_chars = random.choices(string.punctuation, k=sp_count)
    nums = random.choices(string.digits, k=num_count)
    alphabets = random.choices(string.ascii_lowercase, k=alpha_count)

    password = special_chars + nums + alphabets
    random.shuffle(password)

    return "".join(password)


length = int(input("What's the minimum length? "))
sp_count = int(input("How many special characters? "))
num_count = int(input("How many numbers? "))

password = generate_password(length, sp_count, num_count)

print("Your password is")
print(password)

