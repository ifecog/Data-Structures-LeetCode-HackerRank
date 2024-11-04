# House Robber 2
def rob(nums):
    # Implement helper function to solve linear house robbing problem
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
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example usage
nums = [2,3,2]
print(rob(nums))


# # House robber 1
# def rob(nums):
#     if not nums:
#         return 0
#     elif len(nums) == 1:
#         return nums[0]
#     elif len(nums) == 2:
#         return max(nums[0], nums[1])
    
#     prev2 = nums[0]
#     prev1 = max(nums[0], nums[1])
    
#     for i in range(2, len(nums)):
#         current = max(prev1, prev2 + nums[i])
        
#         prev2 = prev1
#         prev1 = current
    
#     return prev1

# # Example usage:
# nums = [1, 2, 3, 1]
# print(rob(nums))