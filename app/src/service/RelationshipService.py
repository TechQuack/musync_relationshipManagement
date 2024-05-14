from typing import List

from sqlalchemy import select

from init_db import Session
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
