
import pandas
import random
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from NoiseRemoval import noiseRemoval
import numpy as np
import re

class Comment(object):

    def __init__(self, id, text, sentiment):
        self.id = id
        self.text = text
        self.sentiment = sentiment

def preprocess_text(text):
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', text)
    text = re.sub('@[^\s]+','USER', text)
    text = text.lower().replace("ё", "е")
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +',' ', text)
    return text.strip()


# Excel stuff
df = pandas.read_excel('comments100.xlsx')
df_id = df["id"]
df_text = df["text"]
df_sentiment=df["sentiment"]



X_train, X_test, y_train, y_test = train_test_split(df['text'].values, df['sentiment'].values, test_size=0.2)

re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')


def tokenize(s): return re_tok.sub(r' \1 ', s).split()


vect = CountVectorizer(tokenizer=tokenize)
tf_train = vect.fit_transform(X_train)
tf_test = vect.transform(X_test)

p = tf_train[y_train==1 or y_train==2].sum(0) + 1

q = tf_train[y_train==-1 or y_train==-2].sum(0) + 1

r = np.log((p/p.sum()) / (q/q.sum()))

b = np.log(len(p) / len(q))

pre_preds = tf_test @ r.T + b
preds = pre_preds.T > 0
accuracy = (preds == y_test).mean()


