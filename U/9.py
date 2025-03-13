def searchRange(nums, target):
    """
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Args:
        nums (array): An array of integers
        target (int): The target number
    """
    
    def binary_search(left=True):
        low, high = 0, len(nums) - 1
        index = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                index = mid
                
                if left:
                    high = mid - 1
                else:
                    low = mid + 1
                
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
                    
        return index
    
    start = binary_search(left=True)
    end = binary_search(left=False)
    
    return [start, end]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))