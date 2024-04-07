import json

import jsonpickle

from init_db import *

from flask import Blueprint, Flask, request
from sqlalchemy import select
from src.models.MusyncUser import MusyncUser

app_route = Blueprint('app_route', __name__, template_folder='templates')


@app_route.route('/')
def hello_world():  # put application's code here
    return 'Hello World! aaaa'


@app_route.route('/getMatch', methods=['GET'])
def getMatch():
    session = Session()
    user1Id: str = request.args.get('user1')
    user2Id: str = request.args.get('user2')
    user1 = session.execute(select(MusyncUser).where(MusyncUser.user_id == int(user1Id))).first()
    user2 = session.execute(select(MusyncUser).where(MusyncUser.user_id == int(user2Id))).first()
    s = ""
    for row in user1:
        row: MusyncUser = row
        s += row.toString()
    s += "\n"
    for row in user2:
        row: MusyncUser = row
        s += row.toString()
    return s

