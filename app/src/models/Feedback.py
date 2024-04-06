from init_db import *


class Feedback(db.Model):
    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.relationship('User', backref="user", lazy=True)
    user2_id = db.relationship('User', backref="user", lazy=True)
    score_user1 = db.Column(db.Integer)
    score_user2 = db.Column(db.Integer)
