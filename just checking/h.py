from nltk import word_tokenize
from nltk.corpus import stopwords
import re

text = "HEllo , what's your plan today? Where you are going tomorrow?"

text = re.sub(r"[^A-Za-z]"," ",text.lower())
print(text)

tokens = word_tokenize(text.lower())

print(tokens)

stop_words = stopwords.words('english')

filtered = [w for w in tokens if not w in stop_words]

print(filtered)


