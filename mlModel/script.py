import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import numpy as np
import pandas as pd

data = pd.read_csv('./dataset/movie_metadata.csv')


# keep important features which can help to recommend movies, drop others

data = data.drop(['color', 'num_critic_for_reviews', 'duration',
        'director_facebook_likes', 'actor_3_facebook_likes',
        'actor_1_facebook_likes', 'gross', 
        'num_voted_users', 'cast_total_facebook_likes',
        'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link',
        'num_user_for_reviews', 'language', 'country',
        'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
        'imdb_score', 'aspect_ratio', 'movie_facebook_likes'], 1)



data.dropna(inplace=True)

data['genres'] = data['genres'].apply(lambda a: str(a).replace('|', ' '))


data['movie_title'] = data['movie_title'].apply(lambda a:a[:-1])

data['combined'] = data['director_name']+' '+data['actor_2_name']+' '+data['genres']+' '+data['actor_1_name']+' '+data['actor_3_name']



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vec = CountVectorizer()
vec_matrix = vec.fit_transform(data['combined'])

similarity = cosine_similarity(vec_matrix)

def recommend(movie):
    if movie not in data['movie_title'].unique():
        return('Sorry! The movie is not Available')
    else:
        i = data.loc[data['movie_title']==movie].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11] # excluding first item since it is the requested movie itself
        movies = []
        for i in range(len(lst)):
            a = lst[i][0]
            movies.append(data['movie_title'][a])
        return movies


print(recommend('The Kids Are All Right'))

