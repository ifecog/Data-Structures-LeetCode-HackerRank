def max_sum(arr):
    """Given an array arr[] of n integers, find the maximum that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.

    Args:
        arr (int): An array of integers.

    Returns:
        int: The maximum sum
    """
    
    n = len(arr)
    
    # 1. Calculate the initial sum and the total sum of the array
    s0, total_sum = 0, 0
    
    for i in range(n):
        s0 += i * arr[i]
        total_sum += arr[i]
        
    # Iniitialize maximum sum as s0
    max_sum_val = s0
    
    # 2. Use the recurrence relation to calculate sums for each rotation
    current_sum = s0
    for i in range(1, n):
        current_sum = current_sum + total_sum - (n * arr[n - 1])
                
        max_sum_val = max(max_sum_val, current_sum)
    
    return max_sum_val

# Example usage:
arr = [8, 3, 1, 2]
print(max_sum(arr))
    