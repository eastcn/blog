"""
@author: east
@date:
@function:
"""
import json
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.basic.article import Article
from config import CONFIG


class ArticleSql:

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
        session = self.DB_Session()
        try:
            article_ = Article(contend=article['contend'], title=article['title'])
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
        finally:
            session.close()

    def updateById(self, article):
        """
        根据ID 更新文章
        :param article:
        :return:
        """
        session = self.DB_Session()
        try:
            # data = session.query(Article.__table__).filter_by(id=article['id']).first()
            # sqlalchemy更新时，只需要用session查询出然后再修改。查询的对象为对应类的model类，上一句为错误示范
            print(article)
            data = session.query(Article).filter(Article.id == article['id']).update(
                {"contend": article['contend'], "title": article['title'],
                 "tag": json.dumps(article['tags'], ensure_ascii=False),
                 "kind": article['kind']})
            session.commit()
            session.close()
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            session.close()

    def updateOldPostById(self,article):
        # 排查更新数据问题 解决，数据类型问题，tags存入时应为string不是list。
        session = self.DB_Session()
        try:
            print(article)
            data = session.query(Article).filter(Article.id==article['id']).first()
            print(f"post id:{data.id}" )
            data.contend = article['contend']
            data.title = article['title']
            data.tag = json.dumps(article['tags'])
            data.kind = article['kind']
            session.commit()
            session.close()
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            session.close()

    def delete(self, object_tuple):
        pass

    def select_by_kind(self, kind, limit):
        session = self.DB_Session()
        try:
            colums = self.article_table.columns.keys()
            data = session.query(Article).filter_by(kind=kind).order_by(Article.create_time.desc()).limit(limit).all()
            return data
        except Exception:
            traceback.print_exc()
            return False
        finally:
            session.close()

    def select_id_by_title(self, title):
        """
        确认是否存在同标题的文章
        :param title:
        :return:
        """
        session = self.DB_Session()
        try:
            article_id = ''
            data = session.query(Article).filter_by(title=title).all()
            if len(data) > 0:
                res = {
                    'id': data[0].id,
                    'contend': data[0].contend,
                    'tags': data[0].tag,
                    'kind': data[0].kind,
                    'updateTime': data[0].update_time.strftime("%Y-%m-%d %H:%M")
                }
                return res
            else:
                return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            session.close()

    def select_by_id(self, article_id):
        session = self.DB_Session()
        try:
            data = session.query(Article).filter_by(id=article_id).first()
            return data
        except Exception:
            traceback.print_exc()
            return False
        finally:
            session.close()
