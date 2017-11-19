#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


WORD_BOUNDARIES = " '\"\n,.:;"

def is_boundary(c):
    return (c in WORD_BOUNDARIES)

def slice_text(text):
    slices = []
    first_char_code = is_boundary(text[0])
    code = (first_char_code, first_char_code)
    start = 0
    end = 0
    for (i, c) in enumerate(text):
        code = (code[1], is_boundary(c))
        if code == (True, False):
            end = i
            slices += [(True, text[start:end])]
            print(slices[-1])
            start = i
        elif code == (False, True):
            end = i
            slices += [(False, text[start:end])]
            start = i
        else:
            end = i

    return slices


def replace_words(text, src, des):
    slices = slice_text(text)
    replaced = []
    for (is_boundary, s) in slices:
        if not is_boundary and s.lower() == src.lower():
            replaced += [des]
        else:
            replaced += [s]
    return "".join(replaced)


text = "".join([x for x in sys.stdin.readlines()])
print(replace_words(text, "utilize", "use"))
