import requests
import json


class apiMobileFriendlyTest:
    def __init__(self, url, mobile_api_key):
        self.url = url
        # use your gmail to get a key from https://developers.google.com/webmaster-tools/search-console-api/v1/configure
        # there are limitations have to take into consideration
        # https://developers.google.com/webmaster-tools/search-console-api/v1/pricing
        self.key = mobile_api_key  # The mobileFriendlyTest API will slow down the script

    def get_responsive_test(self):
        url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=' + self.key
        data = {
            'url': self.url,
            'requestScreenshot': 'false'
        }
        response = requests.request("POST", url, data=data)
        return 1 if response.json()['mobileFriendliness'] == 'MOBILE_FRIENDLY' else 0

        # An alternative but not representative way to check responsiveness
        # Find <meta> tag from source code with name="viewport" attribute, and store the content to
        # seo_help['responsive']
        # Example: <metaname="viewport" content="width=device-width, initial-scale=1.0">
        # If seo_help['responsive'] includes these width=device-width, initial-scale=1.0 return 1 else 0
        # We have the get_responsive_test function bellow to double-check the result using API
        # responsive = get_meta_responsive(meta_tags)
        # if not responsive:
        #     seo['responsive'] = 0
        # else:
        #     seo['responsive'] = 1
        #
        # seo_help['responsive'] = responsive
