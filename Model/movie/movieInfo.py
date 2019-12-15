"""
date: 2019.12.16
author: east
function: movie表的模型
"""
from config import CONFIG
from sqlalchemy import Table, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI, echo=False)
metadata = MetaData(bind=engine)


class MovieInfo(Base):
    __table__ = Table("movieInfo", metadata, autoload=True)
