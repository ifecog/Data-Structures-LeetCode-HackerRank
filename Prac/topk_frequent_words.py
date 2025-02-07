from collections import Counter

def topK_frequent(words, k):
    """Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

    Args:
        words (list): A list of strings
        k (int): a given integer

    Returns:
        list: List of the most frequent words
    """
    # Count the frequency of each word in the list
    count = Counter(words)
    print(count.items())
    
    # Sort the words by decreasing frequency and lexicographical order
    # a. The key for sorting is a tuple (-frequency, word)
    # b. -ve frequency ensures that the words with higher frequencies come first
    # c. word ensures that if the frequencies are the same, they are sorted lexicographically
    sorted_words = sorted(count.items(), key=lambda i: (-i[1], i[0]))
    
    return [word for word, freq in sorted_words[:k]]
    

# Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
output = topK_frequent(words, k)
print(output)
    