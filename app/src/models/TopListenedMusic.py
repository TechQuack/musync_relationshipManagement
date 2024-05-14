from dataclasses import dataclass

from init_db import *


@dataclass
class TopListenedMusic(db.Model):
    user_id: int = db.Column(db.Integer, db.ForeignKey('user_music_statistic.user_id'),
                             nullable=False, primary_key=True)
    top_listened_music: str = db.Column(db.String(255), primary_key=True)
    artist_name: str = db.Column(db.String(255), primary_key=True)
    top_ranking: int = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self, top_listened_music: str, artist_name: str, top_ranking: int, user_id: int):
        self.top_listened_music = top_listened_music
        self.top_ranking = top_ranking
        self.artist_name = artist_name
        self.user_id = user_id
