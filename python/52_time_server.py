#!/usr/bin/env python
from datetime import datetime

from sanic import Sanic
from sanic.response import json


app = Sanic()


@app.route('/')
async def index(request):
    resp = {'currentTime': datetime.now().isoformat()}
    return json(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
