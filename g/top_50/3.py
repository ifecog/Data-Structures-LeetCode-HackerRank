def maxPoints(points):
    m, n = len(points), len(points[0])
    
    dp = [[0] * n for _ in range(m)]
    
    # Base Case: First Row
    for c in range(n):
        dp[0][c] = points[0][c]
        
    # Fill the DP table from row 1 to m-1
    for r in range(1, m):
        # Compute prefix maximumx
        prefix_max = [0] * n
        prefix_max[0] = dp[r - 1][0]
        for c in range(1, n):
            prefix_max[c] = max(prefix_max[c-1], dp[r-1][c] + c)
            
        # Cmompute suffix maximum
        suffix_max = [0] * n
        suffix_max[-1] = dp[r - 1][-1] - (n - 1)
        for c in range(n - 2, -1, -1):
            suffix_max[c] = max(suffix_max[c+1], dp[r-1][c] - c)
            
        for c in range(n):
            dp[r][c] = points[r][c] + max(prefix_max[c] - c, suffix_max[c] + c)
    
    return max(dp[-1])
    
# Example usage
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
print("Maximum Points:", maxPoints(points))