#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

import requests


BASE_URL = 'http://www.omdbapi.com/'


def rating_msg(rating):
    if rating > 80:
        return 'You should watch this movie right now!\n'
    elif rating < 50:
        return 'Avoid this movie at all cost!\n'
    else:
        return ''


api_key = sys.argv[1]

title = input('Enter the name of a movie: ')

data = {'apikey': api_key, 't': title}
r = requests.get(BASE_URL, data)

if r.status_code == requests.status_codes.codes.ok:
    movie_data = json.loads(r.text)
    if 'Error' in movie_data:
        print(movie_data['Error'])
        exit(1)

    print(f'\nTitle: {movie_data["Title"]}')
    print(f'Year: {movie_data["Year"]}')
    print(f'Rating: {movie_data["Rated"]}')
    print(f'Running Time: {movie_data["Runtime"]}')
    print(f'\nDescription: {movie_data["Plot"]}')

    print('\n' + rating_msg(int(movie_data['Metascore'])), end="")
else:
    print(r)
