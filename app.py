import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for j in movie_list:
        recommended_movies.append(movies.iloc[j[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')
st.subheader('-Sourav Dey')
selected_movie_name = st.selectbox(
    'Select the Movie',
    movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for j in recommendations:
        st.write(j)


