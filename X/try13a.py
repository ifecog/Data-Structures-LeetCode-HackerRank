def topK_frequent(nums, k):
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    sorted_nums = sorted(count.keys(), key=lambda i: count[i], reverse=True)
    
    return sorted_nums[:k]


# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topK_frequent(nums, k)) 

    