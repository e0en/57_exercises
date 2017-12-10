#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import time
import datetime

import requests
import yaml


def write_new(s, setting):
    url = setting['url']
    data = json.dumps({'text': s, 'timestamp': time.time()})
    resp = requests.post(url, data=data)
    return resp.status_code == 200


def retrieve_all(setting):
    url = setting['url']
    params = {'orderBy': '"timestamp"'}
    resp = requests.get(url, params=params)
    results = []
    if resp.status_code == 200:
        data = json.loads(resp.text)
        for d in data.values():
            results += [(d['timestamp'], d['text'])]
    results.sort(reverse=True)
    return results


if len(sys.argv) < 2:
    exit(1)

with open('accounts.yml') as fp:
    setting = yaml.load(fp.read())['firebase']
    setting['url'] = setting['databaseURL'] + '/notes.json'

if sys.argv[1] == 'new':
    msg = ' '.join(sys.argv[2:]).strip()

    if msg != '':
        if write_new(msg, setting):
            print('Your note was saved.')
elif sys.argv[1] == 'show':
    notes = retrieve_all(setting)
    for ts, txt in notes:
        date_str = datetime.datetime.fromtimestamp(ts)\
                .strftime('%Y-%m-%d')
        print(f'{date_str} - {txt}')
