def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            
            while current + 1 in num_set:
                current += 1
                streak += 1
            
            longest = max(longest, streak)
            
    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))


def sumOfThree(num):
    if num % 3 != 0:
        return []
    
    x = num // 3
    
    return [x - 1, x, x + 1]

print(sumOfThree(33))


def waysToBuyPencils(total, cost1, cost2):
    ways = 0
    max_pens = total // cost1
    
    for pen in range(max_pens + 1):
        remaining = total - (pen * cost1)
        max_pencils = remaining // cost2
        
        ways += (max_pencils + 1)
    
    return ways

print(waysToBuyPencils(20, 10, 5))


    
    
