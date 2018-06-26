import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk import wordpunct_tokenize,pos_tag,ne_chunk

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")

result_list = soup.findAll('p')
f = open('input.txt','w+',encoding="utf-8")

for p in range(1,5):
    f.write(result_list[p].get_text())
f.close()

f1 = open('input.txt','r',encoding="utf-8")
data = f1.read()

#Tokentization
stokens = nltk.sent_tokenize(data)
wtokens = nltk.word_tokenize(data)

print('!!!!!Tokenization!!!!!!')
for s in stokens:
    print(s)

for w in wtokens:
    print(w)

print('!!!!!!!!!!!!!!!!!!Stemming!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#Stemming
lStemmer = LancasterStemmer()
for w in wtokens:
    print(lStemmer.stem(w))

#POS
print('!!!!!!!!!!!!!!!!!!!!!!!!POS!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for w in wtokens:
    print(nltk.pos_tag(nltk.word_tokenize(w)))

#Lemmatizer
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!Lemmatizer!!!!!!!!!!!!!!!!!!!!!!!!')
lemmatizer = WordNetLemmatizer()
for w in wtokens:
    print(lemmatizer.lemmatize(w))

#Named entity recognition
print('!!!!!!!!!!!!!!!!!!Named Entity Recognition!!!!!!!!!!!!!!!!!!!!!!!!')
for s in stokens:
    print(ne_chunk(pos_tag(wordpunct_tokenize(s))))

#trigrams
print('!!!!!!!!!!!!!!!!!!!!!!!Trigrams!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
tgram = ngrams(wtokens,3)
for t in tgram:
    print(t)