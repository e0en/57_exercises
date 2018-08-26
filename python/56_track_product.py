#!/usr/bin/env python
import json
import csv

from prompt import float_input


FILENAME_PREFIX = '56_track_product'


def load_json():
    try:
        with open(f'{FILENAME_PREFIX}.json') as fp:
            return json.loads(fp.read())
    except FileNotFoundError:
        return []

def save_json(data):
    with open(f'{FILENAME_PREFIX}.json', 'w') as fp:
        fp.write(json.dumps(data))


def to_csv(data):
    result = 'Name\tSerial Number\tValue\n'
    for d in data:
        result += f'{d["name"]}\t{d["serial"]}\t{d["value"]}\n'
    return result


def input_item():
    d = dict()
    d['name'] = input('Name: ')
    if not d['name']:
        return None
    d['serial'] = input('Serial number: ')
    d['value'] = float_input('Value (in $): ')

    return d


def display_items(data):
    print(to_csv(data))

if __name__ == '__main__':
    data = load_json()
    display_items(data)

    i_item = 1
    while True:
        print(f'Item {i_item}')
        new_item = input_item()
        if not new_item:
            break
        data += [new_item]

        i_item += 1
        print('')

    save_json(data)

    csv_data = to_csv(data)
    with open(f'{FILENAME_PREFIX}.csv', 'w') as fp:
        fp.write(csv_data)
