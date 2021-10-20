# -*- coding: utf-8 -*-
import requests
import json


artist = "tania bowra"  # input('Artist name? ')
cArtist = artist.replace(" ", "%20")
artistID = 0

token = "BQDj0RqPTGxtOOvjxt9r8Y_7ItnaujFOkgV3_Eu"

url = f"https://api.spotify.com/v1/search?q={cArtist}&type=artist"


def getArtistID(artistID=artistID):
    r = requests.get(
        url, headers={'Authorization': 'Bearer '+token}, params={'q': 'id'})
    print(r.status_code)
#    jsonR = str(r.text)
#    repo = json.loads(jsonR)
#    print(f'id is: {jsonR}')
    print(r.json()["artists"])


getArtistID()

# r = requests.get(url,
#                 headers={'Authorization': 'Bearer '+token})
# print(r.status_code)

# print(r.json())

#jsonObj = str(r.text())
# print(jsonObj)
# y = json.loads(jsonObj)  # (str(jsonObj))

# print(y)

# for item in y['id']:
#    print(item)


spotify = {
    'artists':
    {
        'href': 'https://api.spotify.com/v1/search?query=tania+bowra&type=artist&offset=0&limit=20',
        'items': [
            {
                'external_urls':
                {
                    'spotify': 'https://open.spotify.com/artist/6LRIeYK0XQHR1mjrPS29Rr'
                },
                'followers':
                {
                    'href': None, 'total': 0
                },
                'genres': [],
                'href': 'https://api.spotify.com/v1/artists/6LRIeYK0XQHR1mjrPS29Rr',
                'id': '6LRIeYK0XQHR1mjrPS29Rr',
                'images': [],
                'name': 'Tania Bowra',
                'popularity': 0,
                'type': 'artist',
                'uri': 'spotify:artist:6LRIeYK0XQHR1mjrPS29Rr'
            },
            {
                'external_urls':
                {
                    'spotify': 'https://open.spotify.com/artist/08td7MxkoHQkXnWAYD8d6Q'
                },
                'followers':
                {
                    'href': None,
                    'total': 255
                },
                'genres': [],
                'href': 'https://api.spotify.com/v1/artists/08td7MxkoHQkXnWAYD8d6Q',
                'id': '08td7MxkoHQkXnWAYD8d6Q',
                'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2731ae2bdc1378da1b440e1f610', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e021ae2bdc1378da1b440e1f610', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048511ae2bdc1378da1b440e1f610', 'width': 64}],
                'name': 'Tania Bowra',
                'popularity': 2,
                'type': 'artist',
                'uri': 'spotify:artist:08td7MxkoHQkXnWAYD8d6Q'
            }
        ],
        'limit': 20,
        'next': None,
        'offset': 0,
        'previous': None,
        'total': 2
    }
}

toJson = json.dumps(spotify)

# print(toJson['id':])
for data in toJson:
    print(data['id'])
