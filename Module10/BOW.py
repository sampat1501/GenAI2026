import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from nltk import WordNetLemmatizer

nltk.download("stopwords", quiet=True)

from sklearn.feature_extraction.text import CountVectorizer

# Text Reading
# Read CSV file from the repository root
csv_path = os.path.join(os.path.dirname(__file__), os.pardir, "spam.csv")
messages = pd.read_csv(
    r"d:\GenAI2026\spam.csv",
    sep=",",
    names=["Label", "Messages"],
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
)

# Data preprocessing and cleaning
# stop_words = set(stopwords.words("english"))
# pe = PorterStemmer()
# corpus = []
# for i in range(len(messages)):
#     review = str(messages["Messages"][i])
#     review = re.sub("[^a-zA-Z]", " ", review)
#     review = review.lower().split()
#     filtered_words = [pe.stem(word) for word in review if word not in stop_words]
#     corpus.append(" ".join(filtered_words))

# print(corpus)

# Text Cleaning
# Stop un-nessasory words
le = WordNetLemmatizer()
stopwords = set(stopwords.words("english"))
pe = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    review = messages["Messages"][i]
    review = re.sub("^[a-zA-Z]", " ", review)
    review = review.lower().split()
    filtered_words = [
        le.lemmatize(word, pos="v") for word in review if word not in stopwords
    ]
    corpus.append(" ".join(filtered_words))
# print(corpus)


# create Model from sklearn librarary
cv = CountVectorizer(max_features=100, binary=True, ngram_range=(3, 3))

X = cv.fit_transform(corpus).toarray()
print(X.shape)
print(X)

for word, index in (cv.vocabulary_).items():
    print(f"{word}:{index}")
