from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

# Data reading from Documents
messages = pd.read_csv(
    r"D:\GenAI2026\spam.csv",
    names=["Lable", "Messages"],
    usecols=[0, 1],
    header=None,
    sep=",",
    encoding="latin-1",
)

# Data cleaning
stopwords = set(stopwords.words("english"))
lemmitizer = WordNetLemmatizer()
corpus = []
for i in range(len(messages)):
    review = messages["Messages"][i]
    review = re.sub("^[a-zA-Z]", " ", review)
    review = review.lower().split()
    filtered_words = [
        lemmitizer.lemmatize(word, pos="v") for word in review if word not in stopwords
    ]
    corpus.append(" ".join(filtered_words))


## TFIDF Vectoriser

tfidf = TfidfVectorizer(max_features=100, ngram_range=(3, 3))
vector = tfidf.fit_transform(corpus).toarray()
for value, index in tfidf.vocabulary_.items():
    print(f"{value} : {index}")
