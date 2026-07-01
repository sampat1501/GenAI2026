import nltk
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize

nltk.download("stopwords")

from nltk.corpus import stopwords

# APJ Abdul Kalam Famous speech
paragraph = """Apj Abdul Kalam was a great scientist and the 11th President of India. He was born on October 15, 1931, in Rameswaram, Tamil Nadu. Kalam played a pivotal role in India's civilian space program and military missile development, earning him the nickname "Missile Man of India." He was also a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honor. Kalam's vision for India was centered around education, innovation, and national development. He inspired millions of people with his speeches and writings, emphasizing the importance of dreaming big and working hard to achieve those dreams. His legacy continues to influence and motivate individuals across the country and beyond."""

sentences = sent_tokenize(paragraph)
type(sentences)
print(sentences)
print(type(sentences))
