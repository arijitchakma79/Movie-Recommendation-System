import numpy as np
import pandas as pd
import ast

import nltk
from nltk.stem.porter import PorterStemmer

def convert(obj):
    newList = []
    for i in ast.literal_eval(obj):
        newList.append(i['name'])
    return newList

def convert_case(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L

def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

def stem(text):
    ps = PorterStemmer()

    y = []
    for i in text.split():
        y.append(ps.stem(i))
    string = " ".join(y)
    return string

def load_data():
    credits = pd.read_csv('./dataset/tmdb_5000_credits.csv')
    movies = pd.read_csv('./dataset/tmdb_5000_movies.csv')

    movies = movies.merge(credits, on='title')
    movies = movies[['movie_id', 'title', 'cast', 'crew', 'genres', 'overview', 'keywords']]
    movies.dropna(inplace=True)

    tags = movies.iloc[0].genres

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert_case)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x:x.split())
    movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    new_df = movies[['movie_id', 'title', 'tags']]

    new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())   

    new_df['tags'] = new_df['tags'].apply(stem) 

    new_df['title'] = new_df['title'].apply(lambda x:x.lower())  

    return new_df