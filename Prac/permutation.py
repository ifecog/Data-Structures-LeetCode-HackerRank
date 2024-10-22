def permute(nums):
    """Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Args:
        nums (int): an array of integers
    """
    
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            
            backtrack(start + 1)
            
            nums[i], nums[start] = nums[start], nums[i]
    
    backtrack(0)
    
    return result


# example test
test_nums = [1, 2, 3, 4, 5, 6]
print(permute(test_nums))
