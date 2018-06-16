inputSentence = input('Enter the sentence:')
listWords = inputSentence.split()
mid_index = int(len(listWords)/2)

def mid_words(listWords): # function to find the middle words in the sentence
    middle_words = [] #append the list of middle words to this variable
    if len(listWords) % 2 == 0: #if sentence contains even number of words then it has two middle words
        middle_words.append(listWords[mid_index - 1]) #1st middle word is len(listWords)/2 -1 th word
        middle_words.append(listWords[mid_index]) #2nd middle word is len(listWords)/2 th word
    else:#if sentence contains odd number of words
        middle_words.append(listWords[mid_index])#middle word is len(listWords)/2
    return middle_words

def longest_keyword(listWords):#function to find the longest word in the list
    return max(listWords,key=len) #max function to find out the word having the maximum length

def reverse_sentence(listWords):# function to reverse all the words in the sentence
    reverse_sentence = ''
    for i in range(len(listWords)):#iterate through the each word in the sentence
        reverse_sentence = reverse_sentence + ' '+listWords[i][::-1]#reverse each word and add it to reverse sentence var
    return reverse_sentence

print('Middle words in the sentence : ',mid_words(listWords))
print('Longest word in the sentence : ',longest_keyword(listWords))
print('Reverse of ech words in the sentence:',reverse_sentence(listWords))