def kth_smallest(matrix, k):
    # This is solved using the binaru search approach
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]
    
    while low < high:
        mid = (low + high) // 2
        
        # Count the number of elements that are less than or equal to the mid point
        count = sum(1 for i in range(n) for j in range(n) if matrix[i][j] <= mid)
        
        if k > count:
            low = mid + 1
        else:
            high = mid
            
    return low