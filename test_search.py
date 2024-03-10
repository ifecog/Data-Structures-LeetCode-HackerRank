# 3. 
def kth_largest(matrix, k):
    # # solution 1
    # tmp = []
    # for i in matrix:
    #     tmp.extend(i)
    # tmp.sort()
    
    # return tmp[-k]
    
    # solution 2
    low, high, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
    def count_greater_equal(matrix, target):
        n, count = len(matrix), 0
        row, col = 0, n - 1
        
        while col >= 0 and row < n:
            if matrix[row][col] >= target:
                count += n - row
                col -= 1
            else:
                row += 1
        
        return count
    
    while low < high:
        mid = (low + high) // 2
        count = count_greater_equal(matrix, mid)
        
        if k > count:
            high = mid
        else:
            low = mid + 1
            
    return low - 1
    

# example
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_largest(matrix, k)
print(result)



# 2.
def kth_smallest(matrix, k):
    # # solution 1
    # tmp = []
    # for i in matrix:
    #     tmp.extend(i)
    # tmp.sort()
    
    # return tmp[k - 1]
    
    # solution 2
    low, high, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
    def count_less_equal(matrix, target):
        n, count = len(matrix), 0
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
   
        return count
    
    while low < high:
        mid = (low + high) // 2
        count = count_less_equal(matrix, mid)
        
        if k > count:
            low = mid + 1
        else:
            high = mid
    
    return low
    
    

# example
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_smallest(matrix, k)
print(result)

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