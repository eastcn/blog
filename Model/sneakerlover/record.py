"""
@author: east
@date:
@function:
"""
from config import CONFIG
from sqlalchemy import Table, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI_SNEAKER, echo=False)
metadata = MetaData(bind=engine)


class Record(Base):
    __table__ = Table("record", metadata, autoload=True)
