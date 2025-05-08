"""Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time."""

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


""""You are given an integer total indicating the amount of money you have. You are also given two integers cost1 and cost2 indicating the price of a pen and pencil respectively. You can spend part or all of your money to buy multiple quantities (or none) of each kind of writing utensil.

Return the number of distinct ways you can buy some number of pens and pencils."""

def waysToBuyPencils(total, cost1, cost2):
    ways = 0
    max_pens = total // cost1
    
    for pens in range(max_pens + 1):
        remaining = total - (pens * cost1)
        max_pencils = remaining // cost2
        
        ways += (max_pencils + 1)
    
    return ways

print(waysToBuyPencils(20, 10, 5))