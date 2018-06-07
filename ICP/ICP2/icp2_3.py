fh = open('q3input.txt')
for line in fh:
    word_count = 1;
    for i in line:
        if(i == ' '):
            word_count = word_count + 1;
    print(line.strip(),',',word_count);
fh.close()
