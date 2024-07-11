#!/usr/bin/env python3

from flask import make_response, jsonify
from models import Song

from config import app

@app.get('/')
def index():
    return "Routes: GET /music - Top Ten Songs"

if __name__ == '__main__':
    app.run(port=5555, debug=True)