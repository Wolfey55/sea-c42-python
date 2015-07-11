import sys
import string
import random
import io

filename = "sherlock_small.txt"
d = {}

def read_data(file_name):

    try:
        # Open the file, read content by line and close.
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()

        # Read through lines and put content in a list.
        full_text = []
        for line in range(len(lines)):
            full_text.append(lines[line])

        # Joins all the items in full_text to create one string.
        print(" ".join(full_text))
        return " ".join(full_text)

    except IOError as e:
        print(str(e))
        sys.exit(1)


def strip_punctuation(texts):

    punctuation = string.punctuation
    punctuation = string.punctuation.replace("'", "")  # keep apostropies
    punctuation = string.punctuation.replace("-", "")  # keep single hyphon
    table = dict([(ord(c), None) for c in punctuation])

    # replace all the '--' with a space
    texts = texts.replace('--', ' ')

    # lower-case everything to remove that complication:
    texts = texts.lower()

    # remove punctuation
    texts = texts.translate(table)

    # split into words
    words = texts.split()
    # words = texts.split("--")

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




