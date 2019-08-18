from sqlalchemy import create_engine

from models import Base

class DBConnector():
   
    def __init__(self, config):
        self.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        self.base = Base


def initiate_db(config):
    db_conn = DBConnector(config)
    db_conn.base.metadata.create_all(db_conn.engine)

        

