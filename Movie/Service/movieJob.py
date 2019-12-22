"""
date: 2019.12.15
author: east
function: 爬取douban的定时任务
"""
import json

from config import CONFIG
from Utils.log import log
from DAO.movie.movie import MovieInfoDao
from Movie.Spider.MovieSpider import MovieSpider

db = MovieInfoDao()


def spider_job():
    """
    爬虫任务
    """
    tags = CONFIG.TAG
    the_recommend_movie = {}
    movie_spider = MovieSpider()
    all_movie = movie_spider.get_movies()
    log.info("——————————————根据tag获取movie数据并且筛选出一部推荐电影————————————")
    for tag in tags:
        data = db.select_movie_id_by_tag(tag)
        db_movie_id = []
        if len(data) > 0:
            for item in data:
                db_movie_id.append(item.movie_id)
            for movie in all_movie[tag]:
                if int(movie['id']) not in db_movie_id:
                    the_recommend_movie[tag] = movie
                    log.info(f"本次推荐电影的index为{all_movie[tag].index(movie)}")
                    break
        else:
            the_recommend_movie[tag] = all_movie[tag][0]

    log.info("——————————————根据推荐电影的id去获取电影的详细信息——————————————————")
    for index in the_recommend_movie.keys():
        movie_dict = {}
        movie_detail = movie_spider.get_movie_detail(the_recommend_movie[index]['id'])['subject']
        log.info(f"{index}: 本次推荐 {json.dumps(movie_dict, ensure_ascii=False)}")
        if movie_detail != "null":
            movie_dict['id'] = the_recommend_movie[index]['id']
            movie_dict['tag'] = index
            movie_dict['name'] = movie_detail['title']
            movie_dict['url'] = movie_detail['url']
            movie_dict['cover'] = the_recommend_movie[index]['cover']
            movie_dict['rate'] = movie_detail['rate']
            movie_dict['playable'] = movie_detail['playable']
            movie_dict['new'] = the_recommend_movie[index]['is_new']
            movie_dict['source'] = None
            movie_dict['actors'] = movie_detail['actors']
            movie_dict['directors'] = movie_detail['directors']
            movie_dict['region'] = movie_detail['region']
            movie_dict['types'] = movie_detail['types']
            movie_dict['release_year'] = movie_detail['release_year']
            movie_dict['duration'] = movie_detail['duration']
            MovieInfoDao().insert_movie(movie_dict)
    log.info("——————————————————把推荐电影插入数据库————————————————")


if __name__ == '__main__':
    spider_job()
