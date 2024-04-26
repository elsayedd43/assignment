import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


with open('C:/Users/asus/Downloads/random_paragraphs.txt') as file:
    text = file.read()


nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]


word_freq = Counter(filtered_words)


for word, freq in word_freq.items():
    print(f"{word}: {freq}")
