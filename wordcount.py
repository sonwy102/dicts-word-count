# put your code here.
def count_words(filename):

    text = open(filename)
    word_count = {}
    
    for line in text:

        line = line.rstrip()
        words = line.split(" ")
        
        #iterate over words and add into word_count dict
        for word in words:

            word = word.rstrip("?!.,")
            word_count[word] = word_count.get(word, 0) + 1
    
    print(word_count)