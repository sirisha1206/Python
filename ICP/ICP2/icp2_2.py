fh = open('q2input.txt')
for line in fh:
    line = line.strip();
    print(line,',',len(line))
fh.close()
