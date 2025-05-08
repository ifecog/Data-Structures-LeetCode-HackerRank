"""There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses."""

def minCostII(costs):
    if not costs:
        return 0
    
    n, k = len(costs), len(costs[0])
    
    # Base case: First row remains the same
    prev_min, prev_second_min, prev_min_index = 0, 0, -1
    
    for i in range(n):
        curr_min, curr_second_min, curr_min_index = float('inf'), float('inf'), -1
        
        for j in range(k):
            # If j was the previous min index, use the prev_second_min; otherwise use prev_min
            cost = costs[i][j] + (prev_second_min if j == prev_min_index else prev_min)
            
            # Update curr_min and curr_second_min
            if cost < curr_min:
                curr_second_min, curr_min = curr_min, cost
                curr_min_index = j
            elif cost < curr_second_min:
                curr_second_min = cost
                
        # Update previous values for the next iteration
        prev_min, prev_second_min, prev_min_index = curr_min, curr_second_min, curr_min_index
        
    return prev_min

    
# Eexample usage   
costs = [
    [1, 5, 3],
    [2, 9, 4]
]
print(minCostII(costs))