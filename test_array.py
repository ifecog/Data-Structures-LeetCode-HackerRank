# # 10. 
# def sorted_squares(nums):
#     nums_square = [i * i for i in nums]
#     nums_square.sort()
    
#     return nums_square    
    

# # Example usage:
# nums = [-4, -1, 0, 3, 10]
# result = sorted_squares(nums)
# print(result)

# 9(a). Merge Sorted Array (different lengths)
def merge_arrays(nums1, m, nums2, n):
    # Ensure that nums1 has the capacity to hold all elements in the combination of both arrays
    nums1 += [0] * n
    
    # Initialize pointers
    p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1
        
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
    
# Example usage:
nums1 = [1, 2, 3, 5, 7, 8]
m = 6
nums2 = [2, 5, 6]
n = 3

merge_arrays(nums1, m, nums2, n)
print(nums1)


# 9(a). Merge Sorted Array (same length)
def merge_arrays(nums1, m, nums2, n):
    # Initialize pointers
    p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1
        
    # If there are remaining elements in nums2, copy to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_arrays(nums1, m, nums2, n)
print(nums1)


# 8. Minimum Size Subarray Sum
def min_subarray_length(nums, target):
    min_length = len(nums) + 1
    current_sum = 0
    left = 0
    
    # Iterate through the array using the sliding windo approach
    for right, num in enumerate(nums):
        # Add current element 'num' to current_sum
        current_sum += num
        
        while current_sum >= target:
            # Update min_length
            min_length = min(min_length, right - left + 1)
            
            # Remove the meftmost element and move the left pointer to the right
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length <= len(nums) else 0
        

# Example usage
nums = [2, 3, 1, 2, 4, 3]
target = 7
result = min_subarray_length(nums, target)
print(result) 


# 7. Two Sum
def two_sum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[num] = i
    
    return []

# Example usage:
nums = [2, 4, 6, 7, 1]
target = 9
result = two_sum(nums, target)
print(result)


# # 6.
# def rotate_array(nums, k):
#     # first, ensure that k is less than the length of nums
#     k = k % len(nums)
    
#     # 1. array alicing
#     # nums[:] = nums[-k:] + nums[:-k]
    
#     # 2. use reverse method
#     nums.reverse()
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
    
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
#     # find the decreasing element
#     i = len(nums) - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1
        
#     # find the smallest element to the right that is greater than nums[i]
#     if i >= 0:
#         j = len(nums) - 1
#         while j >= 0 and nums[j] < nums[i]:
#             j -= 1
        
#         nums[i], nums[j] = nums[j], nums[i] 
        
#     # reverse the right subarray
#     # initialize left and right pointers from i
#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1


# # example test
# num_perm = [1, 2, 3, 4]
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
#     zero_index = 0
    
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[zero_index], nums[i] = nums[i], nums[zero_index]
            
#             zero_index += 1
            
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