#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prompt import int_input


def heart_rate(age, resting_rate, intensity):
    return (((220 - age) - resting_rate) * intensity) + resting_rate


resting_rate = int_input("Enter your resting rate: ")
age = int_input("Enter your age: ")

print(f"Resting Pulse: {resting_rate} Age: {age}")
print(f"{'Intensity': <10}| Rate")
print(f"{'':-<10}|--------")
for intensity in range(55, 100, 5):
    rate = int(heart_rate(age, resting_rate, intensity * 0.01))
    intensity_str = f"{intensity}%"
    print(f"{intensity_str: <9} | {rate} bpm")
