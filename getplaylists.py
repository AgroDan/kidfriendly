#!/usr/bin/env python3

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import config

naughty_words = ["shit", "piss", "fuck", "cunt", "cock", "motherfucker", "tits"]

lg_token = config.lg_token
genius = lyricsgenius.Genius(lg_token)
genius.verbose = False

client_id = config.client_id
client_secret = config.client_secret
playlist_id = config.playlist_id


auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

my_tracks = []
playlist = sp.playlist_tracks(playlist_id, limit=100, offset=0)
offset = 0
while True:
    print(f"Getting offset of {offset}...")
    playlist = sp.playlist_tracks(playlist_id, limit=100, offset=offset)
    if not len(playlist['items']):
        break

    for i in playlist['items']:
        a = {'artist': i['track']['artists'][0]['name'], 'title': i['track']['name']}
        my_tracks.append(a)

    offset += 100

print("Now looping over each track to get lyrics")

for song in my_tracks:
    print(f"Searching for {song['title']} by {song['artist']}")
    this_song = genius.search_song(title=song['title'], artist=song['artist'])
    for n in naughty_words:
        try:
            if n in this_song.lyrics.lower():
                print(f"\tFound cuss words in {song['title']} by {song['artist']}!")
        except AttributeError:
            print(f"\tCould not open lyrics! Check manually for {song['title']} by {song['artist']}")
            