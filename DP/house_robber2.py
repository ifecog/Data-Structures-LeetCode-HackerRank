def rob(nums):
    """You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    Args:
        nums (array): an array of integers
    
    Returns:
        int: maximum amount of money that can be robbed
    """
    
    # Helper function to solve linear house robbing problem
    def rob_linear(houses):
        if not houses:
            return 0
        
        elif len(houses) == 1:
            return houses[0]
        elif len(houses) == 2:
            return max(houses[0], houses[1])
        
        prev2 = houses[0]
        prev1 = max(houses[0], houses[1])
        
        for i in range(2, len(houses)):
            current = max(prev1, prev2 + houses[i])
            
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    n = len(nums) 
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    # Compute the maximum money in both scenarios (1) Exclude the last house (2) Exclude the first house
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Example usage
nums = [2,3,2]
print(rob(nums))