import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import shutil
import requests

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

offset = 0
all_albums = []

while offset < 127:
    results = sp.current_user_saved_albums(50, offset)
    all_albums.extend(results['items'])
    offset += 50

for album in all_albums:
    data = album['album']
    url = data['images'][0]['url']
    filename = 'cover_art/' + data['name'].replace(" ", '').replace('/', '') + '.jpeg'
    photo = requests.get(url, stream=True)
    photo.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(photo.raw, f)
        print(data['name'] + ' downloaded')
