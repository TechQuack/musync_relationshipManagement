import datetime
from datetime import datetime
from operator import and_, or_
from typing import List
from sqlalchemy import desc

from sqlalchemy import select

from init_db import Session
from src.models.Feedback import Feedback
from src.models.Match import Match
from src.models.MusyncUser import MusyncUser
from src.models.UserMusicStatistic import UserMusicStatistic


def updateUserInformation(data) -> MusyncUser:
    session = Session()
    user_id = data["MusyncUser"]['user_id']
    is_certified = data["MusyncUser"]['is_certified']
    birthdate = data["MusyncUser"]['birthdate']
    gender = data["MusyncUser"]['gender']
    accepted_age_gap = data["MusyncUser"]['accepted_age_gap']
    accepted_distance = data["MusyncUser"]['accepted_distance']
    targeted_gender = data["MusyncUser"]['targeted_gender']
    favorite_musician = data["MusyncUser"]['favorite_musician']
    favorite_music = data["MusyncUser"]['favorite_music']
    favorite_musical_style = data["MusyncUser"]['favorite_musical_style']
    musyncUser = MusyncUser(user_id, is_certified, birthdate, gender, accepted_age_gap
                            , accepted_distance, targeted_gender,
                            favorite_musician, favorite_music, favorite_musical_style)
    session.merge(musyncUser)
    session.commit()
    session.close()
    return musyncUser


def updateUserMusicInformation(data) -> UserMusicStatistic:
    from src.models.TopListenedArtist import TopListenedArtist
    from src.models.TopListenedMusic import TopListenedMusic
    session = Session()
    user_id = data['user_id']
    userMusicStatistic: UserMusicStatistic = UserMusicStatistic(user_id)
    session.merge(userMusicStatistic)
    top_listened_artists = data['top_listened_artist']
    top_listened_musics = data['top_listened_music']
    artists: List[TopListenedArtist] = list()
    for artist in top_listened_artists:
        top_listened_artist = artist["top_listened_artist"]
        top_ranking = artist["top_ranking"]
        newArtist = TopListenedArtist(top_listened_artist, top_ranking, user_id)
        artists.append(newArtist)
        session.merge(newArtist)
        session.commit()
    userMusicStatistic.top_listened_artists = artists
    session.merge(userMusicStatistic)
    session.commit()
    musics: List[TopListenedMusic] = list()
    for music in top_listened_musics:
        top_listened_music = music["top_listened_music"]
        top_ranking = music["top_ranking"]
        artist_name = music["artist_name"]
        newMusic = TopListenedMusic(top_listened_music, artist_name, top_ranking, user_id)
        musics.append(newMusic)
        session.merge(newMusic)
        session.commit()
    userMusicStatistic.top_listened_musics = musics
    session.merge(userMusicStatistic)
    session.commit()
    session.close()
    return userMusicStatistic


def getAllPossibleCombination(user: MusyncUser) -> List[Match]:
    if user.is_certified:
        return list()
    session = Session()
    userTargetedGender = user.targeted_gender
    userAge = __getUserAge(session.query(MusyncUser.birthdate).filter(MusyncUser.user_id == user.user_id)
                           .one())
    userAgeGap = user.accepted_age_gap
    userDistanceGap = user.accepted_distance
    userLocation = 0  # TODO
    users = session.query(MusyncUser).filter(MusyncUser.user_id != user.user_id).all()
    matches: List[Match] = list()
    match_id: int = 0
    match = session.query(Match.match_id).order_by(desc(Match.match_id)).limit(1).first()
    if match is not None:
        match_id = match.match_id + 1
    for musyncUser in users:
        if musyncUser.gender == userTargetedGender and __getUserAge(musyncUser) - userAge <= userAgeGap \
                and not musyncUser.is_certified:
            match: Match = Match(match_id, user.user_id, musyncUser.user_id, 50,
                                 Match.MATCH_USER1)
            match_id += 1
            matches.append(match)
    session.close()
    return matches


def filterByMusicTaste(combinations: List[Match], userStatistic: UserMusicStatistic) -> List[Match]:
    session: Session = Session()
    result: List[Match] = list()
    for combination in combinations:
        user2Id = combination.user2_id
        userStatistic2 = (session.query(UserMusicStatistic).filter(UserMusicStatistic.user_id == user2Id)
                          .one())
        compatibility = evaluateCompatibility(userStatistic, userStatistic2)
        if compatibility > 50:
            combination.match_compatibility = compatibility
            result.append(combination)
    session.close()
    return result


def evaluateCompatibility(userStatistic: UserMusicStatistic, userStatistic2: UserMusicStatistic) -> int:
    from src.models.TopListenedArtist import TopListenedArtist
    from src.models.TopListenedMusic import TopListenedMusic
    topListenedArtist1: List[TopListenedArtist] = userStatistic.top_listened_artists
    topListenedArtist2: List[TopListenedArtist] = userStatistic2.top_listened_artists
    result: int = 0
    topListenedArtist2Names = [artist.top_listened_artist for artist in topListenedArtist2]
    for artist in topListenedArtist1:
        if artist.top_listened_artist in topListenedArtist2Names:
            if artist.top_ranking == 1:
                result += 25
            elif artist.top_ranking == 2:
                result += 10
            else:
                result += 5
    topListenedMusic1: List[TopListenedMusic] = userStatistic.top_listened_musics
    topListenedMusic2: List[TopListenedMusic] = userStatistic2.top_listened_musics
    topListenedMusic2Artists = [music.artist_name for music in topListenedMusic2]
    topListenedMusic2Musics = [music.top_listened_music for music in topListenedMusic2]
    for music in topListenedMusic1:
        if (music.top_listened_music in topListenedMusic2Musics
                and music.artist_name in topListenedMusic2Artists):
            if music.top_ranking == 1:
                result += 25
            elif music.top_ranking == 2:
                result += 10
            else:
                result += 5
        elif music.artist_name in topListenedMusic2Artists:
            if music.top_ranking == 1:
                result += 10
            elif music.top_ranking == 2:
                result += 6.5
            else:
                result += 3.5
    return result


def saveMatches(matches: List[Match]):
    session: Session = Session()
    for match in matches:
        session.merge(match)
        session.commit()
    session.close()


def updateStatus(match_id: int, user_id: int, status: bool) -> Match | None:
    session = Session()
    if status:
        newStatus = Match.MATCH
    else:
        newStatus = Match.END_MATCH
    match = session.query(Match).where(and_(Match.match_id == match_id,
                                            or_(Match.user1_id == user_id, Match.user2_id == user_id))
                                       )
    if match.first() is None:
        return None
    match.update({'status_code': newStatus})
    session.commit()
    session.close()
    return match.first()


def changeFeedback(match_id: int, user_id: int, score: int) -> Feedback | None:
    session = Session()
    match: Match = session.query(Match).where(Match.match_id == match_id).first()
    if match is None:
        return None
    feedback = session.query(Feedback).where(Feedback.match_id == match_id).first()
    score_user1: int = 0
    score_user2: int = 0
    if feedback is not None:
        score_user1 = feedback.score_user1
        score_user2 = feedback.score_user2
    if user_id == match.user1_id:
        feedback = Feedback(match_id=match_id, user1_id=match.user1_id, user2_id=match.user2_id,
                            score_user1=score, score_user2=score_user2)
    elif user_id == match.user2_id:
        feedback = Feedback(match_id=match_id, user1_id=match.user1_id, user2_id=match.user2_id,
                            score_user1=score_user1, score_user2=score)
    else:
        return None
    session.merge(feedback)
    session.commit()
    session.close()
    return feedback

def __getUserAge(user: MusyncUser):
    userAge = datetime.now() - user.birthdate.replace(tzinfo=None)
    return userAge.days / 365
