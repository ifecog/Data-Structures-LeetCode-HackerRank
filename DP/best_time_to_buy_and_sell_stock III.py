def max_profit(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Args:
        prices (int): the given array

    Returns:
        int: the maximum profit that can be realized.
    """
    
    if not prices:
        return 0
    
    buy1, sell1 = float('-inf'), 0
    buy2, sell2 = float('-inf'), 0
    
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    
    return sell2


# Example usage
prices = [3,3,5,0,0,3,1,4]
print(max_profit(prices))
