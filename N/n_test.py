def kth_smallest(matrix, k):
    # temp = []
    # for i in matrix:
    #     temp.extend(i)
    
    # temp.sort()
    
    # return temp[k - 1]
    
    low, high = matrix[0][0], matrix[-1][-1]
    
    while low < high:
        mid = (low + high) // 2
        
        count = sum(1 for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] <= mid)
        
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