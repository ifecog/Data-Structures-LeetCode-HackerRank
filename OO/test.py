# # 2. Randomized Set
# import random

# class RandomizedSet:
    
#     def __init__(self):
#         self.dict = {}
#         self.list = []
        
        
#     def insert(self, val: int) -> bool:
#         if val in self.dict:
#             return False
        
#         self.dict[val] = len(self.list)
#         self.list.append(val)
        
#         return True
    
    
#     def remove(self, val: int) -> bool:
#         if val not in self.dict:
#             return False
        
#         # Swap the index last element with the index of the element to be removed
#         last_element = self.list[-1]
#         idx_to_remove = self.dict[val]
        
#         self.list[idx_to_remove] = last_element
#         self.dict[last_element] = idx_to_remove
        
#         self.list.pop()
#         del self.dict[val]
        
#         return True
    
    
#     def get_random(self) -> int:
#         return random.choice(self.list) 
    

# # Example usage:
# randomizedSet = RandomizedSet()
# print(randomizedSet.insert(1))  # Output: True
# print(randomizedSet.remove(2))  # Output: False
# print(randomizedSet.insert(2))  # Output: True
# print(randomizedSet.get_random())  # Output: 1 or 2
# print(randomizedSet.remove(1))  # Output: True
# print(randomizedSet.insert(2))  # Output: False
# print(randomizedSet.get_random())  # Output: 2


# 2. Key Value Timestamp
from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        self.data = defaultdict()
        
    
    def set(self, key, value, timestamp):
        return self.data[key].append((timestamp, value))
    
    
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
            mid = (left + right ) // 2
        
            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        return left