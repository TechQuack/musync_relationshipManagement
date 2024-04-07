from init_db import *


class TopListenedMusic(db.Model):
    top_listened_music: str
    artist_name: str
    top_ranking: int

    top_listened_music = db.Column(db.String(255), primary_key=True)
    artist_name = db.Column(db.String(255))
    top_ranking = db.Column(db.Integer, nullable=False)
