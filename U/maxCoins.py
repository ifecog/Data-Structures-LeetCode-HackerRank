"""Mario drives on a two-lane freeway with coins every mile. You are given two integer arrays, lane1 and lane2, where the value at the ith index represents the number of coins he gains or loses in the ith mile in that lane.

    If Mario is in lane 1 at mile i and lane1[i] > 0, Mario gains lane1[i] coins.
    If Mario is in lane 1 at mile i and lane1[i] < 0, Mario pays a toll and loses abs(lane1[i]) coins.
    The same rules apply for lane2.

Mario can enter the freeway anywhere and exit anytime after traveling at least one mile. Mario always enters the freeway on lane 1 but can switch lanes at most 2 times.

A lane switch is when Mario goes from lane 1 to lane 2 or vice versa.

Return the maximum number of coins Mario can earn after performing at most 2 lane switches.

Note: Mario can switch lanes immediately upon entering or just before exiting the freeway."""

# dp[i][k][l] = max coins at mile i, using k switches so far, currently in lane l 
# i = mile index (0 to n - 1)
# k = number of switches used so far (0, 1, or 2)
# l = current lane (0 for lane1, 1 for lane2)

# For each dp[i][k][l], you can either:
# stay in the same lane: 
# dp[i][k][l] = dp[i - 1][k][l] + lane[l][i]

# Swith lanes if we still have switches left (k > 0)
# dp[i][k][l] = dp[i - 1][k - 1][l - 1] + lane[l][i] 

def max_coins(lane1, lane2):
    n = len(lane1)
    dp = [[[-float('inf')] * 2 for _ in range(3)] for _ in range(n)]
    
    # Base case: Starting on lane1 with 0 swtiches
    dp[0][0][0] = lane1[0]
    
    # Optonal: Start with one switch to lane2 right away
    dp[0][1][1] = lane2[0]
    
    for i in range(1, n):
        for k in range(3):
            for l in range(2):
                val = lane1[i] if l == 0 else lane2[i]
                
                # Stay on the same lane
                dp[i][k][l] = max(dp[i][k][l], dp[i - 1][k][l] + val)
                
                # Switch from the other lane, if switch is available
                if k > 0:
                    dp[i][k][l] = max(dp[i][k][l], dp[i - 1][k - 1][l - 1] + val)
                    
    result = float('-inf')
    for i in range(n):
        for k in range(3):
            for l in range(2):
                result = max(result, dp[i][k][l])
    
    return result


lane1 = [5, -10, 4, 3]
lane2 = [3, 2, -5, 10]
print(max_coins(lane1, lane2))