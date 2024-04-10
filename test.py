# # 6
# def permute(nums):
#     result = []
    
#     def backtrack(start):
#         if start == len(nums):
#             return result.append(nums[:])
        
#         for i in range(start, len(nums)):
#             nums[start], nums[i] = nums[i], nums[start]
            
#             backtrack(start + 1)
            
#             nums[start], nums[i] = nums[i], nums[start]
    
#     backtrack(0)
    
#     return result

# # example test
# test_nums = [1, 2, 3]
# print(permute(test_nums))


# 5. 
def merged_intervals(intervals):
    # sort the intervals based on their starting point
    intervals.sort(key=lambda i : i[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merged_intervals(intervals)
print(result)


# # 4
# from collections import deque

# def longest_subarray(nums, limit):
#     max_queue = deque()
#     min_queue = deque()
    
#     left = 0
#     result = 0
    
#     for right, num in enumerate(nums):
#         while max_queue and num > max_queue[-1]:
#             max_queue.pop()
#         max_queue.append(num)
        
#         while min_queue and num < min_queue[-1]:
#             min_queue.pop()
#         min_queue.append(num)
        
#         while max_queue[0] - min_queue[0] > limit:
#             if max_queue[0] == nums[left]:
#                 max_queue.popleft()
#             if min_queue[0] == nums[left]:
#                 min_queue.popleft()
#             left += 1
        
#         result = max(result, right - left + 1)
    
#     return result


# # Example usage:
# nums = [8, 2, 4, 7]
# limit = 4
# output = longest_subarray(nums, limit)
# print(output)

# # 3
# def closest_palindrome(n):
#     n = int(n)
    
#     def is_palindrome(s):
#         return s == ''.join(reversed(s))
#         # return s == s[::-1]
        
    
#     def get_smaller_palindrome(x):
#         x -= 1
#         while x > 0 and not is_palindrome(str(x)):
#             x -= 1
        
#         return x
    
    
#     def get_higher_palindrome(x):
#         x += 1
#         while True:
#             if is_palindrome(str(x)):
#                 return x
#             x += 1
            
#     smaller_palidrome = get_smaller_palindrome(n)
#     higher_palidrome = get_higher_palindrome(n)
    
#     return str(smaller_palidrome) if abs(n - smaller_palidrome) <= abs(higher_palidrome - n) else str(higher_palidrome)
        

# # Example usage:
# n = "1234"
# output = closest_palindrome(n)
# print(output)
            

# # 2
# def min_available_duration(slots1, slots2, duration):
#     # sort both arrays based on the start time
#     slots1.sort()
#     slots2.sort()
    
#     # iterate through the pair of time slots
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         # find the overlapping interval
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         # if the overlap duration is greater than or equal to the duration, return the duration
#         if end - start >= duration:
#             return [start, start + duration]
        
#         # move to the next time slot with the earlier end time
#         if slots1[i][1] < slots2[j][1]:
#             i += 1
#         else:
#             j += 1
        
#     return []

# # Example usage:
# slots1 = [[10,50],[60,120],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 8
# print(min_available_duration(slots1, slots2, duration))


# 1.
# def height_checker(heights):    
#     expected = sorted(heights)
    
#     # solution 1
#     count = 0
#     for i in range(len(heights)):
#         if heights[i] != expected[i]:
#             count += 1
            
#     # solution 2
#     count = sum(h1 != h2 for h1, h2 in zip(heights, expected)) 
    
#     return count

# # Example usage:
# heights = [1,1,4,2,1,3]
# result = height_checker(heights)
# print(result) 