vowels = {'a','e','i','o','u'} #storing the vowels in a set
no_of_vowels = 0; #initialize the vowels count to 0
data = input('Enter the input data:') #taking the input from the user
for i in range(len(data)): #iterate through each character in the input
    if data[i] in vowels: #using 'in' operator to check whether the character is an vowel
        no_of_vowels = no_of_vowels + 1 #if the character is a vowel increase the count

print(no_of_vowels)