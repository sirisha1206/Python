import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
#reading the file sample
f1 = open('sample','r',encoding="utf-8")
#save the file data in a variable
data = f1.read()

#Tokentization
stokens = nltk.sent_tokenize(data)
wtokens = nltk.word_tokenize(data)

#Lemmatizer
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!Lemmatizer!!!!!!!!!!!!!!!!!!!!!!!!')
lemmatizer = WordNetLemmatizer()
for w in wtokens:
    print(lemmatizer.lemmatize(w))

#bigrams
print('!!!!!!!!!!!!!!!!!!!!!!!Bigrams!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
bgram = ngrams(wtokens,2)
bigrams = []
for t in bgram:
    bigrams.append(t)
print(bigrams)

#word frequency
bigrams_frequencies = nltk.FreqDist(bigrams)
bigrams_frequencies_count = bigrams_frequencies.most_common()
print('!!!!!!!!!!!!!!bigram frequency!!!!!!!!!!!!!!!!')
print(bigrams_frequencies_count)

print('!!!!!!!!!!!!!!!!!!Top 5 bigrams!!!!!!!!!!!!!!!')
bigrams_frequencies_top5 = bigrams_frequencies.most_common(5)
print(bigrams_frequencies_top5)

#finding the sentences with most frequent bigrams
rep_sent_list = []
for s in stokens:
    for word, words in bigrams:
        for ((p,q), l) in bigrams_frequencies_top5:
            if (word, words == p,q):
                if (s not in rep_sent_list):
                    rep_sent_list.append(s)
print('Sentences with most frequent bigrams:')
#concatinating the sentences with most frequent bigrams
rep_sent = ""
for i in rep_sent_list:
    rep_sent = rep_sent + i
    print(i)
print('Concatinating the sentences with most frequent bigrams:')
print(rep_sent)




