import string

def build_word_list(filename):
    """ Return a list of all the words in the specified file,
    sorted in ascending order.
    
    Example:
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """
    infile = open(filename, "r")
    word_set = set()

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

            # Don't save any empty strings created when the punctuation marks
            # are removed. For example, if w is bound to a hyphen, '-',
            # w.strip(string.punctuation) yields the empty string, ''.
            
            if w != '':
                # Storing the words in a set removes any duplicates.
                word_set.add(w)

    # Now build the list of words.
    
    word_list = list(word_set)
    
    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()
    return word_list


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


def words_with_frequency(hist, n):
    s = set()
    
    for word in hist:
        if hist[word] == n:
            s.add(word)
    l = list(s)
    l.sort()
    
    return l

