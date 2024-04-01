def permute(nums):
    """Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Args:
        nums (int): an array of integers
    """
    
    result = []
    
    # define a backtrack function
    def backtrack(start):
        if start == len(nums):
            # when start reaches the length of num, make a copy of the current pemitation
            return result.append(nums[:])
        
        for i in range(start, len(nums)):
            # swap the current element with the element in the start index
            nums[start], nums[i] = nums[i], nums[start]
            
            # recurively backtrack for the remaining elements by calling the backtrack function
            backtrack(start + 1)
            
            # swap back to the original order to explore other possibilities
            nums[start], nums[i] = nums[i], nums[start]
            
    # set the baktrack start parameter to 0 for the nums array
    backtrack(0)
    
    return result


# example test
test_nums = [1, 2, 3]
print(permute(test_nums))
