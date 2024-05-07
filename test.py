def minimum_time(time, totalTrips):
    left = 1
    right = min(time) * totalTrips
    
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
            
        return total_trips >= totalTrips
    
    while left < right:
        mid = (left + right) // 2
        
        if can_complete_trips(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))



# def merged_intervals(intervals):
#     # sort the intervals based on their starting index
#     intervals.sort(key=lambda i: i[0])
    
#     merged = []
#     for interval in intervals:
#         # Append the merged list with the current interval if the list is empty of the current interval does not overlap with the last merged interval.
#         if not merged or interval[0] > merged[-1][1]:
#             merged.append(interval)
        
#         # Merge overlapping intervals by updating the end point of the last merged interval
#         merged[-1][1] = max(merged[-1][1], interval[1])
    
#     return merged

# # Example usage:
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# result = merged_intervals(intervals)
# print(result)


# def min_available_duration(slots1, slots2, duration):
#     slots1.sort()
#     slots2.sort()
    
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         if end - start >= duration:
#             return [start, start + duration]
        
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

# slots1 = [[10,50],[60,120],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 12
# print(min_available_duration(slots1, slots2, duration))


# def length_of_longest_substring(s):
#     # Ths is solved using the sliding window approach
#     char_index_map = {}
#     left = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         # If right index is alread in char_index_map and its character is greater than or equal to 'left', it means that the character is repeating within the current window. :. Update left to the index after the last occcurrence ot the repeating character.
#         if s[right] in char_index_map and char_index_map[s[right]] >= left:
#             left = char_index_map[s[right]] + 1
            
#         char_index_map[s[right]] = right
#         max_length = max(max_length, right - left + 1)
    
#     return max_length
        

# s = "abcabcbb"
# print(length_of_longest_substring(s))

# def leftmost_column_with_one(binaryMatrix):
#     # Initiaize row and col
#     row, col = 0, len(binaryMatrix) - 1
#     leftmost_col = -1
    
#     while row < len(binaryMatrix) and col >= 0:
#         if binaryMatrix[row][col]:
#             leftmost_col = col
#             col -= 1
#         row += 1
    
#     return leftmost_col


# # Example usage:
# binaryMatrix = [
#     [0, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1],
#     [0, 0, 0, 0]
# ]

# print(leftmost_column_with_one(binaryMatrix)) 