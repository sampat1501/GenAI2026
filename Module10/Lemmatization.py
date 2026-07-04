from nltk import WordNetLemmatizer
from nltk import word_tokenize
from nltk import pos_tag
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


# Lemmatization difference

sentence = "The boys are playing games."
# Tokenize
words = word_tokenize(sentence)

# POS tagging
print(pos_tag(words))

print(words)
print("Words after Lemmatization=======")
lemma_words = []
for word in words:
    lemma_words.append(lemmatizer.lemmatize(word, pos="v"))
print(lemma_words)
