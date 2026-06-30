from nltk.stem import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

words = [
    "eat",
    "eating",
    "eaten",
    "program",
    "programming",
    "sit",
    "sat",
    "sitting",
    "run",
    "ran",
    "running",
    "History",
    "Write",
    "Writing",
    "Finally",
    "Final",
    "Finalize",
]

stemmer = PorterStemmer()
for w in words:
    print(f"{w} ===============>{stemmer.stem(w)}")

print("*****************************Separation*******************************")

# RegexStemmer

regex_stemmer = RegexpStemmer("ing$|s$|e$|able$,|ly$,en$", min=6)
for w in words:
    print(f"{w}=======>{regex_stemmer.stem(w)}")

snowball_stemmer = SnowballStemmer("english")
for w in words:
    print(w + "-------------" + snowball_stemmer.stem(w))
