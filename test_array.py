# # 10. 
# def sorted_squares(nums):
#     nums_square = [i * i for i in nums]
#     nums_square.sort()
    
#     return nums_square    
    

# # Example usage:
# nums = [-4, -1, 0, 3, 10]
# result = sorted_squares(nums)
# print(result)

# # 9.
# def merge_arrays(nums1, m, nums2, n):
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
#         p_merged -= 1
    
#     nums1[:p2 + 1] = nums2[:p2 + 1]
    
#     return nums1
        
# # Example usage:
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)


# # 8.
# def min_subarray_length(nums, target):
#     # initialize pointes and variables
#     current_sum, left = 0, 0
#     min_len = len(nums) + 1
    
#     for right, num in enumerate(nums):
#         current_sum += num
        
#         while current_sum >= target:
#             min_len = min(min_len, right - left + 1)
            
#             current_sum -= nums[left]
#             left += 1
            
#     return min_len if min_len <= len(nums) else 0

# # Example usage
# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# result = min_subarray_length(nums, target)
# print(result) 


# #  7.
# def two_sum(nums, target):
#     nums_indices = {}
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in nums_indices:
#             return [nums_indices[complement], i]
        
#         nums_indices[num] = i
    
#     return []

# # Example usage:
# nums = [2, 4, 6, 7, 1]
# target = 9
# result = two_sum(nums, target)
# print(result)


# # 6.
# def rotate_array(nums, k):
#     # ensure that k is less than the length of the array
#     k = k % len(nums)
    
#     nums[:] = nums[-k:] + nums[:-k]
    
#     # nums.reverse()
    
#     # nums[:k] = reversed(nums[:k])
#     # nums[k:] = reversed(nums[k:])
    
#     return nums

# # text examole
# nums = [-1,-100,3,99]
# k = 2
# print(rotate_array(nums, k))


# # 5 .
# def indices_sum(nums, target):
#     result = []
    
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 result.append((i, j))
    
#     return result if result else None

# array = [2, 3, 5, 7, 6, 4]
# target = 11
# print(indices_sum(array, target))


# # 4. 
# def next_permutation(nums):
#     i = len(nums) - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1
    
#     if i >= 0:
#         j  = len(nums) - 1
#         while j >= 0 and nums[j] < nums[i]:
#             j -= 1
#         nums[i], nums[j] = nums[j], nums[i]
    
#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
        
# # example test
# num_perm = [1, 2, 4, 3]
# next_permutation(num_perm)
# print('Next Permutation:', num_perm)


# # 3.
# def maximum_profit(prices):
#     if len(prices) == 0:
#         return 0

#     min_price = prices[0]
#     maximum_profit = 0
    
#     for i in range(len(prices)):
#         min_price = min(min_price, prices[i])
#         maximum_profit = max(maximum_profit, prices[i] - min_price)
    
#     return maximum_profit

# # example test
# prices_of_wears = [3, 1, 6, 4, 9, 7]
# result = maximum_profit(prices_of_wears)
# print('Maximum Profit:', result) 


# # 2.
# def arrange_zero_and_nonzero_elements(nums):
#     non_zer0_index = 0
    
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[non_zer0_index], nums[i] = nums[i], nums[non_zer0_index]
#             non_zer0_index += 1
            
# array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
# arrange_zero_and_nonzero_elements(array)
# print(array)


# # 1.
# def product_of_elements(nums):
#     n = len(nums)
#     left_products, right_products = [1] * n, [1] * n
    
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
    
#     right_product = 1
#     for i in range(n - 2, -1, -1):
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
        
#     result = [left_products[i] * right_products[i] for i in range(n)]
    
#     return result

# # test code
# array = [2, 4, 6, 8, 10]
# result = product_of_elements(array)
# print(result)