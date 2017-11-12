#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

for i in range(1, 58):
    dirname = f"{i:02d}"
    files = os.listdir(dirname)
    for f in files:
        if f.endswith(".py"):
            src = dirname + "/" + f
            des = dirname + "_" + f
            os.replace(src, des)
