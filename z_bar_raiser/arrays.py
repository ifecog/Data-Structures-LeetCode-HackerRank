# 2. Top K frequent words
from collections import Counter

def topK_frequent(words, k):
    # Count the frequency of each word in the list
    count = Counter(words)
    
    sorted_words = sorted(count.items(), key=lambda i: (-i[1], i[0]))
    
    return [word for word, freq in sorted_words[:k]]

# Example usage:
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
output = topK_frequent(words, k)
print(output)


# # 1. Top K frequent elements
# def topK_frequent(nums, k):
#     # This is solved using hash map
#     count = {}
    
#     # Iterate over the array and increment the count of each element in the dictionary
#     for num in nums:
#         count[num] = count.get(num, 0) + 1
        
#     # Sort based on frequency from the highest to the lowest
#     sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
#     return sorted_nums[:k]
    
# # Example usage:
# nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
# k = 2
# print(topK_frequent(nums, k)) 


from collections import deque

def longest_subarray(nums, limit):
    # Store the min and max values of the current window using double ended queues
    max_queue = deque()
    min_queue = deque()
    
    left = 0
    result = 0
    
    for right, num in enumerate(nums):
        # Maintain max queue in decreasing order
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        # Maintain max queue in decreasing order
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
        # If the difference between the max queue and the min queue exceeds the limit, shrink the window from the left
        while max_queue[0] - min_queue[0] > limit:
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            if min_queue[0] == nums[left]:
                min_queue.popleft()
            left += 1
            
        result = max(result, right - left + 1)
    
    return result

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)