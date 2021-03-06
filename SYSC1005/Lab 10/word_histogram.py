"""
SYSC 1005 A Fall 2014 - Using a Dictionary to Implement a Histogram
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse the Library Reference, Section 6.1, in the Python 3.4.1 
# documentation (available @ python.org).

def build_histogram(filename):
    """ Return a histogram of the words in the specified file.
    (A histogram is a set of counters. In this example, each counter
    keeps track of the number of occurrences of one word.)
     
    Example:
    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file?
    >>> most_frequent_word(hist)  # Which word occurs most often?
    """

    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # The split method removes the whitespace from around each word.
        word_list = line.split()

        # For each word, remove any punctuation marks immediately
        # before and after the word, then convert it to lower case.
        
        for word in word_list:
            w = word.strip(string.punctuation).lower()
            
            # or, 
            # w = word.strip(string.punctuation)
            # w = w.lower()

            # Don't count any empty strings created when the punctuation marks
            # are removed. For example, if w is bound to a hyphen, '-',
            # w.strip(string.punctuation) yields the empty string, ''.
            
            if w != '':
                count = hist.get(w, 0)  # get returns the current count of the 
                                         # number of occurrences of word w, 
                                         # or 0 if w is not yet in the 
                                         # dictionary.
                hist[w] = count + 1

            # or simply,
            # hist[w] = hist.get(w, 0) + 1

    return hist


def most_frequent_word(hist):
    """ Return a tuple containing the most frequently occurring word in the 
    specified histogram (a dictionary of word/frequency pairs), along with its 
    frequency.
    """
    max_frequency = -1
    for word in hist:
        if hist[word] > max_frequency:
            max_frequency = hist[word]
            most_frequent = word
    
    return (most_frequent, max_frequency)
