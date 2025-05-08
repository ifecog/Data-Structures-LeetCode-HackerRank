"""You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7."""

# Rearranging:
# nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

from collections import defaultdict

MOD = 10**9 + 7

def rev(x):
    return int(str(x)[::-1])

def countNicePairs(nums):
    # Use a dictionary to count how many times each (num - rev(num)) appears
    diff_count = defaultdict(int)
    result = 0
    
    for num in nums:
        diff = num - rev(num)
        
        result += diff_count[diff]
        
        diff_count[diff] += 1
        
    return result % MOD

nums = [42,11,1,97]
# rev(42) = 24 → 42 - 24 = 18
# rev(11) = 11 → 11 - 11 = 0
# rev(1)  = 1  → 1 - 1 = 0
# rev(97) = 79 → 97 - 79 = 18
# So, diff values: [18, 0, 0, 18]
# Pairs with same diff: (0,3) and (1,2) → total = 2
print(countNicePairs(nums)) 


"""You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums."""

# nums[i] - i == nums[j] - j

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
    
    return total_pairs - good_pairs

# Example usage
nums = [4,1,3,3]
print(countBadPairs(nums))