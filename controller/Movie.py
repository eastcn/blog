"""
date: 2019.12.16
author: east
function: 展示movie信息接口
"""
from flask import Blueprint
from DAO.movie.movie import MovieInfoDao

movie = Blueprint('movie', url_prefix='/api/movie', import_name=__name__)

db = MovieInfoDao()


@movie.route('/subject')
def get_subject():
    print("请求subject")
    movie_info = MovieInfoDao().select_recommend_movie()
    movie_subject = {}
    res = {}
    if movie_info is not "null":
        for item in movie_info:
            movie_subject['tag'] = item.movie_tag
            movie_subject['name'] = item.movie_name
            movie_subject['url'] = item.movie_url
            movie_subject['cover'] = item.movie_cover
            movie_subject['rate'] = item.movie_rate
            movie_subject['playable'] = item.movie_playable
            movie_subject['new'] = item.movie_new
            movie_subject['source'] = item.movie_source
            movie_subject['actors'] = item.movie_actors
            movie_subject['directors'] = item.movie_directors
            movie_subject['region'] = item.movie_region
            movie_subject['types'] = item.movie_types
            movie_subject['release_year'] = item.movie_release_year
            movie_subject['duration'] = item.movie_duration
        res['code'] = 200
        res['subject'] = movie_subject
    else:
        res['code'] = 10000
        res['subject'] = None
    return "get subject"
