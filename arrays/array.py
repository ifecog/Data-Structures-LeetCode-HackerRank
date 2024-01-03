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
    
    min_price =prices[0]
    max_profit = 0
    
    for i in range(1, n):
        # update min_price
        min_price = min(min_price, prices[i])
        
        # update max_profit
        max_profit = max(max_profit, prices[i] - min_price)
        
    return max_profit


# Example usage:
prices = [7, 1, 5, 3, 6, 4]
result = maximum_profit(prices)

print("Maximum profit:", result)

















#     non_zero_index = 0
    
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
#             non_zero_index += 1
    
            
    
# array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
# arrange_zero_elements(array)
# print(array)
    
    
#     n = len(nums)
    
#     left_products = [1] * n
#     right_products = [1] * n
    
#     # calculate the product to the left of each element
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
        
#     # calculate the product to the right of each element
#     right_product = 1
#     for i in range(n-2, -1, -1): 
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
        
#     result = [left_products[i] * right_products[i] for i in range(n)]
    
#     return result

# array = [1, 2, 3, 4, 5]
# result = product_of_elements(array)
# print(result)