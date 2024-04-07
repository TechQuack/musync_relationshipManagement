from init_db import *


class Feedback(db.Model):
    match_id: int
    user1_id: int
    user2_id: int
    score_user1: int
    score_user2: int

    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.relationship('MusyncUser', backref="musync_user", lazy=True)
    user2_id = db.relationship('MusyncUser', backref="musync_user", lazy=True)
    score_user1 = db.Column(db.Integer)
    score_user2 = db.Column(db.Integer)
