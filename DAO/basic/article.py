"""
@author: east
@date:
@function:
"""
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.basic.article import Article
from config import CONFIG


class ArticleSql():

    def __init__(self):
        self.engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
        self.DB_Session = sessionmaker(self.engine)
        self.article_table = Article.__table__

    # 增
    def insert(self, article):
        """
        传入要插入的对象列表
        :param object_list: 要insert的数据库表对象列表
        """
        try:
            article_ = Article(contend=article['contend'], title=article['title'])
            session = self.DB_Session()
            session.add(article_)
            session.flush()
            article_id = article_.id
            session.commit()
            session.close()
            return article_id
        except Exception:
            print("传入数据库失败")
            traceback.print_exc()
            return "failed"

    def updateById(self, article):
        """
        根据ID 更新文章
        :param article:
        :return:
        """
        try:
            session = self.DB_Session()
            # data = session.query(Article.__table__).filter_by(id=article['id']).first()
            # sqlalchemy更新时，只需要用session查询出然后再修改。查询的对象为对应类的model类，上一句为错误示范
            data = session.query(Article).filter_by(id=article['id']).update(
                {"contend": article['contend'], "title": article['title']})
            session.commit()
            return True
        except Exception:
            traceback.print_exc()
            return False

    def delete(self, object_tuple):
        pass

    def select_by_kind(self, kind, limit):
        try:
            session = self.DB_Session()
            colums = self.article_table.columns.keys()
            data = session.query(Article.__table__).filter_by(kind=kind).limit(limit).all()
            return data
        except Exception:
            traceback.print_exc()
            return False

    def select_id_by_title(self, title):
        """
        确认是否存在同标题的文章
        :param title:
        :return:
        """
        try:
            article_id = ''
            data = self.DB_Session().query(Article).filter_by(title=title).all()
            if len(data) > 0:
                res = {
                    'id': data[0].id,
                    'contend': data[0].contend
                }
                return res
            else:
                return True
        except Exception:
            traceback.print_exc()
            return False

    def select_by_id(self, article_id):
        try:
            data = self.DB_Session().query(Article).filter_by(id=article_id).first()
            return data
        except Exception:
            traceback.print_exc()
            return False


