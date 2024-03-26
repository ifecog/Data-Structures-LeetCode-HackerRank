1.
def height_checker(heights):    
    expected = sorted(heights)
    
    # solution 1
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
            
    # solution 2
    count = sum(h1 != h2 for h1, h2 in zip(heights, expected)) 
    
    return count

# Example usage:
heights = [1,1,4,2,1,3]
result = height_checker(heights)
print(result) 