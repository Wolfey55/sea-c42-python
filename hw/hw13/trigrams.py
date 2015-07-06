import sys
import string
import random

filename = "sherlock_small.txt"
d = {}

def read_data(file_name):

    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()

        text = ""
        for line in range(len(lines)):
            text += lines[line]
            #text.extend(line)

        #text = text.split('--')
        return text

    except IOError as e:
        print(str(e))
        sys.exit(1)


def strip_punctuation(texts):

    punctuation = string.punctuation
    punctuation = string.punctuation.replace("'", "")  # keep apostropies
    punctuation = string.punctuation.replace("-", "")  # keep hyphon
    table = dict([(ord(c), None) for c in punctuation])

    # lower-case everything to remove that complication:
    texts = texts.lower()

    # remove punctuation
    texts = texts.translate(table)

    # split into words
    words = texts.split()
    words = texts.split("--")

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    words = [word for word in words if word != "'"]

    print(words)
    return words

    #for (i, word) in enumerate(words):
        #d[(words[i], words[i + 1])] = [words[i + 2]]
    #print(d)


if __name__ == "__main__":

    read_data(filename)

    strip_punctuation(read_data(filename))

    print(string.punctuation)



