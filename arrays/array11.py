def first_non_repeating(nums):
    """
    finds the first non-repeating element in the array

    Args:
        array (int): array of integers
    
    retuns:
        first non-repeating element in the array
    """
    
    # This is sloved by storing the frequency of the numbers in a dict
    freq = {}
            
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    for index, num in enumerate(nums):
        if freq[num] == 1:
            return index    # return the index 
            # return num    # return the element 
    
    return None

        
# test
arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
print(first_non_repeating(arr)) 


