from collections import deque

def longest_subarray(nums, limit):
    """Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

    Args:
        nums (int): an array of integers
        limit (int): a limiting integer
    """
    
    """
    To solve this problem, here is the solution I propose the ffg steps:
    
    1. We use the double ended queue (deque) class from the Python collections library. This allow us to perform some specific element removing operations
    
    2. store the min and max values of the current subarray in using the deque class
    
    3. initialize the left pointer of the array and the initial result to 0
    
    4. Using the enumerate iteration, we can get the position and value of elements in the array (i.e. for right, num in enumerate(nums))
    
    5. update max_queue and min_queue. This is done by checking if the current element is greater than (for max_queue) or less than (for min_queue) the last element in the queues
    
    6. if the difference between the max_queue and the min_queue is greater than the limit, move the left pointer to the right and pop elements from the left for both the max_queue and the min_queue until the condition is met.
    
    7. return the result which is the maximum of the initial result and the difference between the right and left pointers.
    """
    
    max_queue = deque()
    min_queue = deque()
    
    left = 0
    result = 0
    
    for right, num in enumerate(nums):
        # Maintain the max queue in decreasing order
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        # MAintain the min queue in increasing order
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