from collections import Counter

def topK_frequent(words, k):
    # Count the frequency of each word in the list
    count = Counter(words)
    
    # Sort the words by decreasing frequency and lexicographical order
    sorted_words = sorted(count.items(), key=lambda i: (-i[1], i[0]))
    
    return [word for word, freq in sorted_words[:k]]

# Example usage:
words = ["i", "leetcode", "love", "i", "leetcode", "i", "love", "leetcode", "coding", "leetcode"]
k = 2
output = topK_frequent(words, k)
print(output)
    