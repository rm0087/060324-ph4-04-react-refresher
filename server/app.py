#!/usr/bin/env python3

from flask import make_response, jsonify
from models import music

from config import app

@app.get('/')
def index():
    return "Routes: GET /music - Top Ten Songs"

@app.get('/music')
def get_top_ten_songs():
    return make_response( jsonify( music ) ), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)