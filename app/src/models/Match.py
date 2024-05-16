from dataclasses import dataclass

from init_db import *


@dataclass
class Match(db.Model):

    NOT_MATCH = -1
    UNKNOWN = 0
    MATCH_USER1 = 1
    MATCH_USER2 = 2
    MATCH = 3
    END_MATCH = 4

    user1_id: int
    user2_id: int
    match_compatibility: int
    status_code: int

    match_id = db.Column(db.Integer, autoincrement=True, primary_key=False)
    user1_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)
    user2_id = db.Column(db.Integer, db.ForeignKey("musync_user.user_id"), primary_key=True)
    match_compatibility = db.Column(db.Integer)
    status_code = db.Column(db.Integer)

    def __init__(self, match_id, user1_id, user2_id, match_compatibility, status_code):
        self.match_id = int(match_id)
        self.user1_id = int(user1_id)
        self.user2_id = int(user2_id)
        self.match_compatibility = int(match_compatibility)
        self.status_code = int(status_code)