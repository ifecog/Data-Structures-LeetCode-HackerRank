# # House Robber 3
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        

# def rob(root):
#     # Memoization dictionary to store computed values
#     dp = {}
    
#     # Recursive helper function
#     def helper(node):
#         if not node:
#             return 0
#         if node in dp:
#             return dp[node]
        
#         # Option 1: Rob the root node, skip its children, and then rob its grandchildren
#         rob_this = node.val
#         if node.left:
#             rob_this += helper(node.left.left) + helper(node.left.right)
#         if node.right:
#             rob_this += helper(node.right.left) + helper(node.right.right)
            
#         # Option 2: Skip the root node and rob its children
#         not_rob_this = helper(node.left) + helper(node.right)
        
#         dp[node] = max(rob_this, not_rob_this)
        
#         return dp[node]

#     return helper(root)

# # Tree construction for the test
# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

# print(rob(root))


# # House Robber 2
# def rob(nums):
#     # Implement helper function to solve linear house robbing problem
#     def rob_linear(houses):
#         if not houses:
#             return 0
#         elif len(houses) == 1:
#             return houses[0]
#         elif len(houses) == 2:
#             return max(houses[0], houses[1])
        
#         prev2 = houses[0]
#         prev1 = max(houses[0], houses[1])
        
#         for i in range(2, len(houses)):
#             current = max(prev1, prev2 + houses[i])
            
#             prev2 = prev1
#             prev1 = current
        
#         return prev1
    
#     n = len(nums)
#     if n == 1:
#         return nums[0]
#     elif n == 2:
#         return max(nums[0], nums[1])
    
#     return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# # Example usage
# nums = [2,3,2]
# print(rob(nums))


# House robber 1
def rob(nums):
    if not nums:
        return 0
    
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    
    # Initialize 2 variables to store the maximum amount up to the last 2 houses
    prev2 = nums[0]


# Example usage:
nums = [1, 2, 3, 1]
print(rob(nums))