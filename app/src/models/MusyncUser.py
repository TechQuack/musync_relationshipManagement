from flask import json

from init_db import db, func


class MusyncUser(db.Model):
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

    def toString(self) -> str:
        return "{ " + str(self.user_id) + ", " + str(self.is_certified) + ", " + str(self.birthdate) + ", " + \
            self.gender + ", " + str(self.accepted_age_gap) + ", " + str(self.accepted_distance) + ", " + \
            str(self.targeted_gender) + ", " + str(self.favorite_musician) + ", " + str(self.favorite_music) + ", " \
            + str(self.favorite_musical_style) + " }"
