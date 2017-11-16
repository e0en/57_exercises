#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3


def print_records(records, key_order):
    key_lengths = {}
    for k in key_order:
        length = len(k)
        for r in records:
            if k in r:
                length = max(length, len(r[k]))
        key_lengths[k] = length
    
    header = " | ".join([f"{k: <{key_lengths[k]}}" for k in key_order])
    seperator = "-|-".join(["-" * key_lengths[k] for k in key_order])
    body = []
    for r in records:
        body += [" | ".join([f"{r[k]: <{key_lengths[k]}}" for k in key_order])]
    return "\n".join([header, seperator] + body)


def init_db(filename):
    try:
        os.remove(filename)
    except OSError:
        pass

    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute('''CREATE TABLE records
        (first_name text, last_name text, position text, separation_date text)''')

    base_query = "INSERT INTO records VALUES "
    c.execute(base_query + "('John', 'Johnson', 'Manager', '2016-12-31')")
    c.execute(base_query + "('Tou', 'Xiong', 'Software Engineer', '2016-10-15')")
    c.execute(base_query + "('Michaela', 'Michaelson', 'District Manager', '2015-12-19')")
    c.execute(base_query + "('Jake', 'Jacobson', 'Programmer', '')")
    c.execute(base_query + "('Jacquelyn', 'Jackson', 'DBA', '')")
    c.execute(base_query + "('Sally', 'Weber', 'Web Developer', '2015-12-18')")

    conn.commit()
    conn.close()


def load_db(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    records = []
    query = "SELECT first_name, last_name, position, separation_date FROM records"
    for r in c.execute(query):
        (fn, ln, pos, sd) = r
        entry = {
            "first_name": fn, 
            "last_name": ln, 
            "position": pos,
            "separation_date": sd
            }
        records += [entry]

    conn.close()
    return records
