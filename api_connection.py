import stripe

class StripeAPI():

    def __init__(self, config):
        client = stripe.http_client.RequestsClient()
        self._api_client = stripe
        self._api_client.default_http_client = client
        self._api_client.api_key = config 

    @property
    def api_client(self):
        return self._api_client
