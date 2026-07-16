import streamlit as st
import joblib

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

movies = joblib.load("movie_list.joblib")
similarity = joblib.load("similarity.joblib")


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]


st.markdown(
    """
    <h1 style='text-align:center;color:#FF4B4B;'>
    🍿 Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")

movie = st.selectbox(
    "🎥 Select your favourite movie",
    movies['title'].tolist()
)

if st.button("Recommend", use_container_width=True):

    rec_movies = recommend(movie)

    st.subheader("You may also like")

    for i, movie in enumerate(rec_movies, start=1):
        st.write(f"**{i}. {movie}**")