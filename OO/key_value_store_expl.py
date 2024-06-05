"""
Example Explanation
Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Solution Explanation
We use a defaultdict of lists to store the key-value pairs. Each list represents the values for a particular key at different timestamps.
The set method appends a new (timestamp, value) pair to the list for the given key.
The get method performs a binary search on the list of values for the given key to find the value with the largest timestamp that is less than or equal to the given timestamp. If no such value is found, it returns an empty string.
The binary_search method is a helper function that performs the binary search.
"""

from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict()
        
    
    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))
        
        
    def get(self, key, timestamp):
        if key not in self.data:
            return ''
        
        values = self.data[key]
        idx = self.binary_search(values, timestamp)
        if idx == 0:
            return ''
        
        return values[idx - 1][1]
        
        
    
    def binary_search(self, values, timestamp):
        left, right = 0, len(values)
        
        while left < right:
            mid = (left + right) // 2
            
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return left