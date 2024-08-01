def kth_smallest(matrix, k):
    """Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix. Note: it is the kth smallest element in the sorted order, not the kth distinct element. You must find a solution with a memory complexity better than O(n2)

    Args:
        matrix (int): a sorted n * n matrix
        k (int): kth smallest value
    """
    
    # solution 1
    
    # tmp = []
    # for i in matrix:
    #     tmp.extend(i)
    # tmp.sort()
    
    # return tmp[k - 1]
    
    
    # solution 2
    

    low, high = matrix[0][0], matrix[-1][-1]
    
    # Nested function to count elements less than or equal to a given target
    def count_less_equal(array, target):
        n = len(matrix)
        row, col = n - 1, 0
        count = 0
        
        while row >= 0 and col < n:
            if array[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
    
    # Apply binary search algorithm and the count less function to locate the element
    while low < high:
        mid = (low + high) // 2
        count = count_less_equal(matrix, mid)
        
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