def checkRecord(n):
    MOD = (10 ** 9) + 7
    
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
    dp[0][0][0] = 1 # Base Case: empty record is valid
    
    for i in range(n):
        for j in range(2):
            for k in range(3):
                if dp[i][j][k] == 0:
                    continue
                
                # Add 'P'
                dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % MOD
                
                # Add 'A' only if j < 1
                if j < 1:
                    dp[i + 1][j + 1][0] = (dp[i + 1][j + 1][0] + dp[i][j][k]) % MOD
                    
                # Add 'L' only if k < 2
                if k < 2:
                    dp[i + 1][j][k + 1] = (dp[i + 1][j][k + 1] + dp[i][j][k]) % MOD
                    
    # Sum all valid states for n
    result = 0
    for j in range(2):
        for k in range(3):
            result = (result + dp[n][j][k]) % MOD
            
    return result


# Example usage
n = 2
print("Number of valid attendance records:", checkRecord(n))
                
                