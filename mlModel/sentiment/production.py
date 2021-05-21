import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle
import os

nltk.download("stopwords")


stopset = set(stopwords.words('english'))

# Tokenization
def joiner(file_name):
        paths = os.path.dirname(os.path.abspath(__file__))
        paths = os.path.join(paths, file_name)
        return paths

vectorizer = None

with open(joiner("token.pkl"), "rb") as rfile:
    vectorizer = pickle.load(rfile)

text = ["fuck you"]

X = vectorizer.fit_transform(text)
print(X)

X.toarray()
clf = None

with open(joiner("sentiment.pkl"), "rb") as rfile:
    clf = pickle.load(rfile)

clf.predict(X)
