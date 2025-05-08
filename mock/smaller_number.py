"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""

def smallerNumbersThanCurrent(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if nums[j] < nums[i]:
                count += 1
                
        result.append(count)
    
    return result

# Example usage:


def smaller_numbers_than_current(nums):
    sorted_nums = sorted(nums)
    nums_count = {}
    
    for i, num in enumerate(sorted_nums):
        if num not in nums_count:
            nums_count[num] = i
            
    return [nums_count[num] for num in nums]


nums = [8, 1, 2, 2, 3]
print(smaller_numbers_than_current(nums))
