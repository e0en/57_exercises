#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from word_tool import slice_text

def count_words(text):
    words = [x[1] for x in slice_text(text) if x[0]]
    counts = {}
    for w in words:
        wl = w.lower()
        if wl in counts:
            counts[wl] += 1
        else:
            counts[wl] = 1
    return counts

text = "".join([x for x in sys.stdin.readlines()])
counts = sorted([(v, k) for (k, v) in count_words(text).items()])[::-1]

pad_size = max([len(x) for (_, x) in counts]) + 2

for (c, w) in counts:
    stars = "*" * c
    bullet = f"{w}:"
    print(f"{bullet: <{pad_size}}" + stars)
