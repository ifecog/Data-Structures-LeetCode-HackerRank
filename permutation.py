def permute(nums):
    """Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    Args:
        nums (int): an array of integers
    """
    
    """
    To solve this problem, here is my proposed solution:
    
    1. initiate an empty list 'result' to store the pernutations
    
    2. def a recursive nested function 'backtrack(start)'. This represents the backtracking algorithm. It recursively generates permutations of nums starting from the 'start' index.
    
    the best case is when start reaches the length of 'nums', indicating that all elements have been permuted.
    
    3. within the backtrack function,
    a. iterate over the indices of nums from start to the end of nums, swapping each element with the start element.
    b. recursively call backtrack(start + 1) to do the same for the remaining elements
    c. after the recursive call, swap the elements to their original positions to explore other possibilities.
    
    4. call the backtrack function (within the permute function) with start initialized to 0, inidicating that the permutation should start from the 0-indexed element
    
    5. return the resultin list of permutations
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
test_nums = [1, 2, 3]
print(permute(test_nums))
