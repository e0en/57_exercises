#!/usr/bin/env python
import hashlib
import sqlite3
import time
import urllib.request

from sanic import Sanic
from sanic import response
import ujson as json


FILENAME_PREFIX = '54_url_shortener'
conn = sqlite3.connect(f'{FILENAME_PREFIX}.db')
app = Sanic()


def init_db():
    with open(f'{FILENAME_PREFIX}.sql') as fp:
        c = conn.cursor()
        for q in fp.readlines():
            c.execute(q)
        conn.commit()


def is_url_valid(url):
    try:
        urllib.request.Request(url)
        return True
    except:
        return False

def hash_str(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def is_short_id_in_db(short_id):
    c = conn.cursor()
    query = 'SELECT COUNT(1) from urls WHERE short_id=?'
    c.execute(query, (short_id, ))
    r = c.fetchone()
    return r[0] > 0


def generate_short_id(url):
    if not is_url_valid(url):
        return None
    hashed = hash_str(url)
    for i in range(1, len(hashed)):
        shortened = hashed[:i]
        if not is_short_id_in_db(shortened):
            return shortened
    return None


def get_short_id(url):
    c = conn.cursor()
    query = 'SELECT short_id from urls WHERE url=?'
    c.execute(query, (url, ))
    r = c.fetchone()
    if r is not None:
        return r[0]


def set_short_id(url):
    short_id = get_short_id(url)
    if short_id:
        return short_id
    return generate_short_id(url)


def get_url(short_id):
    c = conn.cursor()
    query = 'SELECT url from urls WHERE short_id=?'
    c.execute(query, (short_id, ))
    r = c.fetchone()
    if r is not None:
        return r[0]


def add_log(short_id, request):
    with conn:
        query = ('INSERT INTO logs (short_id, host_json, created_at) '
                 'VALUES (?, ?, ?)')
        d = request_to_dict(request)
        conn.execute(query, (short_id, json.dumps(d), time.time()))


def request_to_dict(request):
    d = dict()

    d['headers'] = request.headers
    d['ip'] = request.ip
    d['port'] = request.port
    d['parsed_args'] = request.parsed_args
    d['parsed_form'] = request.parsed_form
    d['http-version'] = request.version
    d['query-string'] = request.query_string

    if request.token:
        d['token'] = request.token

    return d


@app.route('/', methods=['GET'])
async def index(request):
    request_to_dict(request)
    with open(f'{FILENAME_PREFIX}.html') as fp:
        html = fp.read()
        return response.html(html)


@app.route('/make', methods=['POST'])
async def make(request):
    url = request.form['url'][0]

    short_id = get_short_id(url)
    if short_id:
        print(url, short_id)
        next_url = app.url_for('stats', short_id=short_id)
        return response.redirect(next_url)

    short_id = set_short_id(url)
    with conn:
        query = ('INSERT INTO urls (short_id, url) VALUES (?, ?)')
        conn.execute(query, (short_id, url))
    conn.commit()

    next_url = app.url_for('stats', short_id=short_id)
    return response.redirect(next_url)


@app.route('/<short_id>/stats', methods=['GET'])
async def stats(request, short_id):
    if not is_short_id_in_db(short_id):
        return response.text('', status=404)
    url = get_url(short_id)

    c = conn.cursor()
    query = ('SELECT count(1) FROM logs WHERE short_id=?')
    c.execute(query, (short_id, ))
    r = c.fetchone()
    if r is None:
        count = 0
    else:
        count = r[0]

    result = {'url': url, 'count': count, }
    return response.json(result)


@app.route('/<short_id>', methods=['GET'])
async def forward(request, short_id):
    url = get_url(short_id)
    if url:
        add_log(short_id, request)
        return response.redirect(url)
    else:
        return response.text(f'no url for {short_id}', status=404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
