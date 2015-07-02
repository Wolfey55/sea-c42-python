try:
    f = open('sherlock_small.txt', 'r')
    lines = f.readlines()
    f.close()
    d = {}
    words = ""
    for line in range(len(lines)):
        #lines[line].split()
        words += lines[line]
        for word in words:
            #words[word].append(word.split())
            words.split('-')
    print(words)
    #for (i, word) in enumerate(words):
        #d[(words[i], words[i + 1])] = [words[i + 2]]
    #print(d)

except IOError as e:
    print(str(e))


