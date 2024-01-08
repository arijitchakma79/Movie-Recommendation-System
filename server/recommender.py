import numpy as np
from data import load_data
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from difflib import get_close_matches

class Recommender:
    def __init__(self) -> None:
        self.__data = load_data()
        self.__cv = CountVectorizer(max_features=5000, stop_words='english')

        self.__vectors = self.__cv.fit_transform(self.__data['tags']).toarray()
        self.__similarity = cosine_similarity(self.__vectors)

    def recommend(self, movie):
        movie = movie.lower()

        moiveNames = self.__data['title'].values.tolist()
        match = get_close_matches(movie, moiveNames)[0]

        movieIndex = self.__data[self.__data['title'] == match].index[0]
        distances = self.__similarity[movieIndex]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
        
        result = []
        for i in movies_list:
            result.append(self.__data.iloc[i[0]]['title'])
        return result



