#!/usr/bin/env python3

from flask import make_response, jsonify
from flask_migrate import Migrate
from models import Song

from config import app, db

@app.get('/')
def index():
    return "Routes: GET /music - Top Ten Songs"

@app.get('/songs/')
def get_songs():
    song_list = Song.query.all()

    song_dicts = [song.to_dict() for song in song_list]

    return song_dicts, 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)