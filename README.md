# Music-Recommender-System
A recommender system to recommend songs using unsupervised ML techniques (TF-IDF & Cosine similarity). We use a dataset named Spotify million song. The dataset includes song names, artist 
names along with links to the song and lyrics. It has textual entries of songs containing 4 main columns (artist, song, link, text) with around 643 unique artists, 44,824 unique songs, 57,650 unique links and 57,494 unique lyric entries.

For text preprocessing we did ->
- lowercasing text 
- Tokenization into words 
- Stopword removal 
- Stemming
- 
The project was inspired by online tutorials on music recommendation systems. All code, UI design, and additional features (similarity scores, album cover fetching, Streamlit layout) were implemented and adapted by me.

HOW IT WORKS-
- Uses a precomputed similarity matrix for songs.
- Finds the top 5 songs most similar to the selected song.
- Fetches album covers dynamically from Spotify API.
- Displays results in a clean Streamlit UI.

dataset link - https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset
