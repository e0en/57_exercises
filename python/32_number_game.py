#!/usr/bin/env python
# -*- coding: utf-8 -*-
from prompt import int_input
from random import randint


def score_msg(count):
    if count <= 1:
        msg = "You're a mind reader!"
    elif count <= 4:
        msg = "Most impressive."
    elif count <= 6:
        msg = "You can do better than that"
    else:
        msg = "Better luck next time"
    return msg


def play_game(num):
    user_inputs = set()
    iter_count = 1
    while True:
        if iter_count == 1:
            prompt = "I have my number. What's your guess? "
        else:
            prompt = "Guess again: "

        user_input = input(prompt)
        
        if not user_input.isnumeric():
            response = "Not a number."
        else:
            user_num = int(user_input)

            if user_num in user_inputs:
                response = "Duplicate answer."
            elif user_num > num:
                response = "Too high."
            elif user_num < num:
                response = "Too low."
            else:
                print(f"You got it in {iter_count} guesses!")
                print(score_msg(iter_count))
                break

            user_inputs.add(user_num)
            print(response, end=" ")
        iter_count += 1


print("let's play guess the Number.")
while True:
    level = int_input("Pick a difficulty level (1, 2, or 3): ")
    num = randint(1, 10 ** level)
    play_game(num)
    
    play_again = input("Play again? ")
    if play_again != 'y':
        print("Goodbye!")
        break
