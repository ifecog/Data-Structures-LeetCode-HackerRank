"""You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums."""

# REarranging: nums[i] - i != nums[j] - j
 
from collections import defaultdict

def countBadPairs(nums):
    n = len(nums)
    total_pairs = n * (n - 1) // 2
    freq = defaultdict(int)
    
    for i, num in enumerate(nums):
        key = num - i
        freq[key] += 1
        
    good_pairs = 0
    for count in freq.values():
        good_pairs += count * (count - 1) // 2
        
    print(freq)
    
    return total_pairs - good_pairs
     
# Example usage
nums = [4,1,3,3]
print(countBadPairs(nums))