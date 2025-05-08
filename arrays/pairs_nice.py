"""You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

    0 <= i < j < nums.length
    nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7."""

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
        
    print(diff_count)
    return result % MOD

# Example usage
nums = [42, 11, 1, 97]
print(countNicePairs(nums))
    