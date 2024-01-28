def min_subarray_length(nums, target):
    """Given an array of positive interger nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Args:
        nums (int): An array of positive integers
        target (int): target
    """
    
    # initialize variables
    min_length = len(nums) + 1
    current_sum = 0
    left = 0
    
    # iterate through the array using thr sliding window approach
    for right, num in enumerate(nums):
        # add the surrent element to the sum
        current_sum += num
        
        # check if the current sum is greater than or equal to the target
        while current_sum >= target:
            # update the minimum length
            min_length = min(min_length, right - left + 1)
            
            # remove the leftmost element from the sum and move the left pointer
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length <= len(nums) else 0


# Example usage
nums = [2, 3, 1, 2, 4, 3]
target = 7
result = min_subarray_length(nums, target)
print(result) 
