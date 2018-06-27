from stemming.porter2 import stem

f = open('words.txt')
for line in f:
    l = line.strip()
    if len(l) > 0:
        print("%s\t%s" % (l, stem(l)))
    else:
        print("")
f.close()



