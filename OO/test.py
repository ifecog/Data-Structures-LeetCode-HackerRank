# # 3. Simple Bank
# class ATM:
#     def __init__(self):
#         # Denominations: 20, 50, 100, 200, 500
#         self.denominations = [20, 50, 100, 200, 500]
#         self.banknotes = [0] * 5

#     def deposit(self, banknotesCount):
#         for i in range(5):
#             self.banknotes[i] += banknotesCount[i]

#     def withdraw(self, amount):
#         # Initialize the list to keep track of the number of banknotes to withdraw
#         withdraw_count = [0] * 5

#         # Iterate over the banknote denominations starting from the largest
#         for i in range(4, -1, -1):
#             # Check if the current denomination can be used for the amount
#             if amount >= self.denominations[i]:
#                 # Calculate the number of banknotes needed for the current denomination
#                 needed = amount // self.denominations[i]
#                 # Determine how many banknotes can actually be used (the minimum of needed and available)
#                 if needed <= self.banknotes[i]:
#                     withdraw_count[i] = needed
#                 else:
#                     withdraw_count[i] = self.banknotes[i]
#                 # Subtract the equivalent amount of money from the total amount
#                 amount -= withdraw_count[i] * self.denominations[i]

#         # Check if the entire amount has been successfully withdrawn
#         if amount == 0:
#             # Update the ATM's banknotes by subtracting the withdrawn banknotes
#             for i in range(5):
#                 self.banknotes[i] -= withdraw_count[i]
#             # Return the array of withdrawn banknotes
#             return withdraw_count
#         else:
#             # If the amount could not be fully withdrawn, return [-1]
#             return [-1]



# 2. Key Value Timestamp
# from collections import defaultdict

# class TimeMap:
    
#     def __init__(self):
#         self.data = defaultdict()
        
    
#     def set(self, key, value, timestamp):
#         return self.data[key].append((timestamp, value))
    
    
#     def get(self, key, timestamp):
#         if key not in self.data:
#             return ''
        
#         values = self.data[key]
#         idx = self.binary_search(values, timestamp)
#         if idx == 0:
#             return ''
        
#         return values[idx - 1][1]
    
    
#     def binary_search(self, values, timestamp):
#         left, right = 0, len(values)
    
#         while left < right:
#             mid = (left + right ) // 2
        
#             if values[mid][0] <= timestamp:
#                 left = mid + 1
#             else:
#                 right = mid
                
#         return left


# # Insert Delete GetRandom O(1)
# import random

# class RandomizedSet:
#     def __init__(self):
#         self.dict = {}
#         self.list = []
        
    
#     def insert(self, val: int):
#         if val in self.dict:
#             return False
        
#         self.dict[val] = len(self.list)
#         self.list.append(val)
        
#         return True
    
    
#     def remove(self, val: int):
#         if val not in self.dict:
#             return False
        
#         # Move the index to be removed to the end of the list by swapping it with the last element
#         last_element = self.list[-1]
#         idx_to_remove = self.dict[val]
#         self.list[idx_to_remove] = last_element
#         self.dict[last_element] = idx_to_remove
        
#         # Remove the element
#         self.list.pop()
#         del self.dict[val]
        
#         return True
    
    
#     def get_random(self):
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