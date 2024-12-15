# Maximum sum of Array
def max_sum(arr):
    n = len(arr)
    
    # 1. Calculate the initial sum and the total sum of the array
    s0, total_sum = 0, 0
    
    for i in range(n):
        s0 += i * arr[i]
        total_sum += arr[i]
        
    # Initialize the maximum sum as s0
    max_sum_val = s0
    
    # 2. Use the recurrene relation to calculate sums for each rotation
    current_sum = s0
    for i in range(1, n):
        current_sum = current_sum + total_sum - (n * arr[n - 1])
        
        max_sum_val = max(max_sum_val, current_sum)
    
    return max_sum_val

# Example usage:
arr = [8, 3, 1, 2]
print(max_sum(arr))

# # Trapping Rain Water
# def trap(height):
#     if not height:
#         return 0
    
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]
    
#     water_trapped = 0
    
#     while left < right:
#         # If left_max < right_max, move the left pointer one place to the right
#         if left_max < right_max:
#             left += 1
            
#             # Update left_max
#             left_max = max(left_max, height[left])
            
#             # Calculate trapped water at the current left position
#             water_trapped += left_max - height[left]
            
#         else:
#             # Process from the right
#             right -= 1
            
#             # Update right_max
#             right_max = max(right_max, height[right])
            
#             water_trapped += right_max - height[right]
            
#     return water_trapped

# # Example usage
# length = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(length))

   

# # Example usage
# array = [2, 4, 6, 8, 10]
# result = product_of_elements(array)
# print(result) 

# 11. First no-repeating element
# def first_non_repeating(nums):
#     freq = {}
    
#     for num in nums:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
    
#     for num in nums:
#         if freq[num] == 1:
#             return num
    
#     return None

# # Example usage
# arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
# print(first_non_repeating(arr)) 


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
# def merge_arrays(nums1, m, nums2, n):
#     # Ensure that nums1 has the capacity to hold all elements in the combination of both arrays
#     nums1 += [0] * n
    
#     # Initialize pointers
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
#         p_merged -= 1
        
#     if p2 >= 0:
#         nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
    
# # Example usage:
# nums1 = [1, 2, 3, 5, 7, 8]
# m = 6
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)


# # 9(a). Merge Sorted Array (same length)
# def merge_arrays(nums1, m, nums2, n):
#     # Initialize pointers
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
#         p_merged -= 1
        
#     # If there are remaining elements in nums2, copy to nums1
#     nums1[:p2 + 1] = nums2[:p2 + 1]
    
    
# # Example usage:
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)


# # 8. Minimum Size Subarray Sum
# def min_subarray_length(nums, target):
#     min_length = len(nums) + 1
#     current_sum = 0
#     left = 0
    
#     # Iterate through the array using the sliding windo approach
#     for right, num in enumerate(nums):
#         # Add current element 'num' to current_sum
#         current_sum += num
        
#         while current_sum >= target:
#             # Update min_length
#             min_length = min(min_length, right - left + 1)
            
#             # Remove the meftmost element and move the left pointer to the right
#             current_sum -= nums[left]
#             left += 1
    
#     return min_length if min_length <= len(nums) else 0
        

# # Example usage
# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# result = min_subarray_length(nums, target)
# print(result) 


# # 7. Two Sum
# def two_sum(nums, target):
#     hashmap = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in hashmap:
#             return [hashmap[complement], i]
        
#         hashmap[num] = i
    
#     return []

# # Example usage:
# nums = [2, 4, 6, 7, 1]
# target = 9
# result = two_sum(nums, target)
# print(result)


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