def kth_largest(matrix, k):
    """Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth largest element in the matrix. Note: it is the kth largest element in the sorted order, not the kth distinct element. You must find a solution with a memory complexity better than O(n2)

    Args:
        matrix (int): a sorted n * n matrix
        k (int): kth largest value
    """
    
    # solution 1
    
    # tmp = []
    # for i in matrix:
    #     tmp.extend(i)
    # tmp.sort()
    
    # return tmp[-k]
    
    
    # solution 2
    
    # initializr pointers to the start and end of the 2-D matrix
    low, high = matrix[0][0], matrix[-1][-1]
    
    # define a function to count elements greater than or equal to a given target
    def count_greater_equal(array, target):
        n = len(array)
        row, col = 0, n - 1
        count = 0
        
        while row < n and col >= 0:
            if matrix[row][col] >= target:
                count += n - row
                col -= 1
            else:
                row += 1
        
        return count
    
    # implement binary search anf the count greater than or equal function to locate element
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
