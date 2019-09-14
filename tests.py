import unittest
import datetime

import stripe

import db
import config
import api_connection as ac

from sqlalchemy.orm.session import Session

test_config = config.config['testing']

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_conn = db.DBConnector(test_config)

    def test_db_initialization(self):
        db.initiate_db(test_config)
        self.assertEqual(1,1)

    def test_new_session(self):
        session = self.db_conn.session
        self.assertIsInstance(session, Session) 


class TestAPIConnection(unittest.TestCase):

    def setUp(self):
        self.api_conn = ac.StripeAPI(test_config)
        self.stripe_client = self.api_conn.api_client

    def test_stripe_client(self):
        api_client = self.api_conn.api_client
        self.assertIs(api_client, stripe)

    def test_customers_valid_range(self):
        start_date = datetime.datetime(2018,1,1)
        end_date = datetime.datetime.now()
        customers = self.api_conn.customers_by_date(start_date, end_date)
        self.assertIsNotNone(customers)
            

if __name__ == '__main__':
    unittest.main()

