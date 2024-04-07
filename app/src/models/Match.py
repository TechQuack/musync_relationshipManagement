from dataclasses import dataclass

from init_db import *


@dataclass
class Match(db.Model):
    match_id: int
    user1_id: int
    user2_id: int
    match_compatibility: int
    status_code: int

    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"))
    user2_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"))
    match_compatibility = db.Column(db.Integer)
    status_code = db.Column(db.Integer)
