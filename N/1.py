def find_three_numbers(nums, target):
    """Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.

    Args:
        nums (array): an array of integers
        target (int): the target sum for three numbers
    """
    # This is solved using the 2 pointers approach
    # Sort the array
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                # return True
                return [nums[left], nums[i], nums[right]]
            
            else:
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return False

# Example usage
nums = [12, 3, 4, 1, 6, 9]
target = 24
print(find_three_numbers(nums, target))  # Output: True
