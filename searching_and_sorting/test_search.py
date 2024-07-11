# 4. Median of 2 sorted arrays
def array_median(nums1, nums2):
    # First, the arrays are merged and then the median is found
    
    def merge_arrays(arr1, arr2):
        # Endure that arr1 has the capacity to hold all elements in the combination of both arrays. This is done by extending arr1 with 0s to match the length of the combined arrays
        arr1 += [0] * len(arr2)
        
        # Initialize pointers
        p1, p2, p_merged = len(arr1) - len(arr2) - 1, len(arr2) - 1, len(arr1) - 1
        
        while p1 >= 0 and p2 >= 0:
            if arr1[p1] >= arr2[p2]:
                arr1[p_merged] = arr1[p1]
                p1 -= 1
            else:
                arr1[p_merged] = arr2[p2]
                p2 -= 1
            p_merged -= 1
            
        # Add the remaining elements in arr2 to the merged array, arr1
        arr1[:p2 + 1] = arr2[:p2 + 1]
        
        return arr1
        
    nums = merge_arrays(nums1, nums2)
    print(nums)
    n = len(nums)
    
    # Calculate the median
    if n % 2 == 0:
        median = (nums[(n // 2) - 1] + nums[n // 2]) / 2
    else:
        median = nums[n // 2]
    
    return median


# Example usage:
nums1 = [1, 2]
nums2 = [3, 4]
result = array_median(nums1, nums2)
print(result) 


# # 3. 
# def kth_largest(matrix, k):
#     # # solution 1
#     # tmp = []
#     # for i in matrix:
#     #     tmp.extend(i)
#     # tmp.sort()
    
#     # return tmp[-k]
    
#     # solution 2
#     low, high, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
#     def count_greater_equal(matrix, target):
#         n, count = len(matrix), 0
#         row, col = 0, n - 1
        
#         while col >= 0 and row < n:
#             if matrix[row][col] >= target:
#                 count += n - row
#                 col -= 1
#             else:
#                 row += 1
        
#         return count
    
#     while low < high:
#         mid = (low + high) // 2
#         count = count_greater_equal(matrix, mid)
        
#         if k > count:
#             high = mid
#         else:
#             low = mid + 1
            
#     return low - 1
    

# # example
# matrix = [
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# k = 8
# result = kth_largest(matrix, k)
# print(result)



# # 2.
# def kth_smallest(matrix, k):
#     # solution 1
    
#     # tmp = []
#     # for i in matrix:
#     #     tmp.extend(i)
#     # tmp.sort()
    
#     # return tmp[k - 1]
    
    
#     # solution 2
    
#     # initialize low and high pointers to the start and end of the 2D-matrix
#     low, high = matrix[0][0], matrix[-1][-1]
    
#     # define a function to count elements less than of equal to a given target
#     def count_less_equal(array, target):
#         n = len(array)
#         row, col = n - 1, 0
#         count = 0
        
#         # iterate through the array to count the intended elements
#         while row >= 0 and col < n:
#             if array[row][col] <= target:
#                 count += row + 1
#                 col += 1
#             else:
#                 row -= 1
        
#         return count
    
#     # implement binary search and the count_less_equal function to locate the element
#     while low < high:
#         mid = (low + high) // 2
        
#         count = count_less_equal(matrix, mid)
        
#         if k > count:
#             low = mid + 1
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

# # 1.
# def binary_search(list, n):
#     lb, ub, mid = 0, len(list) - 1, 0
#     step = 0
    
#     while lb <= ub:
#         print('Step', step, ':', str(list[lb:ub + 1]))
#         step += 1
        
#         mid = (lb + ub) // 2
        
#         if n == list[mid]:
#             return mid
#         else:
#             if n > list[mid]:
#                 lb = mid + 1
#             else:
#                 ub = mid - 1
    
#     return -1

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(test_list)
# target = int(input('Target element? '))

# print('Target Location:', binary_search(test_list, target))