"""
@author: east
@date:
@function:
"""
import json
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.sneakerlover.record import Record
from config import CONFIG


class RecordDao:
    def __init__(self):
        self.engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI_SNEAKER)
        self.session = sessionmaker(self.engine)

    def rank(self):
        """通过执行原生的sql查询rank"""
        conn = self.engine.connect()
        sql = "SELECT userName, count(userName) as num from record GROUP BY userName ORDER BY num DESC"
        data = conn.execute(sql).fetchall()
        # print(data)
        conn.close()
        return data

    def select_detail_by_name(self, name):
        data = self.session().query(Record).filter(Record.userName == name).all()
        data_list = []
        for item in data:
            data_list.append((item.userName, item.method, item.shoes, item.create_time.strftime("%Y-%m-%d")))
        return data_list
