import click

import db
import config

configuration = config.config['development']


def create_db():
    db_conn = db.DBConnector(configuration)
    db_conn.base.metadata.create_all(db_conn.engine)

def init_db():
    pass 
