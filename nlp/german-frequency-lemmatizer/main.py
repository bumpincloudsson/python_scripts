import spacy
import re  # regular expression
import nltk  # natural language toolkit
import string
from pathlib import Path


# download de_core like this -> python -m spacy download de_core_news_sm
nlp = spacy.load('de_core_news_sm')


# save text file content into original_text within current dir
text = Path('./analyze.txt').read_text()
# format and get rid of any line breaks
text = re.sub(r'\s+', ' ', text)


nltk.download('punkt')
nltk.download('stopwords')


stopwords = nltk.corpus.stopwords.words('german')


def preprocess(text):
   formatted_text = text.lower()
   rid = ['``', "'s", "''", "--", "'"]
   tokens = []
   for token in nltk.word_tokenize(formatted_text):
       tokens.append(token)
   tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation and word not in rid]
   formatted_text = ' '.join(element for element in tokens)


   return formatted_text

# use nltk to break up the text block into individual words and then save them in this string
formatted_text = preprocess(text)


doc = nlp(formatted_text)


freqs = []
for token in doc:
   # print(token.text, token.lemma_)
   freqs.append(token.lemma_)


# convert formatted_text tokens into lemmas, save them in freqs as a list, then bring them together
# as a string and save in new_text
new_text = ' '.join(element for element in freqs)


# rank each lemma by frequency
word_frequency = nltk.FreqDist(nltk.word_tokenize(new_text))


# extract the top 20 into a list
frequency_list = word_frequency.most_common(20)


# write each list item on new text file
with open(r'output.txt', 'w') as fp:
   fp.write("\n".join(str(item) for item in frequency_list))

print("Frequency list is saved in output.txt")
