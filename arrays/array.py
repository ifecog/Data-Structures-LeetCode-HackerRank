def merge_arrays(nums1, m, nums2, n):
    """You are given 2 integer arrays nums1 and nums2, sorted in non-decreasing order, and 2 intergers m and n, representing the number of elements in muns1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    """
    
    p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1
        
    nums1[:p2 + 1] = nums2[:p2 + 1]
    

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_arrays(nums1, m, nums2, n)
print(nums1)


# def min_subarray_length(nums, target):
#     """Given an array of positive interger nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

#     Args:
#         nums (int): An array of positive integers
#         target (int): target
#     """
    
#     # Initialize variables
#     min_length = len(nums) + 1
#     current_sum = 0
#     left = 0
    
#     for right, num in enumerate(nums):
#         current_sum += num
        
#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
            
#             current_sum -= nums[left]
#             left += 1
    
#     return min_length if min_length < len(nums) else 0


# # Example usage
# nums = [2, 3, 1, 2, 4, 3]
# target = 9
# result = min_subarray_length(nums, target)
# print(result) 


# def next_permutation(nums):
#     """1. Given an integer of array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
    
#     2. Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in place without making a copy of the array.
    
#     3. You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot return any profit, return 0.
    
#     4. The next permutation of an array of integers is the next lexicographically greater permutation of its integer. Given an array of integer nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

#     Args:
#         nums (int): the given array

#     Returns:
#         int: the next permutation of numbers
#     """
    
#     # find the first decreasing element
#     i = len(nums) - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1
    
#     # find the smallest element to the right that is greater than nums[i]
#     if i >= 0:
#         j = len(nums) - 1
#         while j >= 0 and nums[i] >= nums[j]:
#             j -= 1
#         nums[i], nums[j] = nums[j], nums[i]
        
#     # reverse the subarray to the right of nums[i]
#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
        

# # example test
# test_array = [1, 2, 3]
# next_permutation(test_array)
# print('Next Permutation:', test_array)
    
    
# #     n = len(prices)
# #     if n == 0:
# #         return 0
    
# #     min_price =prices[0]
# #     max_profit = 0
    
# #     for i in range(1, n):
# #         # update min_price
# #         min_price = min(min_price, prices[i])
        
# #         # update max_profit
# #         max_profit = max(max_profit, prices[i] - min_price)
        
# #     return max_profit


# # # Example usage:
# # prices = [7, 1, 5, 3, 6, 4]
# # result = maximum_profit(prices)

# # print("Maximum profit:", result)


# #     non_zero_index = 0
    
# #     for i in range(len(nums)):
# #         if nums[i] != 0:
# #             nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
# #             non_zero_index += 1
    
            
    
# # array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
# # arrange_zero_elements(array)
# # print(array)
    
    
# #     n = len(nums)
    
# #     left_products = [1] * n
# #     right_products = [1] * n
    
# #     # calculate the product to the left of each element
# #     left_product = 1
# #     for i in range(1, n):
# #         left_product *= nums[i - 1]
# #         left_products[i] = left_product
        
# #     # calculate the product to the right of each element
# #     right_product = 1
# #     for i in range(n-2, -1, -1): 
# #         right_product *= nums[i + 1]
# #         right_products[i] = right_product
        
# #     result = [left_products[i] * right_products[i] for i in range(n)]
    
# #     return result

# # array = [1, 2, 3, 4, 5]
# # result = product_of_elements(array)
# # print(result)