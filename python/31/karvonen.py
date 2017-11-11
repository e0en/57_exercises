#!/usr/bin/env python
# -*- coding: utf-8 -*-
def heart_rate(age, resting_rate, intensity):
    return (((220 - age) - resting_rate) * intensity) + resting_rate


def int_input(prompt):
    while True:
        result = input(prompt)
        if result.isnumeric():
            return int(result)
        else:
            print("Input must be an integer.")


resting_rate = int_input("Enter your resting rate: ")
age = int_input("Enter your age: ")

print(f"Resting Pulse: {resting_rate} Age: {age}")
print(f"{'Intensity': <10}| Rate")
print(f"{'':-<10}|--------")
for intensity in range(55, 100, 5):
    rate = int(heart_rate(age, resting_rate, intensity * 0.01))
    intensity_str = f"{intensity}%"
    print(f"{intensity_str: <9} | {rate} bpm")
