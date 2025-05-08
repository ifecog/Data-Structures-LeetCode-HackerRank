def sorted_squares(nums):
    """Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

    Args:
        nums (int): an array of integers
    """
  
    
#     nums_square = [i ** 2 for i in nums]
#     nums_square.sort()
#     return nums_square


# # Example usage:
# nums = [-4, -1, 0, 3, 10]
# result = sorted_squares(nums)
# print(result)


def sorted_squares(nums):
    n = len(nums)
    l, r = 0, n - 1
    pos = n - 1
    result = [0] * n
    
    while l <= r:
        left_square, right_square = nums[l] ** 2, nums[r] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            l += 1
        else:
            result[pos] = right_square
            r -= 1
            
        pos -= 1
        
    
    return result
            

# Example usage:
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)