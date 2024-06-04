from collections import Counter

def topk_frequent(words, k):
    # Use the counter library to count the frequency of each word
    count = Counter(words)
    
    # Sort the words by decreasing frequency and lexicographical order
    sorted_words = sorted(count.items(), key=lambda item : (-item[1], item[0]))
    
    return [word for word, freq in sorted_words[:k]]


# Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
output = topk_frequent(words, k)
print(output)
    