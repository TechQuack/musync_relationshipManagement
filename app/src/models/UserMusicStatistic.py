from init_db import *


class UserMusicStatistic(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), primary_key=True)
    top_listened_artist = db.Column(db.String, db.ForeignKey("top_listened_artist.top_listened_artist"))
    top_listened_music = db.Column(db.String, db.ForeignKey("top_listened_music.top_listened_music"))
