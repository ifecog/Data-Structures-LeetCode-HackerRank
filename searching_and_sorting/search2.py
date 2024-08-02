def kth_smallest(matrix, k):
    """Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix. Note: it is the kth smallest element in the sorted order, not the kth distinct element. You must find a solution with a memory complexity better than O(n2)

    Args:
        matrix (int): a sorted n * n matrix
        k (int): kth smallest value
    """
    
    # Use sorting
    # temp = []
    # for i in matrix:
    #     temp.extend(i)
    
    # temp.sort()
    
    # return temp[k - 1]
    
    
    # Use binary search approach
    
    # Set the boundaries
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


# Example usage
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_smallest(matrix, k)
print(result)