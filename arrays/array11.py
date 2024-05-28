def first_non_repeating(nums):
    """
    finds the first non-repeating element in the array

    Args:
        array (int): array of integers
    
    retuns:
        first non-repeating element in the array
    """
    
    freq = {}
    
    # 1. Return the element
    # for num in nums:
    #     if num in freq:
    #         freq[num] += 1
    #     else:
    #         freq[num] = 1
    
    # for num in nums:
    #     if freq[num] == 1:
    #         return num
        
        
    # 2. Return the index
    for i, num in enumerate(nums):
        if num in freq:
            freq[num] = (freq[num][0] + 1, freq[num][1])
        else:
            freq[num] = (1, i)
    
    for num, (count, index) in freq.items():
        if count == 1:
            return index
    
    return None

        
# test
arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
print(first_non_repeating(arr)) 


