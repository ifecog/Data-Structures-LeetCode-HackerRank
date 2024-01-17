# def sort_colors(nums):
#     red, white, blue = 0, 0, len(nums) - 1

#     while white <= blue:
#         if nums[white] == 0:
#             nums[red], nums[white] = nums[white], nums[red]
#             red += 1
#             white += 1
#         elif nums[white] == 1:
#             white += 1
#         else:
#             nums[white], nums[blue] = nums[blue], nums[white]
#             blue -= 1

# # Example usage:
# colors = [2, 0, 2, 1, 1, 0]
# sort_colors(colors)
# print(colors)


# def product_of_elements(nums):
#     n = len(nums)
#     left_products, right_products = [1] * n, [1] * n
    
#     # calculate the products to the left of the element
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
        
#     # calculatethe products to the right of the element
#     right_product = 1
#     for i in range(n-2, -1, -1):
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
        
#     result = [left_products[i] * right_products[i] for i in range(n)]
    
#     return result
    
    
# # test code
# array = [2, 4, 6, 8, 10]
# result = product_of_elements(array)
# print(result)


# def arrange_zero_and_nonzero_elements(nums):
#     n = len(nums)
#     zero_index = 0
    
#     for i in range(n):
#         if nums[i] != 0:
#             nums[zero_index], nums[i] = nums[i], nums[zero_index]
#             zero_index += 1
            
# # test example
# array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
# arrange_zero_and_nonzero_elements(array)
# print(array)


# def maximum_profit(prices):
#     n = len(prices)
#     if n == 0:
#         return 0
    
#     # initialize min_proce and max_profit
#     min_price = prices[0]
#     max_profit = 0
    
#     # iterate through the array of prices and update to real time factors
#     for i in range(1, n):
#         min_price = min(min_price, prices[i])
#         max_profit = max(max_profit, prices[i] - min_price)
        
#     return max_profit

# prices_of_wears = [3, 1, 6, 4, 9, 7]
# result = maximum_profit(prices_of_wears)
# print('Maximum Profit:', result) 


# def binary_search(array, n):
#     lb, ub, mid = 0, len(array) - 1, 0
#     steps = 0
    
#     while (lb <= ub):
#         print('step', steps, ':', str(list[lb:ub + 1]))
#         steps += 1
        
#         # calc mid
#         mid = (lb + ub) // 2
        
#         if n == array[mid]:
#             return mid
        
#         else:
#             if n < array[mid]:
#                 ub = mid - 1
#             else:
#                 lb = mid + 1
                
#     return -1


# # test example
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list)
# target = int(input('Insert the target element: '))
# print('Target Location:', binary_search(list, target))


# def kth_largest(matrix, k):
#     tmp = []
#     for i in matrix:
#         tmp.extend(i)
#     tmp.sort()
    
#     return tmp[-k]


# # example
# matrix = [
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# k = 8
# result = kth_largest(matrix, k)
# print(result)


# def kth_smallest(matrix, k):
#     low, high, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
#     def count_less_equal(matrix, target):
#         n, count = len(matrix), 0
#         row, col = n - 1, 0
        
#         while row >= 0 and col < n:
#             if matrix[row][col] < target:
#                 count += row + 1
#                 col += 1
#             else:
#                 row -= 1
                
#         return count
    
#     # implement binary search
#     while low < high:
#         mid = (low + high) // 2
        
#         count = count_less_equal(matrix, mid)
#         if count < k:
#             low = mid - 1
#         else:
#             high = mid
            
#     return low


# # example
# matrix = [
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# k = 8
# result = kth_smallest(matrix, k)
# print(result)


from collections import Counter


def find_anarams(s, p):
    len_s, len_p = len(s), len(p)
    result = []
    
    if len_s < len_p:
        return result
    
    # count the occurences of characters in p
    p_counter = Counter(p)
    
    # initialize the 1st window
    window_counter = Counter(s[:p])
    
    # check if theere is an anagram in the 1st window
    if p_counter == window_counter:
        result.append(0)
        
    # iterate through the rest of s
    for i in range(len_p, len_s):
        window_counter[s[i]] += 1
        
        # remove the leftmost element from the next window
        if window_counter[s[i - len_p]] == 1:
            del window_counter[s[i - len_p]]
        else:
            window_counter[s[i - len_p]] -= 1
            
        # check if consequent windows are anagrams
        if window_counter == p_counter:
            result.append(i - len_p + 1)
        
        
        
        

    