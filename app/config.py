# import libraries

import urllib.request, urllib.parse, urllib.error
import json


# make request to youtube api

serviceurl = 'https://www.googleapis.com/youtube/v3/search?'

def send_query(api_key, search_term):
    try:
        # create url

        url = serviceurl + urllib.parse.urlencode({'part': 'snippet', 'q': search_term, 'key': api_key})

        # open url

        print('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print("*"*50)
        print(data)
        print('Retrieved', len(data), 'characters')

        # parse json

        try:
            data = json.loads(data)
        except Exception as e:
            print(e)

        return data
    except Exception as e:
        print(e)