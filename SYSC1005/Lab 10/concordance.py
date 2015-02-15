import string

def build_histogram(filename):
    
    infile = open(filename, "r")
    dct = {}
    n = 0
    for line in infile:
        n = n + 1  
        word_list = line.split()
        
        for word in word_list:
            w = word.strip(string.punctuation).lower()
            
            if w != '':
                lst = dct.get(w, []) 
                lst.append(n)
                dct[w] = lst
    return dct

filename = input()               
hist = build_histogram(filename)
words = sorted(hist.keys())
for w in words:
    print (w ," : ", hist[w])