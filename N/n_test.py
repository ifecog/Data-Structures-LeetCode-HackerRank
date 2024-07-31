def find_three_numbers(nums, target):
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        left, right = i, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return True
            
            else:
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return False