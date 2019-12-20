"""
date: 2019.12.16
author: east
function: 展示movie信息接口
"""
import json
import time
from flask import Blueprint, request
from DAO.movie.movie import MovieInfoDao

movie = Blueprint('movie', url_prefix='/api/movie', import_name=__name__)

db = MovieInfoDao()


@movie.route('/subjects', methods=['get'])
def get_subject():
    print("请求subject")
    movies = []
    res = {}
    time_array = []
    try:
        offset = int(request.args.get('offset'))
        limit = int(request.args.get('limit'))
        print(f"offset:{offset},limit:{limit}")
    except Exception:
        print("参数error")
        offset = 0
        limit = 7
    movie_info = MovieInfoDao().select_recommend_movie_limit(offset, limit)
    if movie_info != "null":
        for item in movie_info:
            time_str = time.strftime("%Y-%m-%d", time.strptime(str(item.create_time), "%Y-%m-%d %H:%M:%S"))
            if time_str not in time_array:
                time_array.append(time_str)
        for item in movie_info:
            movie_subject = {
                'tag': item.movie_tag,
                'name': item.movie_name,
                'url': item.movie_url,
                'cover': item.movie_cover,
                'rate': item.movie_rate,
                'playable': item.movie_playable,
                'new': item.movie_new,
                'source': item.movie_source,
                'actors': item.movie_actors,
                'directors': item.movie_directors,
                'region': item.movie_region,
                'types': item.movie_types.replace('[', '').replace(']', '').replace('\'', ''),
                'release_year': item.movie_release_year,
                'duration': item.movie_duration,
                'create_time': time.strftime("%Y-%m-%d", time.strptime(str(item.create_time), "%Y-%m-%d %H:%M:%S"))
            }
            movies.append(movie_subject)
        res['code'] = 200
        res['subject'] = movies
        res['timeline'] = time_array
    else:
        res['code'] = 10000
        res['subject'] = None
    return json.dumps(res, ensure_ascii=False)
