#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from records import print_records


def format_currency(x):
    return f'$ {x}'

fields = [x.strip().split(',') for x in sys.stdin.readlines()]
columns = ['Last', 'First', 'Salary']
records = [dict(zip(columns, x)) for x in fields]
print(print_records(records, columns, ''))
