# put your code here.
def count_words(filename):
    """Return dict of words and # of occurrences in textfile"""

    # Open text file
    text = open(filename)

    # Initialize word-count dictionary
    word_count = {}
    
    # Iterate over each line of text file
    for line in text:
        
        # Strip any extra spacing at the end of line
        line = line.rstrip()

        # Create list of words in each line (space-separated)
        words = line.split(" ")
        
        # Iterate over words and add into word_count dict
        for word in words:

            # Strip any punctuation marks at the end of word
            word = word.rstrip("?!.,")

            # Store word as key and occurences of word as value in word_count
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count