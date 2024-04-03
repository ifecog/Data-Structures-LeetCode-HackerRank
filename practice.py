from collections import deque

def longest_subarray(nums, limit):
    # store the max and min values of the current sub array using the deque class
    max_queue = deque()
    min_queue = deque()
    
    # initialize the left pointer of the array and the initial result to 0
    left = 0
    result = 0
    
    for right, num in enumerate(num):
        # update max_queue: while 'max_queue' is not empty and current num is greater than the last element in 'max_queue'
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        # update min_queue: while 'min_queue' is not empty and current num is less than the last element in 'min_queue'
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
        while max_queue[0] - min_queue[0] > limit:
            
            left += 1
            
        
        
    
    return result


# def min_available_duration(slots1, slots2, duration):
#     # sort both slot arrays based on the start time
#     slots1.sort()
#     slots2.sort()
    
#     # iterate through the pair of time slots using pointers for each
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         # find the overlap interval
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         # if overlap duration is gte to the duration, return the slot
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
print(result) 