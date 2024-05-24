from operator import or_, and_

import jsonpickle
from flask import Blueprint, request, jsonify
from jsonpickle import json
from sqlalchemy import select
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from init_db import *
from src.models.Feedback import Feedback
from src.models.Match import Match
from src.models.MusyncUser import MusyncUser
from src.models.UserMusicStatistic import UserMusicStatistic
from src.service import RelationshipService

app_route = Blueprint('app_route', __name__, template_folder='templates')

TOPICS = ['MATCH']
BOOTSTRAP_SERVERS = ['kafka:9092']

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS, value_serializer=lambda m: json.dumps(m).encode('ascii'))
consumer = KafkaConsumer('MATCH', bootstrap_servers=BOOTSTRAP_SERVERS,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         auto_offset_reset='earliest', enable_auto_commit=True, group_id='test')


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
    producer.send("MATCH", value=jsonpickle.encode(match))
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


@app_route.route('/getFeedback/<feedbackId>', methods=['GET'])
def getFeedback(feedbackId: int):
    session = Session()
    feedback: Feedback = session.query(Feedback).where(Feedback.match_id == feedbackId).first()
    if feedback is None:
        return "No feedback found", 404
    session.close()
    return jsonify(feedback)


@app_route.route('/postFeedback', methods=['POST'])
def postFeedback():
    request_data = request.get_json()
    match_id: int = request_data["match_id"]
    user_id: int = request_data["user_id"]
    score: int = request_data["score"]
    feedback: Feedback = RelationshipService.changeFeedback(match_id, user_id, score)
    if feedback is None:
        return "Error, the user is not concerned by this match", 403
    return jsonify(feedback)


@app_route.route('/updateUserInformation', methods=['PUT'])
def updateUserInformation():
    request_data = request.get_json()
    user: MusyncUser = RelationshipService.updateUserInformation(request_data)
    return jsonify(user)


@app_route.route('/updateUserMusicStatisticInformation', methods=['PUT'])
def updateUserMusicStatisticInformation():
    request_data = request.get_json()
    user_music_statistic_data = request_data["UserMusicStatistic"]
    user_id = user_music_statistic_data["user_id"]
    session: Session = Session()
    user = session.query(MusyncUser).where(MusyncUser.user_id == user_id).first()
    if user is None:
        return "No user found", 404
    userMusicStatistic: UserMusicStatistic = (
        RelationshipService.updateUserMusicInformation(user_music_statistic_data))
    return jsonify(userMusicStatistic)
