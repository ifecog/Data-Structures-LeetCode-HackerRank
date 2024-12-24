def sorted_squares(nums):
    """Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

    Args:
        nums (int): an array of integers
    """
    
    # nums_square = [i ** 2 for i in nums]
    
    # # sort the squared array
    # nums_square.sort()
    
    # return nums_square
    
    nums_square = [i ** 2 for i in nums]
    nums_square.sort()
    return nums_square


# Example usage:
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)