#!/usr/bin/env python
# -*- coding: utf-8 -*-

def enter_a(typ):
    article = "a"
    if typ[0] in "aeiou":
        article = "an"
    return f"Enter {article} {typ}: "

def take_input(typ):
    return input(enter_a(typ))

noun = take_input("noun")
verb = take_input("verb")
adjective = take_input("adjective")
adverb = take_input("adverb")

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
