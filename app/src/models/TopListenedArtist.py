from init_db import *


class TopListenedArtist(db.Model):
    top_listened_artist = db.Column(db.String(255), primary_key=True)
    top_ranking = db.Column(db.Integer, nullable=False)
