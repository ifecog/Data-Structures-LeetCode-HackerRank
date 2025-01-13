# def climb_stairs(n):
#     """
#     You are climbing a staircase. It takes n steps to reach the top.

#     Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#     Args:
#         n (int): the number of steps
#     """
    
#     if n <= 1:
#         return n
    
#     dp = [0] * (n + 1)
#     dp[0], dp[1] = 1, 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
        
#     return dp[n]

# print(climb_stairs(5))

def climb_stairs(n):
    if n <= 1:
        return n
    
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
                 
print(climb_stairs(5))