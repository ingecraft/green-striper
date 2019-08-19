import unittest

import db
import config
from sqlalchemy.orm.session import Session

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.configuration = config.config['testing']
        self.db_conn = db.DBConnector(self.configuration)

    def test_db_initialization(self):
        db.initiate_db(self.configuration)
        self.assertEqual(1,1)

    def test_new_session(self):
        session = self.db_conn.session
        self.assertIsInstance(session, Session) 

if __name__ == '__main__':
    unittest.main()

