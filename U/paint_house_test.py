# """There are a row of n houses, each house can be  painted with one of the three colors: red, blue or green. The cost of

#  painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# dp[i][0] = costs[i][0] + min(costs[i][1], min[costs][i][2])
# base case: dp[0][j] = costs[0][j]


# For the 2nd Question
# dp[i][j] = costs[i][j] + min(costs[i - 1][x]) where x != j

# Instead of computing the minimum for every j in O(k), we track only the 2 smallest from the previous row
# So, if the current color is the same as the minumum color from the previous row, we use the second minimum

# Otherwise, we use the minimum cost

# """

# def minCostII(costs):
#     if not costs:
#         return 0
    
#     n, k = len(costs), len(costs[0])
    
#     # Base Case: 1st row remains the same
#     prev_min, prev_second_min, prev_min_index = 0, 0, -1
    
#     for i in range(n):
#         curr_min, curr_second_min, curr_min_index = float('inf'), float('inf'), -1
        
#         for j in range(k):
#             cost = costs[i][j] + (prev_second_min if j == prev_min_index else prev_min)
            
#             # Update current minimum and current second minimum
#             if cost < curr_min:
#                 curr_second_min, curr_min = curr_min, cost
#                 curr_min_index = j
#             elif cost < curr_second_min:
#                 curr_second_min = cost
                
#         # Update the previous values with the current values for the next iteration
#         prev_min, prev_second_min, prev_min_index = curr_min, curr_second_min, curr_min_index
        
#     return prev_min

# costs = [
#     [1, 5, 3],
#     [2, 9, 4]
# ]
# print(minCostII(costs))


# def minCost(costs):
#     if not costs:
#         return 0
    
#     n = len(costs)
    
#     for i in range(1, n):
#         costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
#         costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
#         costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        
#     return min(costs[n - 1])

# # Example usage 
# costs = [
#     [17, 2, 17],
#     [16, 16, 5],
#     [14, 3, 19]
# ]

# print(minCost(costs))


# MOD = (10 ** 9) + 7

# def maxBowlingPoints(nums):
#     n = len(nums)
#     nums = [1] + nums + [1]
    
#     dp = [[0] * (n + 2) for _ in range(n + 2)]
    
#     for length in range(2, n + 1, 2):
#         for i in range(1, n - length + 2):
#             j = i + length - 1
            
#             max_points = 0
            
#             for k in range(i, j):
#                 points = nums[i - 1] * nums[k] * nums[k + 1] * nums[j + 1]
                
#                 total = dp[i][k - 1] + points + dp[k + 2][j]
                
#                 max_points = max(max_points, total)
                
#             dp[i][j] = max_points
            
#     return dp[1][n]
            

# arr = [2, 3, 5, 4]
# print(maxBowlingPoints(arr))

from collections import Counter, defaultdict, deque

def rotateTheBox(boxGrid):
    if not boxGrid or not boxGrid[0]:
        return []
    
    m, n = len(boxGrid), len(boxGrid[0])
    
    rotated = [['.'] * m for _ in range(n)]
    
    for r in range(m):
        for c in range(n):
            rotated[c][m - r - 1] = boxGrid[r][c]
            
    for col in range(m):
        bottom = n - 1
        
        for row in range(n - 1, -1, -1):
            if rotated[row][col] == '*':
                bottom = row - 1
                
            elif rotated[row][col] == '#':
                rotated[row][col] = '.'
                rotated[bottom][col] = '#'
                
                bottom -= 1
                
    return rotated

boxGrid = [["#",".","*","."],
            ["#","#","*","."]]

output = rotateTheBox(boxGrid)
for row in output:
    print("".join(row))
