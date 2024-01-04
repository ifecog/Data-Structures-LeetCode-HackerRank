def maximum_profit(prices):
    """You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot return any profit, return 0.

    Args:
        prices (int): the given array

    Returns:
        int: the maximum profit that can be realized.
    """
    
    n = len(prices)
    if n == 0:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    # iterate through the array and update the min_proce and max_profit
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
    
    return max_profit


# example test
prices_of_wears = [3, 1, 6, 4, 9, 7]
result = maximum_profit(prices_of_wears)
print('Maximum Profit:', result) 
