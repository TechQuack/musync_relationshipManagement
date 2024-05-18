from dataclasses import dataclass

from init_db import *


@dataclass
class Feedback(db.Model):
    match_id: int
    user1_id: int
    user2_id: int
    score_user1: int
    score_user2: int

    match_id = db.Column(db.Integer, primary_key=False, unique=True)
    user1_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)
    user2_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)
    score_user1 = db.Column(db.Integer)
    score_user2 = db.Column(db.Integer)
