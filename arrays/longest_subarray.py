from collections import deque


def character_replacement(s, k):
    char_count = {}
    left = 0
    max_count, max_length = 0, 0
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        max_count = max(max_count, char_count[s[right]])
        
        if right - left + 1 - char_count > k:
            char_count[s[left]] -= 1
            left += 1
            
        max_length = max(max_length, right - left + 1)
    
    return max_length


# def longest_subarray(nums, limit):
#     max_q = deque()
#     min_q = deque()
    
#     left = 0
#     max_length = 0
    
#     for right in range(len(nums)):
#         while max_q and nums[right] > max_q[-1]:
#             max_q.pop()
#         max_q.append(nums[right])
        
#         while min_q and nums[right] < min_q[-1]:
#             min_q.pop()
#         min_q.append(nums[right])
        
#         # If max_q - min_q > limit, shrink the window
#         while max_q[0] - min_q[0] > limit:
#             if nums[left] == max_q[0]:
#                 max_q.popleft()
#             if nums[left] == min_q[0]:
#                 min_q.popleft()
                
#             left += 1
            
#         max_length = max(max_length, right - left + 1)
            
    
#     return max_length


# # Example usage:
# nums = [8, 2, 4, 7]
# limit = 4
# output = longest_subarray(nums, limit)
# print(output)


# def length_of_longest_substring(s):
#     char_set = set()
#     left = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
            
#         char_set.add(s[right])
        
#         max_length = max(max_length, right - left + 1)
    
#     return max_length

# # Example usage
# s = "abcabcbb"
# print(length_of_longest_substring(s))


def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        
        else:
            right -= 1
            
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
    
    return water_trapped

# Example usage
length = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(length))