import numpy as np
import pandas as pd
import os
import pickle

data = pd.read_csv('./dataset/recommender.csv')

def joiner(file_name):
        paths = os.path.dirname(os.path.abspath(__file__))
        paths = os.path.join(paths, file_name)
        return paths

recommender = None

with open(joiner("recommender.pkl"), "rb") as rfile:
    recommender = pickle.load(rfile)


# Save tokenizer for future use

def recommend(movie):
    if movie not in data['movie_title'].unique():
        return('Sorry! The movie is not Available')
    else:
        i = data.loc[data['movie_title']==movie].index[0]
        lst = list(enumerate(recommender[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        movies = []
        for i in range(len(lst)):
            a = lst[i][0]
            movies.append(data['movie_title'][a])
        return movies


print(recommend('And So It Goes'))

