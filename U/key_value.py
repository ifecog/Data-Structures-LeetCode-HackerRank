from collections import defaultdict
import bisect


class TimeMap:
    def __init__(self):
        self.key_to_timestamps = defaultdict(list)
        
    def set(self, key, value, timestamp):
        self.key_to_timestamps[key].append((timestamp, value))
        
    def get(self, key, timestamp):
        if key not in self.key_to_timestamps:
            return ''
        
        timestamps = self.key_to_timestamps[key]
        
        left, right = 0, len(timestamps) - 1
        result = ''
        
        while left <= right:
            mid = (left + right) // 2
            
            if timestamps[mid][0] <= timestamp:
                result = timestamps[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result


class TimeMap2:
    def __init__(self):
        self.key_to_timestamps = defaultdict(list)
        
    def set(self, key, value, timestamp):
        self.key_to_timestamps[key].append((timestamp, value))
        
    def get(self, key, timestamp):
        if key not in self.key_to_timestamps:
            return ''
        
        timestamps = self.key_to_timestamps[key]
        
        idx = bisect.bisect_right(timestamps, (timestamp, chr(127))) - 1
        if idx >= 0:
            return timestamps[idx][1]
        
        return ''
    

timeMap = TimeMap2()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # "bar"
print(timeMap.get("foo", 3))  # "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # "bar2"
print(timeMap.get("foo", 5))