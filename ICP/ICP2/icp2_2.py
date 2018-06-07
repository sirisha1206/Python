fh = open('q2input.txt')
f = open('myfile', 'w')
for line in fh:
    line = line.strip();
    t = line+','+ str(len(line))+'\n'
    f.write(t)
fh.close()
