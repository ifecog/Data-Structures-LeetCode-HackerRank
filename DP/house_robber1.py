def rob(nums):
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Args:
        nums (array): an array of integers

    Returns:
        int: maximum amount of money that can be robbed
    """
    
    n = len(nums)
    
    if not nums:
        return 0    
    if n == 1:
        return nums[0]
    
    # Initialize 2 variables to store the maximum amount up to the last 2 houses
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, n):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

# Example usage:
nums = [1, 2, 3, 1]
print(rob(nums))