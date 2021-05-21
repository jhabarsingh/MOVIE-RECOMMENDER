import os
import pickle
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def process(review):
   review = BeautifulSoup(review, features="lxml").get_text()
   review = re.sub("[^a-zA-Z]",' ',review)
   review = review.lower()
   review = review.split()
   swords = set(stopwords.words("english"))
   review = [w for w in review if w not in swords]               
   return(" ".join(review))




vectorizer = None


def joiner(file_name):
        paths = os.path.dirname(os.path.abspath(__file__))
        paths = os.path.join(paths, file_name)
        return paths

with open(joiner("token.pkl"), "rb") as rfile:
    vectorizer = pickle.load(rfile)






def predict(text):
    test = [process(i) for i in text]


    test = vectorizer.transform(test)
    test = test.toarray()

    model = None

    with open(joiner("model.pkl"), "rb") as rfile:
        model = pickle.load(rfile)

    train_predict = model.predict(test)
    return train_predict


if __name__ == "__main__" :
    text = ["good one", "very bad"]
    print(predict(text))