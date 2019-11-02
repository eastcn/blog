"""
@author: east
@date:
@function:
"""
from sqlalchemy.ext.automap import automap_base
from config import CONFIG
from sqlalchemy import Table, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI, echo=False)
metadata = MetaData(bind=engine)


class Article(Base):
    __table__ = Table("articles", metadata, autoload=True)
