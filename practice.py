def permute(nums):
    result = []
    
    # def a nested bactrack function
    def backtrack(start):
        # when start reaches the length of num, make a copy of the current permutation
        if start == len(nums):
            return result.append(nums[:])
        
        # iterare through nums from start and swap the current element with the element in the start index
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            
            # recursively backtrack for the remaning elements by calling the backtrack function
            backtrack(start + 1)
        
            # swap back to the original order to explore other possibolities
            nums[i], nums[start] = nums[start], nums[i]
    
    # set the backtrack start parameter to 0 for the nums array
    backtrack(0) 
    
    return result

# example test
test_nums = [1, 2, 3]
print(permute(test_nums))


# from collections import deque

# def longest_subarray(nums, limit):
#     # store the max and min values of the current sub array using the deque class
#     max_queue = deque()
#     min_queue = deque()
    
#     # initialize the left pointer of the array and the initial result to 0
#     left = 0
#     result = 0
    
#     for right, num in enumerate(nums):
#         # update max_queue: while 'max_queue' is not empty and current num is greater than the last element in 'max_queue'
#         while max_queue and num > max_queue[-1]:
#             max_queue.pop()
#         max_queue.append(num)
        
#         # update min_queue: while 'min_queue' is not empty and current num is less than the last element in 'min_queue'
#         while min_queue and num < min_queue[-1]:
#             min_queue.pop()
#         min_queue.append(num)
        
#         # while the difference between max queue and min queue is gt the limit, increment the left pointer and pop elements from both 'max_queue' and 'min_queue' from the left until the condition is met
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


# def height_checker(heights):
#     expected = sorted(heights)
    
#     # count = 0
#     # for i in range(len(heights)):
#     #     if heights[i] != expected[i]:
#     #         count += 1
    
#     count = sum(h1 != h2 for h1, h2 in zip(heights, expected))
    
#     return count

# # Example usage:
# heights = [1,1,4,2,1,3]
# result = height_checker(heights)
# print(result) 


# def closest_palindrome(n):
#     # convert n to int for the purpose of iteration
#     n = int(n)
    
#     # def a nested function to determine palindromic status
#     def is_palindrome(s):
#         return s == s[::-1]
    
#     # def nested function to determine nearest smaller palindome
#     def get_smaller_palindrome(x):
#         x -= 1
#         while x > 0 and not is_palindrome(str(x)):
#             x -= 1
        
#         return x
    
#     # def nested function to determine nearest higher palindrome
#     def get_higher_palindrome(x):
#         x += 1
#         while True:
#             if is_palindrome(str(x)):
#                 return x
#             x += 1
            
#     # assign variable names to smaller and higher palindrome
#     smaller_palindrome = get_smaller_palindrome(n)
#     higher_palindrome = get_higher_palindrome(n)
    
#     return str(smaller_palindrome) if abs(n - smaller_palindrome) <= abs(higher_palindrome - n) else str(higher_palindrome)

# # Example usage:
# n = "1234"
# output = closest_palindrome(n)
# print(output)


# def min_available_duration(slots1, slots2, duration):
#     # sort the time slots based on their starting time
#     slots1.sort()
#     slots2.sort()
    
#     # initialize pointers for both time slots and iterate through the pair of time slots
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         # find the overlapping interval
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         # if overlapping interval is gte the duration, return the slot
#         if start - end >= duration:
#             return [start, start + duration]
        
#         # move to the next time slot with an earlier end time
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
