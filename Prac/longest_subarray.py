from collections import deque

def longest_subarray(nums, limit):
    """Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

    Args:
        nums (int): an array of integers
        limit (int): a limiting integer
    """
    # This is solved using the sliding window approach
    
    # Double ended queues to store the min and max values of the current window
    max_queue = deque()
    min_queue = deque()
    
    left = 0
    result = 0
    
    for right, num in enumerate(nums):
        # Maintain the max queue in decreasing order
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        # Maintain the min queue in increasing order
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
        # If the difference between the max queue and the min queue exceeds the limit, shrink the window
        while max_queue[0] - min_queue[0] > limit:
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            if min_queue[0] == nums[left]:
                min_queue.popleft()
            left += 1
            
        result = max(result, right - left + 1)
    
    return result
        

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)