from joblib import parallel_backend
import nltk
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import SnowballStemmer
from nltk import WordNetLemmatizer
from nltk import LancasterStemmer

nltk.download("stopwords")


# APJ Abdul Kalam Famous speech
paragraph = """Apj Abdul Kalam was a great scientist and the 11th President of India. He was born on October 15, 1931, in Rameswaram, Tamil Nadu. Kalam played a pivotal role in India's civilian space program and military missile development, earning him the nickname "Missile Man of India." He was also a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honor. Kalam's vision for India was centered around education, innovation, and national development. He inspired millions of people with his speeches and writings, emphasizing the importance of dreaming big and working hard to achieve those dreams. His legacy continues to influence and motivate individuals across the country and beyond."""

sentences = sent_tokenize(paragraph)
type(sentences)
print(sentences)
print(type(sentences))
print(len(sentences))
stemmer = PorterStemmer()
# print(stopwords.words("english"))

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    filtered_words = [
        stemmer.stem(word)
        for word in words
        if word not in set(stopwords.words("english"))
    ]
    sentences[i] = " ".join(filtered_words)
print(sentences)


# Snowball Stemmmer
print("======================================")
stemmer = SnowballStemmer("english")
sentences = sent_tokenize(paragraph)
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    stemmed_words = [
        stemmer.stem(word)
        for word in words
        if word not in set(stopwords.words("english"))
    ]
    sentences[i] = " ".join(stemmed_words)
print(sentences)

# Lancaster Stemming
print("Lancaster Stemming=====================================")
sentences = sent_tokenize(paragraph)
stemmer = LancasterStemmer()
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    filterd_words = [
        stemmer.stem(word)
        for word in words
        if word not in set(stopwords.words("english"))
    ]
    sentences[i] = " ".join(filterd_words)
print(sentences)

print("Lemmatization ============================")
# Lemmatization
sentences = sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()
stemmer = LancasterStemmer()
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    filterd_words = [
        lemmatizer.lemmatize(word, pos="v").lower()
        for word in words
        if word not in set(stopwords.words("english"))
    ]
    sentences[i] = " ".join(filterd_words)
print(sentences)
