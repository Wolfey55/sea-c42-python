import sys
import string
import random
import io

# file to be imported
filename = "sherlock.txt"


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
        return " ".join(full_text)

    except IOError as e:
        print(str(e))
        sys.exit(1)


def strip_punctuation(texts):

    # function to evaluate whether characters in texts are punctuation.
    def is_punctuation(char):

        # if char is an apostrophy return False
        if char is "'":
            return 0
        # if char is a hyphon retrun False
        elif char is '-':
            return 0
        # if char is any other punctuation retrun True
        elif char in string.punctuation:
            return 1
        # any number or letter return False
        else:
            return 0

    stripped_text = ''
    # iterate through every character in texts.
    for char in texts:
        # if is_punctuation function returns False for said character:
        if is_punctuation(char) is 0:
            # add character to new text
            stripped_text += char

    # lower-case everything to remove that complication:
    stripped_text = stripped_text.lower()

    # replace all the '--' and '-' with a space
    stripped_text = stripped_text.replace('--', ' ')
    stripped_text = stripped_text.replace('-', ' ')

    # remove punctuation
    # texts = texts.translate(table)

    # split into words
    words = stripped_text.split()

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    words = [word for word in words if word != "'"]

    return words


def trigram_constructor(words):

    word_pairs = {}

    # iterate through words stopping short of the end to prevent error
    for w in range(len(words) - 2):
        # takes the current index and following index and makes a tuple
        # this will be used as word_pairs key
        leading_pair = tuple(words[w:w+2])
        # assigns the word following the tuple
        # this will be used as the word_pairs value
        follower = words[w+2]
        # if the leading pair is already in word_pairs:
        if leading_pair in word_pairs:
            # append the 'follower' word in the value list
            word_pairs[leading_pair].append(follower)
        # If leading pair is not in word_pairs:
        else:
            # create new tuple(key):[value]
            word_pairs[leading_pair] = [follower]

    return word_pairs


def create_text(word_pairs):

    # create an empty list for the new story to be stored in.
    new_story = []

    # makes 100 sentences.
    for i in range(100):
        # create list of the keys in word_pairs.
        key_list = list(word_pairs.keys())
        # select a random index of key_list to start the sentence.
        sentence = list(random.choice(key_list))

        for j in range(random.randint(2, 10)):
            # create new word_pairs[key] from the last two words in sentence.
            pair = tuple(sentence[-2:])
            if pair in word_pairs:
                # append a randomly chosen value for matching key
                sentence.append(random.choice(list(word_pairs[pair])))
            else:
                # if the pair doesn't exist, end sentence.
                break
        # capitalize beginning of sentence
        sentence[0] = sentence[0].capitalize()
        # add period at the end of sentence
        sentence[-1] += '.'
        new_story.extend(sentence)

    new_story = " ".join(new_story)

    print(new_story)
    return new_story

if __name__ == "__main__":

    # strip_punctuation(read_data(filename))

    create_text(trigram_constructor(strip_punctuation(read_data(filename))))
