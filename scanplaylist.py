#!/usr/bin/env python3

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import config

naughty_words = config.naughty_words

lg_token = config.lg_token
genius = lyricsgenius.Genius(lg_token)
genius.verbose = False

# Below added courtesy of Josh Rodgers (joshrodgers.com)
# Fixes intermittent timeout errors on laggy connections to Lyrics Genius
# Original timeout is 5 seconds.
genius.timeout = 100

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
            if len(this_song.lyrics) > 10000:
                print(f"\tHuge output! Didn't find actual lyrics, check manually!")
                break
            if n in this_song.lyrics.lower():
                print(f"\tFound cuss words in {song['title']} by {song['artist']}!")
                print(f"\tFound word: {n}")
                continue
        except AttributeError:
            print(f"\tCould not open lyrics! Check manually for {song['title']} by {song['artist']}")
            break
        except:
            print(f"\tLOST CONNECTION! Try again later? Skipping...")
