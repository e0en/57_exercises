#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from word_tool import slice_text


def replace_words(text, src, des):
    slices = slice_text(text)
    replaced = []
    for (is_word, s) in slices:
        if is_word and s.lower() == src.lower():
            replaced += [des]
        else:
            replaced += [s]
    return "".join(replaced)


text = "".join([x for x in sys.stdin.readlines()])
print(replace_words(text, "utilize", "use"))
