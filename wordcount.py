"""To run word counter on a file, enter name of file after wordcount.py """

import string
import sys

def get_wordcount(text_file):
    """takes file, returns dictionary with unique words and the number of times
    each word appears"""

    with open(text_file) as the_file:
        all_text = the_file.read() # .read(): makes string with all words in file
        all_text = all_text.split() # makes list out of all words, split

        words_in_file = {}

        for word in all_text:
            if word[-1] in string.punctuation: #remove punctuation
                word = word[:-1]

            word = word.lower()
            words_in_file[word] = words_in_file.get(word, 0) + 1

        # print it pretty
        for word, count in words_in_file.iteritems():
            print word, count

if len(sys.argv) < 2:
    print __doc__
else:
    get_wordcount(sys.argv[1]) #Take the name of file as argument on command line
# get_wordcount("test.txt")
# print sys.argv
print
# get_wordcount("twain.txt")