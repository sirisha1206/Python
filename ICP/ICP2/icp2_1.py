data= input("Enter the elements of the list")

words = data.split()
tuple(words)

words_length = [len(x) for x in data.split()]
tuple(words_length)

words_length_pair = list(zip(words_length,words))
print(words_length_pair)

sorted_list = sorted(words_length_pair)
print(sorted_list)

print(sorted_list[-1])