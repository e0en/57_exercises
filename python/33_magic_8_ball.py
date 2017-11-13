#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

answers = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later"
    ]

input("What's your question? ")
print(random.choice(answers))
