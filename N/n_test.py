def kth_smallest(matrix, k):
    # Use sorting
    # temp = []
    # for i in matrix:
    #     temp.extend(i)
    
    # temp.sort()
    
    # return temp[k - 1]
    
    
    # Use binary search
    
    # Initialize the boundaries
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]
    
    while low < high:
        mid = (low + high) // 2
        
        # Count the number of elements less than or equal to the mid point
        count = sum(1 for i in range(n) for j in range(n) if matrix[i][j] <= mid)
        
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