def max_profit(prices, k):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Args:
        prices (array): an array of prices
        k (int): highest number of transactions that can e completed
    """
    
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # If k is large enough, it is equivalent to unlimited transactions
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
    
    # DP table: transactions (rows), days (Columns)
    dp = [[0] * n for _ in range(k + 1)]
    print(dp)
    
    for i in range(1, k + 1):
        max_diff = -prices[0]
        
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
            
    return dp[k][n - 1]

prices = [3,2,6,5,0,3]
k = 2
print(max_profit(prices, k))
    