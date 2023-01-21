import streamlit as st
import pickle
import requests


def fetch_poster(mve_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key='
                            'c7b6a3b327ae4486eda03ad7de23e9c5&language=en-US&external_source=imdb_id'.format(mve_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_name = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for name in movies_name:
        movie_id = movies.iloc[name[0]].movie_id
        # fetch poster
        recommended_movies.append(movies.iloc[name[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


st.title('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

select_movie_name = st.selectbox(
    'Please enter the movie of your choice',
    movies_list)

if st.button('Recommend'):
    names, posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
