import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "95ba8314e4494cf59ee438ead741fa74"
CLIENT_SECRET = "875d8aff877c41be89d23abc7f1f78fd"

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fetch album cover function
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png" 

# Recommendation function with similarity score
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similer[index])), reverse=True, key=lambda x: x[1])
    
    recommended_names = []
    recommended_artists = []
    recommended_covers = []
    recommended_scores = []

    for i in distances[1:6]:  # Top 5 recommendations excluding selected song
        idx = i[0]
        score = i[1]
        artist = music.iloc[idx].artist
        song_name = music.iloc[idx].song
        recommended_names.append(song_name)
        recommended_artists.append(artist)
        recommended_covers.append(get_song_album_cover_url(song_name, artist))
        recommended_scores.append(score)

    return recommended_names, recommended_artists, recommended_covers, recommended_scores

st.header('Music Recommender System')

music = pickle.load(open('df.pkl', 'rb'))
similer = pickle.load(open('similer.pkl', 'rb'))

music_list = music['song'].values
selected_music = st.selectbox("Type or select a song from the dropdown", music_list)

# Show recommendations
if st.button('Show Recommendation'):
    names, artists, covers, scores = recommend(selected_music)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(f"{names[i]} by {artists[i]} ({scores[i]:.2f})")
            st.image(covers[i])
