def min_cost_climbing_stairs(cost):
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.

    Args:
        cost (int): Cost of climbing each step
    """
    
    n = len(cost)
    
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
    return dp[n]

cost = [10, 15, 20]
print(min_cost_climbing_stairs(cost))