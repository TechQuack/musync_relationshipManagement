from dataclasses import dataclass
from datetime import datetime

from flask import json

from init_db import db, func


@dataclass
class MusyncUser(db.Model):
    user_id: int
    is_certified: bool
    birthdate: datetime
    gender: str
    accepted_age_gap: int
    accepted_distance: int
    targeted_gender: str
    favorite_musician: int
    favorite_music: int
    favorite_musical_style: int

    user_id = db.Column(db.Integer, primary_key=True)
    is_certified = db.Column(db.Boolean, nullable=False)
    birthdate = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    accepted_age_gap = db.Column(db.Integer)
    accepted_distance = db.Column(db.Integer)
    targeted_gender = db.Column(db.String(50))
    favorite_musician = db.Column(db.Integer())
    favorite_music = db.Column(db.Integer())
    favorite_musical_style = db.Column(db.Integer())

    def __repr__(self):
        return '<User %r>' % self.user_id
