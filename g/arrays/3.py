def kth_largest(nums, k):
    sorted_nums = sorted(nums)
    
    return sorted_nums[-k]

trys = [3,2,3,1,2,4,5,5,6]
print(kth_largest(trys, 4))