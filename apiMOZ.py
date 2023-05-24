from SEOmozAPISamples.python.mozscape import Mozscape


class apiMOZ:
    def __init__(self, url, moz_api_client, moz_api_key):
        self.url = url
        self.moz_api_client = moz_api_client
        self.moz_api_key = moz_api_key

        # create a free account on https://moz.com/products/api/pricing
        # get your API key up to 2,500 rows per month
        # or upgrade to premium
        self.moz_client = Mozscape(self.moz_api_client, self.moz_api_key)

    def get_da(self):
        mozMetrics = self.moz_client.urlMetrics(self.url)
        return mozMetrics['pda']
