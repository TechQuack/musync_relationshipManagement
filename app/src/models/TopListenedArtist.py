from dataclasses import dataclass

from init_db import *


@dataclass
class TopListenedArtist(db.Model):
    user_id: int = db.Column(db.Integer, db.ForeignKey('user_music_statistic.user_id'),
                             nullable=False, primary_key=True)
    top_listened_artist: str = db.Column(db.String(255), primary_key=True, nullable=False)
    top_ranking: int = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self, top_listened_artist: str, top_ranking: int, user_id: int):
        self.top_listened_artist = top_listened_artist
        self.top_ranking = top_ranking
        self.user_id = user_id
