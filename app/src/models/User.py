from init_db import db, func


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    is_certified = db.Column(db.Boolean, nullable=False)
    birthdate = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    gender = db.Column(db.String(50), unique=True, nullable=False)
    accepted_age_gap = db.Column(db.Integer)
    accepted_distance = db.Column(db.Integer)
    targeted_gender = db.Column(db.String(50))
    favorite_musician = db.Column(db.Integer())
    favorite_music = db.Column(db.Integer())
    favorite_musical_style = db.Column(db.Integer())
