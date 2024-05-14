from operator import or_

from flask import Blueprint, request, jsonify
from sqlalchemy import select

from init_db import *
from src.models.Match import Match
from src.models.UserMusicStatistic import UserMusicStatistic
from src.service import RelationshipService

app_route = Blueprint('app_route', __name__, template_folder='templates')


@app_route.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app_route.route('/getMatch/<user1Id>/<user2Id>', methods=['GET'])
def getMatch(user1Id: int, user2Id: int):
    session = Session()
    match = (session.execute(select(Match)
                             .where(Match.user1_id == user1Id)
                             .where(Match.user2_id == user2Id))
             .one_or_none())
    if match is None:
        match = (session.execute(select(Match)
                                 .where(Match.user2_id == user1Id)
                                 .where(Match.user1_id == user2Id))
                 .one_or_none())
    if match is None:
        return "No match found"
    return jsonify(match)


@app_route.route('/getMatches/<userId>', methods=['GET'])
def getMatches(userId: int):
    session = Session()
    result = (session.execute(select(Match)
                              .where(or_(Match.user1_id == userId,
                                         Match.user2_id == userId)))
              .all())
    matches = [tuple(row) for row in result]
    return jsonify(matches)


@app_route.route('/postMatches', methods=['POST'])
def postMatches():
    request_data = request.get_json()
    RelationshipService.updateUserInformation(request_data)

    user_music_statistic_data = request_data["UserMusicStatistic"]
    result: UserMusicStatistic = RelationshipService.updateUserMusicInformation(user_music_statistic_data)
    return jsonify(result)
