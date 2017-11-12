#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prompt_yes_no(q):
    try:
        answer = input(q + "? ").lower()
        if answer[0] == 'y':
            return True
        return False
    except:
        return False


if prompt_yes_no("Is the car silent when you turn the key"):
    if prompt_yes_no("Are the battery terminals corroded"):
        print("Clean terminals and try again.")
    else:
        print("Replace cables and try again.")
else:
    if prompt_yes_no("Does the car make clicking sound"):
        print("Replace battery and try again.")
    else:
        if prompt_yes_no("Does the car starts incompletely"):
            print("Check your starter plug connections.")
        else:
            if prompt_yes_no("Does engine stops immediately after startup"):
                if prompt_yes_no("Does the car have fuel injection device"):
                    print("Check if the chokes open and close properly.")
                else:
                    print("Call your service center.")
            else:
                print("Sorry, I have no answer.")
