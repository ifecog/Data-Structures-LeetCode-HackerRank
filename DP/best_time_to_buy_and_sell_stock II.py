def max_profit(prices):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.

    Args:
        prices (int): the given array

    Returns:
        int: the maximum profit that can be realized.
    """
    
    n = len(prices)
    # profit = 0
    
    # for i in range(1, n):
    #     if prices[i] > prices[i - 1]:
    #         profit += prices[i] - prices[i - 1]
    
    # return profit
    
    # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
    
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))


# Example usage
prices = [7,1,5,3,6,4]
print(max_profit(prices))
