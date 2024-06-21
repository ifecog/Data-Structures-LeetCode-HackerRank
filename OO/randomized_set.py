import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []
        
    
    def insert(self, val: int):
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        
        return True
    
    
    def remove(self, val: int):
        if val not in self.dict:
            return False
        
        # Move the index to be removed to the end of the list by swapping it with the last element
        last_element = self.list[-1]
        idx_to_remove = self.dict[val]
        self.list[idx_to_remove] = last_element
        self.dict[last_element] = idx_to_remove
        
        # Remove the element from the dict and list
        self.list.pop()
        del self.dict[val]
        
        return True
    
    
    def get_random(self):
        return random.choice(self.list)
    
    
# Example usage:
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # Output: True
print(randomizedSet.remove(2))  # Output: False
print(randomizedSet.insert(2))  # Output: True
print(randomizedSet.get_random())  # Output: 1 or 2
print(randomizedSet.remove(1))  # Output: True
print(randomizedSet.insert(2))  # Output: False
print(randomizedSet.get_random())  # Output: 2