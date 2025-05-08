# """
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
# """

# from collections import defaultdict
# import bisect


# class TimeMap:
#     def __init__(self):
#         self.key_to_timestamps = defaultdict(list)
        
#     def set(self, key, value, timestamp):
#         self.key_to_timestamps[key].append((timestamp, value))
        
#     # def get(self, key, timestamp):
#     #     if key not in self.key_to_timestamps:
#     #         return ''
        
#     #     timestamps = self.key_to_timestamps[key]
        
#     #     idx = bisect.bisect_right(timestamps, (timestamp, chr(127))) - 1
        
#     #     if idx >= 0:
#     #         return timestamps[idx][1]
        
#     #     return ''

#     def get(self, key, timestamp):
#         if key not in self.key_to_timestamps:
#             return ''
        
#         timestamps = self.key_to_timestamps[key]
        
#         left, right = 0, len(timestamps) - 1
#         result = ''
        
#         while left <= right:
#             mid = (left + right) // 2
            
#             if timestamps[mid][0] <= timestamp:
#                 result = timestamps[mid][1]
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return result

    
# timeMap = TimeMap()
# timeMap.set("foo", "bar", 1)
# print(timeMap.get("foo", 1))  # "bar"
# print(timeMap.get("foo", 3))  # "bar"
# timeMap.set("foo", "bar2", 4)
# print(timeMap.get("foo", 4))  # "bar2"
# print(timeMap.get("foo", 5))


# # class TimeMap:
    
# #     def __init__(self):
# #         self.data = defaultdict()
        
# #     # Set method to append a new (timestamp, value) pair to list
# #     def set(self, key, value, timestamp):
# #         self.data[key].append((timestamp, value))
    
    
# #     # Get method to find the value with the largest timestamp
# #     def get(self, key, timestamp):
# #         if key not in self.data:
# #             return ''
        
# #         values = self.data[key]
# #         idx = self.binary_search(values, timestamp)
# #         if idx == 0:
# #             return ''
        
# #         return values[idx - 1][1]
        
    
# #     # Helper function that performs binary search operation
# #     def binary_search(self, values, timestamp):
# #         left, right = 0, len(values)
        
# #         while left < right:
# #             mid = (left + right) // 2
            
# #             if values[mid][0] <= timestamp:
# #                 left = mid + 1 
# #             else:
# #                 right = mid
# #         return left
    
    
# # timeMap = TimeMap()
# # timeMap.set("foo", "bar", 1)
# # print(timeMap.get("foo", 1))  # "bar"
# # print(timeMap.get("foo", 3))  # "bar"
# # timeMap.set("foo", "bar2", 4)
# # print(timeMap.get("foo", 4))  # "bar2"
# # print(timeMap.get("foo", 5))

# class MyCalendar:
#     def __init__(self):
#         self.intervals = []
        
#     def book(self, startTime, endTime):
#         # Find the position to insert the new interval
#         left, right = 0, len(self.intervals)
        
#         while left < right:
#             mid = (left + right) // 2
            
#             if self.intervals[mid][1] <= startTime:
#                 left = mid + 1
#             else:
#                 right = mid
                
#         # Check if the new interval overlaps with the next interval
#         if left < len(self.intervals) and self.intervals[left][0] < endTime:
#             return False
        
#         # Insert the new interval
#         self.intervals.insert(left, (startTime, endTime))
        
#         return True

class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.overlaps = []
        
    def book(self, startTime, endTime):
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                return False
            
        temp_overlaps = []
        for s, e in self.events:
            if startTime < e and endTime > s:
                overlap_start = max(startTime, s)
                overlap_end = min(endTime, e)
                temp_overlaps.append((overlap_start, overlap_end))
                
        self.events.append((startTime, endTime))
        
        self.overlaps.extend(temp_overlaps)
        
        return True
    
    
class MyCalendar:
    def __init__(self):
        self.intervals = []
        
    def book(self, startTime, endTime):
        left, right = 0, len(self.intervals)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.intervals[mid][1] <= startTime:
                left = mid + 1
            else:
                right = mid
                
        if left < len(self.intervals) and self.intervals[left][0] < endTime:
            return False
        
        self.intervals.insert(left, (startTime, endTime))
        
        return True