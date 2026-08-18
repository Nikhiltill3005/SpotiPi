import requests
from io import BytesIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth,SpotifyClientCredentials
import time
import sys
from PIL import Image
import os

#CLIENT_ID & CLIENT_SECRET Have been erased for privacy reasons.
def initialise_env_var():
    os.environ['SPOTIPY_CLIENT_ID']     =   '################'
    os.environ['SPOTIPY_CLIENT_SECRET'] =   '################'
    os.environ['SPOTIPY_REDIRECT_URI']  =   '################'


def get_song_info(token):
    song_data   = token.currently_playing()
    song_title  = (song_data["item"]["name"])
    song_artist = (song_data["item"]["artists"][0]["name"])
    song_cover_url    = (song_data["item"]["album"]["images"][0]["url"])

    return [song_title,song_artist,song_cover_url]

def write_img(img_url):
   # print("Running Write_IMG")
    img_data = requests.get(img_url).content
    with open('album.jpg', 'wb') as handler:
        handler.write(img_data)

def main():
    initialise_env_var()
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,open_browser=False))
    prev_song = None

    while 1 > 0:
        current_song_info = get_song_info(sp)

        if current_song_info[0] != prev_song:
            print("You are now listening to ",current_song_info[0], " by ",current_song_info[1])
            prev_song = current_song_info[0]
            write_img(current_song_info[2])
main()

