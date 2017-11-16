#!/usr/bin/env python
# -*- coding: utf-8 -*-
from records import print_records, init_db, load_db


def filter_records(records, query, columns):
    result = []
    for r in records:
        for c in columns:
            if query in r[c]:
                result += [r]
                break
    return result


filename = "40_record.db"

init_db(filename)
records = load_db(filename)

query = input("Enter a search string: ")

sorted_records = filter_records(records, query, ['first_name', 'last_name'])

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
