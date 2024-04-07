from init_db import *
from src.models.TopListenedArtist import TopListenedArtist
from src.models.TopListenedMusic import TopListenedMusic


class UserMusicStatistic(db.Model):
    user_id: int
    top_listened_artist: TopListenedArtist
    top_listened_music: TopListenedMusic

    user_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)
    top_listened_artist = db.Column(db.String, db.ForeignKey("top_listened_artist.top_listened_artist"))
    top_listened_music = db.Column(db.String, db.ForeignKey("top_listened_music.top_listened_music"))
