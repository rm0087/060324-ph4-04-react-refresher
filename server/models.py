from config import db
from sqlalchemy_serializer import SerializerMixin

class Song(db.Model, SerializerMixin):

    __tablename__ = 'songs_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    youtube_link = db.Column(db.String)
    # youtube_embed = db.Column(db.String)