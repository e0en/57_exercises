#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from records import print_records


names = [x.strip() for x in sys.stdin.readlines()]

names.sort()
column_name = f"Total of {len(names)} names"

records = [{ column_name: x } for x in names]
print(print_records(records, [column_name]))
