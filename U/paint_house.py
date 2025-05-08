"""There are a row of n houses, each house can be  painted with one of the three colors: red, blue or green. The cost of

 painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers."""

# dp[i][0] = costs[i][0] + min(costs[i][1], min[costs][i][2])
# base case: dp[0][j] = costs[0][j]

def minCost(costs):
    if not costs:
        return 0
    
    n = len(costs)
    
    for i in range(1, n):
        # Update cost of painting house i with each color
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        
    return min(costs[n - 1])

# Example usage 
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]

print(minCost(costs))

