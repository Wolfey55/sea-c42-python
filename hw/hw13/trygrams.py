try:
    f = open('sherlock_small.txt', 'r')
    lines = f.readlines()
    f.close()
    d = {}
    words = []
    for line in lines:
        words.extend(line.split())

    print(words)
    #for (i, word) in enumerate(words):
        #d[(words[i], words[i + 1])] = [words[i + 2]]
    #print(d)

except IOError as e:
    print(str(e))


