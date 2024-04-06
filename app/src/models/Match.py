from init_db import *


class Match(db.Model):
    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    user2_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    match_compatibility = db.Column(db.Integer)
    status_code = db.Column(db.Integer)