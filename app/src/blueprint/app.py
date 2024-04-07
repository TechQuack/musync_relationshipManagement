import json

import jsonpickle

from init_db import *

from flask import Blueprint, Flask, request, jsonify
from sqlalchemy import select

from src.models.Match import Match
from src.models.MusyncUser import MusyncUser

app_route = Blueprint('app_route', __name__, template_folder='templates')


@app_route.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app_route.route('/getMatch', methods=['GET'])
def getMatch():
    session = Session()
    user1Id: str = request.args.get('user1')
    user2Id: str = request.args.get('user2')
    match = (session.execute(select(Match)
                             .where(Match.user1_id == int(user1Id))
                             .where(Match.user2_id == int(user2Id)))
             .one())
    for row in match:
        return jsonify(row)
