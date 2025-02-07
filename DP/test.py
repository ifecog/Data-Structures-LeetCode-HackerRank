def max_profit(prices):
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
