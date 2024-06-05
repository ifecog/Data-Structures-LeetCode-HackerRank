"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""

from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        self.data = defaultdict()
        
    # Set method to append a new (timestamp, value) pair to list
    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))
    
    
    # Get method to find the value with the largest timestamp
    def get(self, key, timestamp):
        if key not in self.data:
            return ''
        
        values = self.data[key]
        idx = self.binary_search(values, timestamp)
        if idx == 0:
            return ''
        
        return values[idx - 1][1]
        
    
    # Helper function that performs binary search operation
    def binary_search(self, values, timestamp):
        left, right = 0, len(values)
        
        while left < right:
            mid = (left + right) // 2
            
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left