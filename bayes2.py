import math
import pandas
import re

import numpy as np

# Excel stuff
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

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



print(tf_train[0:10])

