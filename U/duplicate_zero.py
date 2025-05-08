"""Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything."""

def duplicate_zeros(arr):
    n = len(arr)
    zeros = arr.count(0)  # Count the number of zeros
    i, j = n - 1, n + zeros - 1  # Two pointers: original and expanded positions
    
    while i >= 0:
        if j < n:
            arr[j] = arr[i]  # Move element to its correct position
        
        if arr[i] == 0:  # If it's a zero, duplicate it
            j -= 1
            if j < n:
                arr[j] = 0
        
        i -= 1
        j -= 1

# Example Usage:
arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr)
print(arr)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]


def arrange_zero_and_nonzero_elements(nums):   
    n = len(nums)
    
    zero_index = 0
    
    for i in range(n):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1    
            
array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
arrange_zero_and_nonzero_elements(array)
print(array)

def min_domino_rotations(tops, bottoms):
    n = len(tops)
    
    def check(target):
        top_rotations = bottom_rotations = 0
        
        for i in range(n):
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            
            elif tops[i] != target:
                top_rotations += 1
                
            elif bottoms[i] != target:
                bottom_rotations += 1
                
        return min(top_rotations, bottom_rotations)
    
    rotations = min(check(tops[0]), check(bottoms[0]))
    
    return rotations if rotations != float('inf') else -1
    
# Example Usage:
tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(min_domino_rotations(tops, bottoms))  # Output: 2