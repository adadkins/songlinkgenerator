from urllib.parse import parse_qs, urlparse
from flask import Flask, jsonify, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv() 
app = Flask(__name__)

# set up spotify wrapper
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# set up youtube music wrapper
yt = YTMusic()

@app.route('/spotify-to-ytm', methods=['POST'])
def spotify_to_ytm():
    spotify_link = request.json.get('spotify_link')

    # trim trailing / if exists
    if spotify_link.endswith('/'):
        spotify_link = spotify_link[:-1]

    # Split the URL using '/' as a delimiter and get the last part
    spotify_id = spotify_link.split('/')[-1]

    print(spotify_id)
    # Implement the conversion logic here (e.g., using regex or APIs)
    ytm_link = convert_spotify_to_ytm(spotify_id)

    return jsonify({'ytm_link': ytm_link})

@app.route('/ytm-to-spotify', methods=['POST'])
def ytm_to_spotify() -> None:
    ytm_link = request.json.get('ytm_link')

    # trim trailing / if exists
    if ytm_link.endswith('/'):
        ytm_link = ytm_link[:-1]

    parsed_url = urlparse(ytm_link)

    # Get the query parameters
    query_parameters = parse_qs(parsed_url.query)

    # Get the value of the 'v' parameter
    v_parameter_value = query_parameters.get('v', [])[0]
    # TODO: add some validation 


    # Implement the conversion logic here (e.g., using regex or APIs)
    spotify_link = convert_ytm_to_spotify(v_parameter_value)

    return jsonify({'spotify_link': spotify_link})


def convert_spotify_to_ytm(link: str) -> str:
    try: 
        result = sp.track(track_id=link)
        song_title = result["name"]
        artist_name = result['album']['artists'][0]['name']
        # album_title = result['album']['name']

        q = artist_name + " " + song_title

        result = yt.search(query=q, filter='songs')
        song_id= result[0]['videoId']
        ytm_link= "https://music.youtube.com/watch?v=" + song_id
        return ytm_link
    
    except:
        return "Internal Server Error"


def convert_ytm_to_spotify(link: str) -> str:
    try: 
    # get song details from youtube music
        search_results = yt.get_song(link)

        # construct a query from the band name and song title
        spotify_query= search_results["videoDetails"]["author"] + " " + search_results["videoDetails"]["title"]

        # hit spotify api with the query
        result = sp.search(q=spotify_query)

        # Extract the artist name, album title, and artist's Spotify URL
        # artist_name = result["tracks"]["items"][0]['album']['artists'][0]['name']
        # album_title = result["tracks"]["items"][0]['album']['name']
        # artist_spotify_url = result["tracks"]["items"][0]['href']
        # song_title = result["tracks"]["items"][0]['name']

        song_spotify_url= result["tracks"]["items"][0]['external_urls']['spotify']

        # # Print the extracted information
        # print("Artist:", artist_name)
        # print("Album Title:", album_title)
        # print("Song Title:", song_title)
        # print("Song's Spotify URL:", song_spotify_url)
        # print("Artist's Spotify URL:", artist_spotify_url)

        # TODO: probably do some nonsense to make sure the artists and titles match. Or maybe a "matching" score. 

        return song_spotify_url
    except: 
        return "Internal Server Error"
    
if __name__ == "__main__":
    app.run(debug=True)