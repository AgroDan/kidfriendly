# kidfriendly
A little script I wrote to check a playlist for cuss words. This year, my kid is having her first outdoor birthday party in which we invite a bunch of her friends and their parents over. Since I've never met any of them, I want to make a good first impression, and as we all know, outdoor parties always need some sort of music. I have a really good outdoor playlist of just generic background music, but not all of that music is kid friendly. Some of it is downright vulgar. Perfectly fine for grilling with a few beers, but not so great when children are running around.

I wrote this script to scan a spotify playlist, query every song it gets for its lyrics, and then check for certain cuss words.

## How to Use

 1. Install pip
 2. Install requirements: `pip install -r requirements.txt`
 3. Register for an API token for [Lyrics Genius](https://genius.com/api-clients)
 4. Register for an ClientID and Client Secret for [Spotify Developer](https://developer.spotify.com/)
 5. Find the playlist ID of what you want to scan for (see screenshot below)
 6. Copy config.sample.py to config.py (`cp config.sample.py config.py`)
 7. Enter all the values into config.py
 8. Run with `python3 scanplaylist.py`


## Spotify Playlist ID

To obtain the spotify playlist ID, find the playlist you want to work with and get the link to it:

![Copy Link](img/spotify-copylink.png)

From the link which is now in your clipboard, paste it into a text editor and find the Base64 encoded string between `playlist/` and `?si`:

![Playlist ID](img/spotifyplaylist.png)

## Result

Here it is in action:

![Working](img/workingkidfriendly.png)
