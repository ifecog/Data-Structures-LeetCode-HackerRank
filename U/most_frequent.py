from collections import Counter

# 1. Top k most frequent nums
def topK_frequent(nums, k):
    # freq = {}
    
    # for num in nums:
    #     freq[num] = freq.get(num, 0) + 1
    
    freq = Counter(nums)
        
    sorted_nums = sorted(freq.keys(), key=lambda i: freq[i], reverse=True)
    
    return sorted_nums[:k]

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topK_frequent(nums, k)) 


def top_K_frequent(words, k):
    freq = Counter(words)
    
    sorted_words = sorted(freq.items(), key=lambda i: (-i[1], i[0]))
    
    return [word for word, count in sorted_words[:k]]

# Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
output = top_K_frequent(words, k)
print(output)