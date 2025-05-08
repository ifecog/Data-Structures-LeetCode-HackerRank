import bisect

def can_place_blocks(queries):
    obstacles = [0]
    result = []
    
    for q in queries:
        if q[0] == 1:
            x = q[1]
            bisect.insort(obstacles, x)
            
        elif q[0] == 2:
            x, sz = q[1], q[2]
            can_place = False
            
            idx = bisect.bisect_right(obstacles, x)
            
            for i in range(1, idx):
                if obstacles[i] - obstacles[i - 1] >= sz:
                    can_place = True
                    break
                
            if not can_place:
                last_obstacle = obstacles[idx - 1] if idx > 0 else 0
                
                if x - last_obstacle >= sz:
                    can_place = True
                
            result.append(can_place)
            
    return result

queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
print(can_place_blocks(queries))



# # 4. 
# def max_profit(prices, k):
#     if not prices or k == 0:
#         return 0
    
#     n = len(prices)
    
#     if k >= n // 2:
#         return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
    
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

# # 3.
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


# # 2. 
# def max_profit(prices):
#     if not prices:
#         return 0
    
#     n = len(prices)
    
#     profit = 0
    
#     for i in range(1, n):
#         if prices[i] > prices[i - 1]:
#             profit += prices[i] - prices[i - 1]
            
#     return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
            
#     # Example usage
# prices = [7,1,5,3,6,4]
# print(max_profit(prices))



# # 1.
# def maximum_profit(prices):
#     n = len(prices)
#     if n == 0:
#         return 0
    
#     min_price = prices[0]
#     max_profit = 0
    
#     for i in range(1, n):
#         min_price = min(min_price, prices[i])
#         max_profit = max(max_profit, prices[i] - min_price)
        
#     return max_profit

# # Example usage
# prices_of_wears = [3, 1, 6, 4, 9, 7]
# result = maximum_profit(prices_of_wears)
# print('Maximum Profit:', result) 