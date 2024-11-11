from collections import Counter

def compute_word_frequency(text):
    # Split the text into words, converted into the lowercase for case-insensitive
    words = text.lower().split()

    # Use Counter to count the frequency of each word
    word_count = Counter(words)

    # Sort the word count by key (word) alphanumerically
    sorted_word_count = sorted(word_count.items())
    #print(sorted_word_count)
    return sorted_word_count
