# Song Link Generator

This is a site to enter a spotify song link and get the youtube music link for the song, and vice versa. 

Spotify has an API, but not Youtube music. There is a hacked/3rd party Youtube Music API.

[Youtube Music python wrapper/client api](https://github.com/sigma67/ytmusicapi)

[Spotify python wrapper](https://github.com/spotipy-dev/spotipy)

### Basics
A react front end SPA that is hosted on github pages, located in /songlinkegenerator_react, and a backend python api located in /songlinkgenerator_api

### React Frontend deploy

Deployed using a gh-pages npm package to its own branch, then the GH pages is pointed to that branch. 

```
cd songlinkgenerator_react
npm run deploy
```

### Python API
```
cd songlinkgenerator_api
docker-compose -d up
```

Example curl: 
```
curl --location 'http://127.0.0.1:5001/ytm-to-spotify' \
--header 'Content-Type: application/json' \
--data '{
    "ytm_link": "https://music.youtube.com/watch?v=wOGWrbIYPqY"
}'
```


### Basic Flow: 

Mr Brightside example links: 

- https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B
- https://music.youtube.com/watch?v=m2zUrruKjDQ&si=7m20qFYO9BxIcdUc


* Parse each ID
* call the API to get the Title and Artist
* Call the other API Track endpoint with the title and artist
* Return the other link 

### TODO: 

- improve error handling
- tests
- build out react front end
- add some sort of verification to make sure returned link is same as input link
- deploy api somewhere
- deploy front end to github pages
- 
