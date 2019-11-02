"""
@author: east
@date:
@function:
"""
import traceback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.basic.user import User
from config import CONFIG

class UserMethod:
    def __init__(self):
        self.engine = create_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
        self.DB_Session = sessionmaker(self.engine)
        self.user = User.__table__

    def selectUserInfo(self):
        try:
            session = self.DB_Session()
            data = session.query(self.user).limit(1).all()
            return data
        except Exception:
            traceback.print_exc()
            return False