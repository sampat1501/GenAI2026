import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer

# download once
nltk.download("punkt")
nltk.download("punkt_tab")

corpus = """My School

My school's is very big. It has a beautiful playground!
I love my school.

Our's teachers are very helpful. They teach us very well.
We respect them."""

print(corpus)

sentences = sent_tokenize(corpus, language="english")

print(sentences)

words = word_tokenize(corpus)
print(words)

for sent in sentences:
    words = word_tokenize(sent)
    print(words)
    print("This is dividing line =====================================")
    words1 = wordpunct_tokenize(sent)
    print(words1)
    print("This is dividing line =====================================")
    tokeniser = TreebankWordTokenizer()
    word_bank = tokeniser.tokenize(sent)
    print(word_bank)
