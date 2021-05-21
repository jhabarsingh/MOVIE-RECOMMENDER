import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

train_data = pd.read_csv('./dataset/labeledTrainData.tsv.zip',  delimiter="\t", quoting=3)
test_data = pd.read_csv('./dataset/testData.tsv.zip', delimiter = "\t", quoting= 3 )
submission1 = pd.read_csv("./dataset/sampleSubmission.csv")

train_data.head()

train_data.isnull().sum().sum()

train_y = np.array(train_data["sentiment"])

nltk.download('stopwords')

def process(review):
   review = BeautifulSoup(review, features="lxml").get_text()
   review = re.sub("[^a-zA-Z]",' ',review)
   review = review.lower()
   review = review.split()
   swords = set(stopwords.words("english"))
   review = [w for w in review if w not in swords]               
   return(" ".join(review))


train_x = []
for r in range(len(train_data["review"])):
  train_x.append(process(train_data["review"][r]))


vectorizer = CountVectorizer( max_features = 5000 )
train_x = vectorizer.fit_transform(train_x)
train_x = train_x.toarray()


with open("token.pkl", "wb") as wfile:
    pickle.dump(vectorizer, wfile)

train_x.shape, train_y.shape

test_data.head()

test_data.isnull().sum().sum()


text = ["good one", "very bad"]
test = [process(i) for i in text]


test = vectorizer.transform(test)
test = test.toarray()

test.shape


model = RandomForestClassifier(n_estimators = 100)
model.fit(train_x, train_y)
train_predict = model.predict(test)
print(train_predict)


with open("model.pkl", "wb") as wfile:
    pickle.dump(model, wfile)
