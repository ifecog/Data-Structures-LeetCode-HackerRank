def top_k_frequent(nums, k):
    """Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Args:
        nums (array): an array of integers
        k (int): integer representing the most frequent elements

    Returns:
        array: an array of the k most frequent elements
    """
    
    # Initiate an empty dictionary 'count' to store the frequency of the elements
    count = {}
    
    # Iterate over the array nums and increment the count of each element in the dictionary
    for num in nums:
        count[num] = count.get(num, 0) + 1
        
    # sorted_nums = sorted(count, key=count.get, reverse=True)
    sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)
    
    return sorted_nums[:k]

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(top_k_frequent(nums, k)) 

