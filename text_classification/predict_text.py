import pickle
import nltk
from nltk.corpus import stopwords
#from text_prototype_1 import text_prepare
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import re
from ast import literal_eval
import pandas as pd
import numpy as np
import json

def read_data(file):
  data = pd.read_csv(file, sep = '\t')
  data['tags'] = data['tags'].apply(literal_eval)
  return data


train = read_data('text_classification/data/train.tsv')
X_train, Y_train = train['title'].values, train['tags'].values

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
#print(REPLACE_BY_SPACE_RE)

BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = dict()
stopwords = []
with open('text_classification/listfile.txt', 'r') as filehandle:
  for line in filehandle:
    currentPlace = line[:-1]
    stopwords.append(currentPlace)

for i in stopwords:
  STOPWORDS[i] = 1

def text_prepare(text):
  text = text.lower()
  text = REPLACE_BY_SPACE_RE.sub(" ", text)
  text = BAD_SYMBOLS_RE.sub("", text)
  text = text.split()
  #print(text)
  arr = []
  for i in text:
    if STOPWORDS.get(i) == None:
      arr.append(i)
  text = " ".join(arr)
  return text

X_train = [text_prepare(x) for x in X_train]

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def tfidf_features_TEXT(TEXT):
  tfidf_vectorizer = TfidfVectorizer(token_pattern = r'\S+', ngram_range = (1,2), max_df = 0.9, min_df = 5,)
  X = tfidf_vectorizer.fit(X_train)
  TEXT = tfidf_vectorizer.transform(TEXT)
  #X_test = tfidf_vectorizer.transform(X_test)
  return TEXT

def predict(text):
  TEXT = []
  TEXT.append(text)
  TEXT = [text_prepare(x) for x in TEXT]
  TEXT_tfidf = tfidf_features_TEXT(TEXT)
  classifier_tfidf = pickle.load(open('text_classification/finalized_model.sav', 'rb'))
  Y_predicted_scores = classifier_tfidf.decision_function(TEXT_tfidf)
  Y_predicted_scores = sigmoid(Y_predicted_scores)
  words_to_index = json.load(open("text_classification/words_to_index.txt"))
  index_to_words = json.load(open("text_classification/index_to_words.txt"))
  count = 0
  for (i, j) in words_to_index.items():
    words_to_index[i] = Y_predicted_scores[0][count]
    count += 1
  most_tag = sorted(words_to_index.items(), key=lambda x: x[1], reverse=True)[:5]
  total = 0
  # for (i, j) in ans.items():
  #   total += j
  ans = []
  for (i, j) in most_tag:
    j = j * 100
    ans.append((i, j))
  #print(ans)
  return ans

predict("How to use cin and cout statements")