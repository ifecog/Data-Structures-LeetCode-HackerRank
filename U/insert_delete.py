import random
from collections import defaultdict


# class RandomizedSet:
#     def __init__(self):
#         self.val_to_index = {}
#         self.values = []
        
#     def insert(self, val):
#         if val in self.val_to_index:
#             return False
        
#         self.values.append(val)
#         self.val_to_index[val] = len(self.values) - 1
        
#         return True
    
#     def remove(self, val):
#         if val not in self.val_to_index:
#             return False
        
#         last_val = self.values[-1]
#         idx = self.val_to_index[val]
        
#         self.values[idx] = last_val
#         self.val_to_index[last_val] = idx
        
#         self.values.pop()
#         del self.val_to_index[val]
        
#         return True
    
#     def getRandom(self) -> IndentationError:
#         return random.choice(self.values)
    
    
# randomizedSet = RandomizedSet()
# print(randomizedSet.insert(1))   # True
# print(randomizedSet.remove(2))   # False
# print(randomizedSet.insert(2))   # True
# print(randomizedSet.getRandom()) # 1 or 2
# print(randomizedSet.remove(1))   # True
# print(randomizedSet.insert(2))   # False
# print(randomizedSet.getRandom()) # 2
        
        
class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.val_to_indices = defaultdict(set)
        
    def insert(self, val):
        self.values.append(val)
        self.val_to_indices[val].add(len(self.values) - 1)
        
        return len(self.val_to_indices[val]) == 1
    
    def remove(self, val):
        if not self.val_to_indices or val not in self.val_to_indices:
            return False
        
        last_val = self.values[-1]
        idx = self.val_to_indices[val].pop()
        
        self.values[idx] = last_val
        self.val_to_indices[last_val].add(idx)
        
        self.val_to_indices[last_val].discard(len(self.values))
        self.values.pop()
        
        return True
    
    def getRandom(self):
        return random.choice(self.values)
    
randomizedCollection = RandomizedCollection()
print(randomizedCollection.insert(1))   # True
print(randomizedCollection.insert(1))   # False
print(randomizedCollection.insert(2))   # True
print(randomizedCollection.getRandom()) # 1 or 2 (with higher probability for 1)
print(randomizedCollection.remove(1))   # True
print(randomizedCollection.getRandom())
