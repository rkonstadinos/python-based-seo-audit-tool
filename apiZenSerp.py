import requests
import json


class apiZenSerp:
    def __init__(self, keyword, zenserp_api_key):
        self.keyword = keyword
        # create a free account on https://app.zenserp.com/
        # get your API key up to 50 free API requests per month
        # or upgrade to premium
        self.zenserp_api_key = zenserp_api_key

    # Get_organic_serps function will get as input the keyword and the location from the user,
    # and it will return the organic SERPs for this specific keyword in a dictionary using the zenserp api
    def get_organic_serps(self):
        # if keyword or location is not a string show an error
        if not isinstance(self.keyword, str):
            return 'Keyword given is not a string'
        # if not isinstance(location, str):
        #     return 'Location given is not a string'

        # prepare headers for zenserp api
        headers = {"apikey": self.zenserp_api_key}
        # set query parameters
        params = (
            ('q', self.keyword),
            # ('location', location),
            ('search_engine', 'google.com'),
        )
        # do the request
        response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
        # get the response
        response = response.text

        # turn json to python dictionary
        organic = json.loads(response)

        # get only the organic results
        organic = organic["organic"]

        # if empty organic return error. It is not possible though
        if not organic:
            return 'Missing Organic SERPs'

        # create a new empty dictionary
        my_dictionary = {}

        i = 1
        # loop on organic
        for website in organic:
            # if localPack and videos exists then the result is from Google my business or Youtube and I have to
            # escape it
            if 'localPack' not in website.keys() and 'videos' not in website.keys():
                # if not, append it to the dictionary
                if not website["isAmp"]:  # if amp is False
                    amp = 0
                else:  # if amp is True
                    amp = 1
                # create a dictionary for this website
                this_website = {
                    "position": i,
                    "url": website["url"],
                    # "title": website["title"],
                    # "description": website["description"],
                    "amp": amp
                }
                my_dictionary[i] = this_website  # append the dictionary having as a key the position
                i = i + 1

        return my_dictionary
