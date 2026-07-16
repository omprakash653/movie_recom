import joblib
import streamlit as st
import requests
import time
from requests.exceptions import RequestException

def fetch_poster(movie_id, retries=3, backoff=2):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                # No poster path found
                return "https://via.placeholder.com/500x750?text=No+Image"
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff)
                backoff *= 2  # Exponential backoff
            else:
                st.error(f"Error fetching poster after {retries} attempts: {e}")
                return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_url = fetch_poster(movie_id)
        recommended_movie_posters.append(poster_url)
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

st.header('🎬 Movie Recommender System Using Machine Learning')

# Load your data and similarity matrix (make sure the path is correct)
movies = joblib.load(open('movie_list.joblib', 'rb'))
similarity = joblib.load(open('similarity.joblib', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.text(name)  
            st.image(poster)
st.text("Made with ❤️ by Om Yadav")
st.text("Source Code:")










