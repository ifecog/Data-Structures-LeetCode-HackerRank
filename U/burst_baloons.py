"""You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely."""

def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Step 2: Create DP table
    dp = [[0] * n for _ in range(n)]
    
    # Iterate over sub array lengnths
    for length in range(1, n - 1):
        for i in range(1, n - length): # Start index
            j = i + length - 1 # End index
            
            # Start busting ballons in the range [i, j] last
            for k in range(i, j + 1):
                coins = (nums[i - 1] * nums[k] * nums[j + 1]) + dp[i][k - 1] + dp[k + 1][j]
                
                dp[i][j] = max(dp[i][j], coins)
                
    return dp[1][n - 2]

# Example usage
nums = [3,1,5,8]
print(maxCoins(nums))
            
            
"""Bowling is a sport in which a player rolls a bowling ball towards a group of pins, the target being to knock down the pins at the end of a lane. In this challenge, the rules of the game are slightly modified. Now, there are n number of pins, n is even, and the pins are arranged in a horizontal line instead of a triangular formation. ith pin has number arr[i] on it. In each throw you have to knock down exactly two consecutive pins. Once you knock down pins at positions i and i+1, those present at i-1 and i+2 will become adjacent. And you'll get arr[i-1]*arr[i]*arr[i+1]*arr[i+2] points for knocking ith and i+1th pins down. If i-1 or i+2 goes out of bounds, assume that there is a pin with number 1 on it at that position.

Find out the maximum number of points one can get when played wisely. Since the answer can be large, return answer modulo 1e9 + 7 as output. solve this variation of the burst balloon problem"""

MOD = int(10e9) + 7

def maxBowlingPoints(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    for length in range(2, n + 1, 2):
        for i in range(1, n - length + 2):
            j = i + length - 1
            
            max_points = 0
            
            for k in range(i, j, 2):
                points = dp[i][k - 1] + (nums[i - 1] * nums[k] * nums[k + 1] * nums[j + 1]) + dp[k + 2][j]
                
                points_modulus = points % MOD
                
                max_points = max(max_points, points_modulus)
                
            dp[i][j] = max_points
                
    return dp[1][n]
                

arr = [2, 3, 5, 4]
print(maxBowlingPoints(arr))
                