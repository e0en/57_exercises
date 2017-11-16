#!/usr/bin/env python
# -*- coding: utf-8 -*-
from records import print_records, init_db, load_db


def sort_records(records, key):
    return sorted(records, key=lambda x: x[key])


filename = "39_record.db"

init_db(filename)
records = load_db(filename)


sorted_records = sort_records(records, 'last_name')

result = []
for r in sorted_records:
    entry = {
        "Name": r["first_name"] + " " + r["last_name"],
        "Position": r["position"],
        "Separation Date": r["separation_date"]
        }
    result += [entry]


s = print_records(result, ["Name", "Position", "Separation Date"])
print(s)
