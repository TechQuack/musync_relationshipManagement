from dataclasses import dataclass
from typing import List

from init_db import *
from src.models.TopListenedArtist import TopListenedArtist
from src.models.TopListenedMusic import TopListenedMusic
from sqlalchemy.orm import Mapped


@dataclass
class UserMusicStatistic(db.Model):
    user_id: int
    top_listened_artists: Mapped[List["TopListenedArtist"]] = db.relationship("TopListenedArtist",
                                                                              backref='userMusicStatistic',
                                                                              lazy=True,
                                                                              cascade="save-update, merge, "
                                                                                      "delete, delete-orphan")

    top_listened_musics: Mapped[List["TopListenedMusic"]] = db.relationship("TopListenedMusic",
                                                                            backref='userMusicStatistic',
                                                                            lazy=True,
                                                                            cascade="save-update, merge, "
                                                                                    "delete, delete-orphan")



    user_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)

    def __init__(self, user_id: int):
        self.user_id = user_id

    def __repr__(self):
        return '<Statistic %r>' % self.user_id
