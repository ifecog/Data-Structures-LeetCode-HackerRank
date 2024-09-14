def longest_repeating_character_replacement(s, k):
    # This is solved using the sliding window approach
    char_count = {}
    left, max_count, max_length = 0, 0, 0
    
    for right in range(len(s)):
        # Increment the count for the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update the max_count to be the highest count of any character in the window
        max_count = max(max_count, char_count[s[right]])
        
        # If the number of characters that need to be replaced is more than k, shrink the window from the left
        if right - left + 1 - max_count > k:
            char_count[s[left]] -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Example usage:
s = "AABABBA"
k = 1
result = longest_repeating_character_replacement(s, k)
print(result)

# from collections import defaultdict

# def binary_search(values, timestamp):
#     left, right = 0, len(values)
    
#     while left < right:
#         mid = (left + right) // 2
        
#         if values[mid][0] <= timestamp:
#             left = mid + 1
#         else:
#             right = mid
            
#     return left


# class TimeMap:
    
#     def __init__(self):
#         self.data = defaultdict()
        
        
#     def set(self, key, value, timestamp):
#         self.data[key].append((timestamp, value))
        
    
#     def get(self, key, timestamp):
#         if key not in self.data:
#             return ''
        
#         values = self.data[key]
#         idx = binary_search(values, timestamp)
        
#         if idx == 0:
#             return ''
        
#         return values[idx - 1][1]
        