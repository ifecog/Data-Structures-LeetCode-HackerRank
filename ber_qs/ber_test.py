


# # Top K Frequent Words
# from collections import Counter

# def topK_frequent(words, k):
#     # Count the frequency of the words in the list
#     count = Counter(words)
    
#     # Sort the words by decvreasing frequency and lexicographical order. This is done by using a key that is a tuple (-frequency, word)
#     sorted_words = sorted(count.items(), key=lambda i: (-i[1], i[0]))
    
#     return [word for word, freq in sorted_words[:k]]
    
# # Example usage:
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
# output = topK_frequent(words, k)
# print(output)
  


# # Top K Frequent Elements
# def topK_frequent(nums, k):
#     count = {}
    
#     for num in nums:
#         count[num] = count.get(num, 0) + 1
    
#     sorted_nums = sorted(count.keys(), key=lambda i: count[i], reverse=True)
    
#     # print(count)
#     # print(sorted_nums)
    
#     return sorted_nums[:k]

# # Example usage:
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# print(topK_frequent(nums, k)) 



# # Merge Intervals
# def merged_intervals(intervals):
#     intervals.sort(key=lambda i: i[0])
    
#     merged = []
    
#     for interval in intervals:
#         if not merged or interval[0] >= merged[-1][1]:
#             merged.append(interval)
            
#         merged[-1][1] = max(merged[-1][1], interval[1])
    
#     return merged
            
# # Example usage:
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# result = merged_intervals(intervals)
# print(result)


# # Meeting Scheduler
# def min_available_duration(slots1, slots2, duration):
#     # Sort the slots using ther starting index
#     slots1.sort()
#     slots2.sort()
    
#     # Initiate the starting pointers of each slot to 0
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         if start - end >= duration:
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


# # Uber Count
# def easy_count_uber(coordinates):
#     # Initialize an empty set to store unique markers since sets do not store duplicates
#     markers = set()
    
#     for left, right in coordinates:
#         # Add each marker in the range(left, right) to the set (duplicates are automatically eliminated)
#         for marker in range(left, right + 1):
#             markers.add(marker)
    
#     return len(markers)
    
    
# # Example usage:
# coordinates = [[4, 7], [-1, 5], [3, 6]]
# result = easy_count_uber(coordinates)
# print(result)


# # Number of Trips
# def minimum_time(time, totalTrips):
#     # Left pointer is set to the minimum possible time, 1 unit
#     left = 1
#     # Right pointer is we set to the maximum possible time. This would be the time it takes for the fastest bus to complete all the trips by itself
#     right = min(time) * totalTrips
    
    
#     # Helper function to determine if it is possible to complete the required number of trips within a given maximum time
#     def can_complete_trips(max_time):
#         total_trips = 0
#         for t in time:
#             total_trips += max_time // t
            
#         return total_trips >= totalTrips
    
    
#     # Binary search implementation
#     while left < right:
#         mid = (right + left) // 2
        
#         if can_complete_trips(mid):
#             right = mid
#         else:
#             left = mid + 1
    
#     # When the left pointer meets the right pointer, we have found the minimum time
#     return left


# # Example usage:
# time_period = [2, 3, 5]
# total_trips_taken = 8
# print(minimum_time(time_period, total_trips_taken))



# # Permutation
# def permute(nums):
#     result = []
    
#     def backtrack(start):
#         if start == len(nums):
#             result.append(nums[:])
        
#         for i in range(start, len(nums)):
#             nums[start], nums[i] = nums[i], nums[start]
            
#             backtrack(start + 1)
            
#             nums[start], nums[i] = nums[i], nums[start]
            
#     backtrack(0)
    
#     return result


# # # example test
# # test_nums = [1, 2, 3]
# # print(permute(test_nums))



# # Fibonacci
# def fibonacci_iteration(n):
#     if n <= 0:
#         return 'Number must be grater than 0'
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
    
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
#     return fib_sequence[-1]        
        
# a = 8
# print(fibonacci_iteration(a))


# # Check if a number is a power of 4
# def is_power_of_four(n):
#     if n <= 0:
#         return False
    
#     while n % 4 == 0:
#         n //= 4
    
#     return n == 1


# # Example usage:
# print(is_power_of_four(16)) 
# print(is_power_of_four(15)) 


# def is_power_of_three(n):
#     if n <= 0:
#         return False
    
#     while n % 3 == 0:
#         n //= 3
    
#     return n == 1


# # Example usage:
# print(is_power_of_three(27)) 
# print(is_power_of_three(30)) 


# Check if a number is the sum of the powers of 3
def check_powers_of_three(n):
    while n > 0:
        if n % 3 == 2:
            return False
        
        n //= 3
    
    return True
    