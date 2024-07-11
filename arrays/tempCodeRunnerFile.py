    for i, num in enumerate(nums):
        if num in freq:
            freq[num] = (freq[num][0] + 1, freq[num][1])
        else:
            freq[num] = (1, i)
    
    for num, (count, index) in freq.items():
        if count == 1:
            return index
    
    return None
