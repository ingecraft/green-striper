from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

class DBConnector():
   
    def __init__(self, config):
        self._engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        self._base = Base
        Session = sessionmaker(bind=self.engine)
        self._session = Session()

    @property
    def session(self):
        return self._session 

    @property
    def engine(self):
        return self._engine

    @property
    def base(self):
        return self._base


def initiate_db(config):
    db_conn = DBConnector(config)
    db_conn.base.metadata.create_all(db_conn.engine)
