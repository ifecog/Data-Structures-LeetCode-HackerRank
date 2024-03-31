# 3


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

# Example usage:
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
print(min_available_duration(slots1, slots2, duration))


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