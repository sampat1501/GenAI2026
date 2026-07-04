from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
import nltk

nltk.download("maxent_ne_chunker_tab")

nltk.download("words")

paragraph = """The Eiffel Tower is one of the most famous landmarks in the world, located in Paris, France. It was designed by engineer Gustave Eiffel and completed in 1889 for the World's Fair, which celebrated the 100th anniversary of the French Revolution. The tower stands approximately 330 meters (1,083 feet) tall and was the tallest man-made structure in the world until 1930. Made of iron, the Eiffel Tower attracts millions of visitors every year who come to enjoy its observation decks, stunning views of Paris, and beautiful nighttime illumination. Today, it is a symbol of France and an important cultural and tourist attraction recognized worldwide."""
sentences = sent_tokenize(paragraph)
print(sentences)
print(type(sentences))
word_list = []
for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    word_list = words
    taggged_words = pos_tag(words)
    print(taggged_words)
    named_words = ne_chunk(taggged_words).draw()
    print(named_words)
print(word_list)
