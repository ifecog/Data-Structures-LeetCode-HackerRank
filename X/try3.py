from collections import deque

def longest_subarray(nums, limit):
    min_queue = deque()
    max_queue = deque()
    
    left = 0
    result = 0
    
    for right, num in enumerate(nums):
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
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