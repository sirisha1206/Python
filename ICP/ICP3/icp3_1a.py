data= input("Enter the sentence:")
word_dict = {}; #dictonary for storing the frequency of the words
words = data.split() #splitting the words seperated by space
words.sort() #sort the words
print(words);
wordfreq = [words.count(p) for p in words] #counting the frequency of words
freq_dict = dict(zip(words, wordfreq)) #storing the frequency of the words in  dictonary
print(freq_dict);
