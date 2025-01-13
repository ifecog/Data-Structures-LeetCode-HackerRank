# # Max Profit 4
# def max_profit(prices, k):
#     n = len(prices)
#     if not prices and k == 0:
#         return 0
    
#     if k >= n:
#         return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
    
#     dp = [[0] * n for _ in range(k + 1)]
#     for i in range(1, k + 1):
#         max_diff = -prices[0]
#         for j in range(1, n):
#             dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
#             max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    
#     return dp[k][n - 1]

# prices = [3,2,6,5,0,3]
# k = 2
# print(max_profit(prices, k))


# # Max Profit 3
# def max_profit(prices):
#     if not prices:
#         return 0
    
#     buy1, sell1 = float('-inf'), 0
#     buy2, sell2 = float('-inf'), 0
    
#     for price in prices:
#         buy1 = max(buy1, -price)
#         sell1 = max(sell1, buy1 + price)
#         buy2 = max(buy2, sell1 - price)
#         sell2 = max(sell2, buy2 + price)
        
#     return sell2

# # Example usage
# prices = [3,3,5,0,0,3,1,4]
# print(max_profit(prices))



# # Max Profit 2
# def max_profit(prices):
#     if not prices:
#         return 0
    
#     # profit = 0
    
#     # for i in range(1, len(prices)):
#     #     if prices[i] > prices[i - 1]:
#     #         profit += prices[i] - prices[i - 1]

#     # return profit
    
#     return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

# # Example usage
# prices = [7,1,5,3,6,4]
# print(max_profit(prices))


# # Max Profit 1
# def max_profit(prices):
#     if not prices:
#         return 0
    
#     min_price = prices[0]
#     max_profit = 0
    
#     for i in range(1, len(prices)):
#         min_price = min(min_price, prices[i])
#         max_profit = max(max_profit, prices[i] - min_price)
    
#     return max_profit

# # example test
# prices_of_wears = [3, 1, 6, 4, 9, 7]
# result = max_profit(prices_of_wears)
# print('Maximum Profit:', result) 


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
        
#         # Option 1: Rob the root node and its grandchildren
#         rob_root = node.val
#         if node.left:
#             rob_root += helper(node.left.left) + helper(node.left.right)
#         if node.right:
#             rob_root += helper(node.right.left) + helper(node.right.right)
        
#         # Option 2: Rob children
#         rob_children = helper(node.left) + helper(node.right)
        
#         # Get the maximum
#         dp[node] = max(rob_root, rob_children)
        
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
    
#     # Compute the maximum money in oth scenarios
#     # (1) Exclude the last house
#     # (2) Exclude the first house
#     return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# # Example usage
# nums = [2,3,2]
# print(rob(nums))
    


# # House Robber 1
# def rob(nums):
#     if not nums:
#         return 0
    
#     elif len(nums) == 1:
#         return nums[0]
#     elif len(nums) == 2:
#         return max(nums[0], nums[1])
    
#     # Initialize 2 variables to store the maximum amount up to the last 2 houses
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