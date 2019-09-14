import datetime

import stripe

import aux


class StripeAPI():
    default_start_date = datetime.datetime(2018,1,1)
    default_end_date = datetime.datetime.now()

    def __init__(self, key):
        client = stripe.http_client.RequestsClient()
        self._api_client = stripe
        self._api_client.default_http_client = client
        self._api_client.api_key = key

    @property
    def api_client(self):
        return self._api_client

    def customers_by_date(self, start_date=default_start_date,
            end_date=default_end_date):
        unix_start = aux.datetime_to_unix(start_date)
        unix_end = aux.datetime_to_unix(end_date)
         

