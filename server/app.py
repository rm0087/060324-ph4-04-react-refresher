#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_cors import CORS

from models import music

app = Flask(__name__)
app.json.compact = False

CORS(app)

@app.get('/')
def index():
    return "Routes: GET /music - Top Ten Songs"

@app.get('/music')
def get_top_ten_songs():
    return make_response( jsonify( music ) ), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)