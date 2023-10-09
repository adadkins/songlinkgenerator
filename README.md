##Intro

This is a site to enter a spotify song link and get the youtube music link for the song, and vice versa. 

Spotify has an API, but Youtube music. There is a hacked/3rd party Youtube Music API.
Python wrapper/client for youtube music api: 
https://github.com/sigma67/ytmusicapi

Python wrapper for spotify: 
https://github.com/spotipy-dev/spotipy


Basic Flow: 

Mr Brightside- 

https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B


https://music.youtube.com/watch?v=m2zUrruKjDQ&si=7m20qFYO9BxIcdUc


Parse each ID, call the API to get the Title and Artist. Call the other API Track endpoint with the title and artist. 

TODO: 

improve error handling
tests
build out react front end
add some sort of verification to make sure returned link is same as input link
deploy api somewhere
deploy front end to github pages