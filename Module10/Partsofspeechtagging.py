import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk import word_tokenize

nltk.download("averaged_perceptron_tagger_eng")


paragraph = (
    "My dear young friends, Dream, dream, dream. Dreams "
    "transform into thoughts, and thoughts result in action. "
    "You have to dream before your dreams can come true. "
    "Never be afraid of aiming high. Difficulties are a part "
    "of life; they are meant to make us stronger and help us "
    "appreciate success. Every young person has the power to "
    "change the nation through knowledge, hard work, and "
    "determination. Let your dreams become your mission. "
    "Believe in yourself, work with integrity, and never give "
    "up. A developed and prosperous nation can be built when "
    "its youth dare to dream and have the courage to act on "
    "those dreams. Small aim is a crime; have great aim. "
    "Thank you."
)

sentences = sent_tokenize(paragraph)

# prepare stopwords set once (use lowercase for comparison)
stopwords_set = set(stopwords.words("english"))

for sentence in sentences:
    words = word_tokenize(sentence)
    # remove stopwords (case-insensitive)
    filtered_words = [w for w in words if w.lower() not in stopwords_set]

    # remove punctuation and duplicate words while preserving order
    seen = set()
    unique_words = []
    for w in filtered_words:
        key = w.lower()
        # keep tokens that contain at least one alphabetic character
        if key not in seen and any(c.isalpha() for c in w):
            seen.add(key)
            unique_words.append(w)

    pos_words = nltk.pos_tag(unique_words)
    print(pos_words)

# print(sentences)
