#!/usr/bin/env python
# -*- coding: utf-8 -*-

num_people = int(input("How many people? "))
num_pizza = int(input("How many pizzas do you have? "))
num_piece = int(input("\nHow many pieces are in a pizza? "))

num_all_piece = num_piece * num_pizza
piece_per_person = num_all_piece // num_people
num_leftover = num_all_piece - piece_per_person * num_people

person_str = "person" if num_people == 1 else "people"
pizza_str = "pizza" if num_pizza == 1 else "pizzas"
per_piece_str = "piece" if piece_per_person == 1 else "pieces"

leftover_be_str = "is" if piece_per_person == 1 else "are"
leftover_piece_str = "piece" if piece_per_person == 1 else "pieces"

print(f"{num_people} {person_str} with {num_pizza} {pizza_str}")
print(f"Each person gets {piece_per_person} {per_piece_str} of pizza")
print(f"There {leftover_be_str} {num_leftover} leftover {leftover_piece_str}")
