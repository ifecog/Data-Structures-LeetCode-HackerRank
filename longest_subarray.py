from collections import deque


def longest_subarray(nums, limit):
    """Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

    Args:
        nums (int): an array of integers
        limit (int): a limiting integer
    """
    # store the max and min values of the current subarray using the deque class
    max_queue = deque()
    min_queue = deque()
    
    # iniitialize the left pointer of the subarray and set initial result to 0
    left = 0
    result = 0
    
    # loop throught the array using enumerate (index, num)
    for right, num in enumerate(nums):
        while max_queue and num > max_queue[0]:
            max_queue.pop()
        max_queue.append(num)
        
        while min_queue and num < min_queue[0]:
            min_queue.pop()
        min_queue.append(num)
        
        while max_queue[0] - min_queue[0] > limit:
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            if min_queue[0] == nums[left]:
                min_queue.popleft()
            left +=1
            
        result = max(result, right - left + 1)
    
    return result
        

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)