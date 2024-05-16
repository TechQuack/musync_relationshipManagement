from operator import or_, and_

from flask import Blueprint, request, jsonify
from sqlalchemy import select

from init_db import *
from src.models.Match import Match
from src.models.MusyncUser import MusyncUser
from src.models.UserMusicStatistic import UserMusicStatistic
from src.service import RelationshipService

app_route = Blueprint('app_route', __name__, template_folder='templates')


@app_route.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app_route.route('/getMatch/<user1Id>/<user2Id>', methods=['GET'])
def getMatch(user1Id: int, user2Id: int):
    session = Session()
    match: Match = session.query(Match).where(
        or_(and_(Match.user1_id == user1Id, Match.user2_id == user2Id),
            and_(Match.user1_id == user2Id, Match.user2_id == user1Id))).first()
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
    if len(result) == 0:
        return "No match found"
    matches = [tuple(row) for row in result]
    return jsonify(matches)


@app_route.route('/postMatches', methods=['POST'])
def postMatches():
    request_data = request.get_json()
    user: MusyncUser = RelationshipService.updateUserInformation(request_data)

    user_music_statistic_data = request_data["UserMusicStatistic"]
    userMusicStatistic: UserMusicStatistic = (
        RelationshipService.updateUserMusicInformation(user_music_statistic_data))
    combinations = RelationshipService.getAllPossibleCombination(user)
    matches = RelationshipService.filterByMusicTaste(combinations, userMusicStatistic)
    RelationshipService.saveMatches(matches)
    return jsonify(matches)


@app_route.route('/updateMatch', methods=['PUT'])
def updateMatch():
    request_data = request.get_json()
    match_id: int = request_data["match_id"]
    user_id: int = request_data["user_id"]
    has_matched: bool = request_data["has_matched"]
    match: Match = RelationshipService.updateStatus(match_id, user_id, has_matched)
    if match is None:
        return "No match found", 404
    return jsonify(match)


@app_route.route('/deleteMatch/<matchId>', methods=['DELETE'])
def deleteMatch(matchId: int):
    session = Session()
    match = session.query(Match).where(Match.match_id == matchId).first()
    if match is None:
        return "No match found", 404
    session.delete(match)
    session.commit()
    session.close()
    return jsonify(match)
