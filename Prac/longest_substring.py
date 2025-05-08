def length_of_longest_substring(s):
    """Given a string s, find the length of the longest 
    substring without repeating characters.

    Args:
        s (string): a string of characters

    Returns:
        int: length of the longest substring without repeating characters
    """
    
    # This is solved using the sliding window approach and a hash set
    # Initialize 2 pointers to represent the window. If s[right] is not in the window, add it and update the max length
    # if s[right] is in the window, move left to remove s[left] from the window so that no duplicates remain.
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
    
    
# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))

from collections import deque
def longest_subarray(nums, limit):
    if not nums:
        return 0
    
    max_q = deque()
    min_q = deque()
    
    left = 0
    max_length = 0
    
    for right in range(len(nums)):
        while max_q and nums[right] > max_q[-1]:
            max_q.pop()
        max_q.append(nums[right])
        
        while min_q and nums[right] < min_q[-1]:
            min_q.pop()
        min_q.append(nums[right])
        
        while max_q[0] - min_q[0] > limit:
            if nums[left] == max_q[0]:
                max_q.popleft()
            if nums[left] == min_q[0]:
                min_q.popleft()
                
            left += 1
            
        max_length = max(max_length, right - left + 1)
    
    return max_length
    
# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)
