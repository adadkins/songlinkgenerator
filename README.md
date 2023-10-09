##Intro

This is a site to enter a spotify song link and get the youtube music link for the song, and vice versa. 

Spotify has an API, but Youtube music. There is a hacked/3rd party Youtube Music API.

Go Wrapper for Spotify API: 

https://github.com/zmb3/spotify

No wrapper/client for youtube music api: 
https://github.com/sigma67/ytmusicapi

Basic Flow: 
Mr Brightside- 
https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B

https://music.youtube.com/watch?v=m2zUrruKjDQ&si=7m20qFYO9BxIcdUc

Parse each ID, call the API to get the Title and Artist. Call the other API Track endpoint with the title and artist. 

TODO: 

Auth into both clients

parse id from both clients

implement the search for each client

return the url/link from the search
