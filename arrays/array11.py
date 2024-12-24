def first_non_repeating(nums):
    """
    finds the first non-repeating element in the array

    Args:
        array (int): array of integers
    
    retuns:
        first non-repeating element in the array
    """
    
    # This is solved by storing the frequency of the numbers in a dict
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for i, num in enumerate(nums):
        if freq[num] == 1:
            return num
    
    return -1

        
# Example usage
arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
print(first_non_repeating(arr)) 


