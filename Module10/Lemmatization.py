from nltk import WordNetLemmatizer
import nltk

nltk.download("wordnet")

# we can use the WordNetLemmatizer class to lemmatize words. The lemmatizer requires a part of speech (POS) tag to accurately lemmatize words. In this example, we will use the verb POS tag ("v") for lemmatization.

lemmatizer = WordNetLemmatizer()

words = [
    "running",
    "ran",
    "runs",
    "easily",
    "fairly",
    "sportingley",
    "better",
    "best",
    "good",
    "bad",
    "worse",
    "worst",
]
for w in words:
    print(w + "--->" + lemmatizer.lemmatize(w, pos="v"))


