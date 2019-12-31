"""
date: 2019.12.16
author: east
function: 对movie表进行操作
"""
import json
import traceback
from Utils.utils import true_or_false
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.movie.movieInfo import MovieInfo
from config import CONFIG


class MovieInfoDao:
    def __init__(self):
        self.engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
        self.session = sessionmaker(self.engine)

    def select_recommend_movie(self):
        """
        从数据库中检索
        """
        session = self.session()
        try:
            data = session.query(MovieInfo).order_by(MovieInfo.create_time.desc()).limit(1).all()
            return data
        except Exception:
            print("检索数据库出错error")
            traceback.print_exc()
            return "null"
        finally:
            session.close()

    def select_all_recommend_movie(self):
        """
        从数据库中检索
        """
        session = self.session()
        try:
            data = session.query(MovieInfo).order_by(MovieInfo.create_time.desc()).all()
            return data
        except Exception:
            print("检索数据库出错error")
            traceback.print_exc()
            return "null"
        finally:
            session.close()

    def select_recommend_movie_limit(self, offset, limit):
        """
        从数据库中检索, 根据分页
        """
        session = self.session()
        try:
            data = session.query(MovieInfo).order_by(MovieInfo.create_time.desc()).limit(limit).offset(offset).all()
            return data
        except Exception:
            print("检索数据库出错error")
            traceback.print_exc()
            return "null"
        finally:
            session.close()

    def select_movie_id_by_tag(self, tag):
        """
        检索数据库中的所有movie id
        """
        session = self.session()
        try:
            data = session.query(MovieInfo.movie_id).filter(MovieInfo.movie_tag == tag).all()
            return data
        except Exception:
            print("检索所有的id时出错error")
            traceback.print_exc()
            return []
        finally:
            session.close()

    def insert_movie(self, movie_dict):
        """
        插入数据库
        """
        session = self.session()
        try:
            print(json.dumps(movie_dict, ensure_ascii=False))
            movie_ = MovieInfo(
                movie_id=movie_dict['id'],
                movie_tag=movie_dict['tag'],
                movie_name=movie_dict['name'],
                movie_url=movie_dict['url'],
                movie_cover=movie_dict['cover'],
                movie_rate=movie_dict['rate'],
                movie_playable=true_or_false(movie_dict['playable']),
                movie_new=true_or_false(movie_dict['new']),
                movie_source=movie_dict['source'],
                movie_actors=str(movie_dict['actors']),
                movie_directors=str(movie_dict['directors']),
                movie_region=movie_dict['region'],
                movie_types=str(movie_dict['types']),
                movie_release_year=movie_dict['release_year'],
                movie_duration=movie_dict['duration']
            )
            session.add(movie_)
            session.flush()
            session.commit()
            session.close()
        except Exception:
            print("插入数据库error")
            traceback.print_exc()
        finally:
            session.close()
