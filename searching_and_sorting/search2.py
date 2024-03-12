def kth_smallest(matrix, k):
    """Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix. Note: it is the kth smallest element in the sorted order, not the kth distinct element. You must find a solution with a memory complexity better than O(n2)

    Args:
        matrix (int): a sorted n * n matrix
        k (int): kth smallest value
    """
    
    # tmp = []
    # for l in matrix:
    #     tmp.extend(l)
    # tmp.sort()
    
    # return tmp[k-1]
    
    low, high = matrix[0][0], matrix[-1][-1]
    
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
    
    # binary search
    while low < high:
        mid = (low + high) // 2
        
        count = count_less_equal(matrix, mid)
        if count < k:
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