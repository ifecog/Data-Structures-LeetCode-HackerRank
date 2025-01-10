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
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(n - 1))
    
    # DP table: transactions (rows), days (Columns)
    dp = [[0] * n for _ in range(k + 1)]
    
    