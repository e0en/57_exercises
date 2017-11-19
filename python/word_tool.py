#!/usr/bin/env python
# -*- coding: utf-8 -*-
WORD_BOUNDARIES = " '\"\n,.:;"

def is_word(c):
    return not (c in WORD_BOUNDARIES)

def slice_text(text):
    slices = []
    first_char_code = is_word(text[0])
    code = (first_char_code, first_char_code)
    start = 0
    end = 0
    for (i, c) in enumerate(text):
        code = (code[1], is_word(c))
        if code[0] != code[1]:
            end = i
            slices += [(code[0], text[start:end])]
            start = i
        else:
            end = i

    return slices


