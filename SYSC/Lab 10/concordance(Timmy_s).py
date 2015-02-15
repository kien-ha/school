import string

def build_histogram(filename):

    infile = open(filename, "r")
    hist = {}
    ln = 0
    for line in infile:
        ln += 1
        word_list = line.split()
        
        for word in word_list:
            w = word.strip(string.punctuation).lower()
            
            if w != '':
                count = hist.get(w, []) 
                if ln not in count:
                    count.append(ln)                         
                    hist[w] = count

    sorted_hist = sorted(hist.keys())
    for word in sorted_hist:
        print(word, ":",hist[word])

    return hist
