import random

class Solution:
    def __init__(self, w: list[int]):
        # Create prefix sum
        self.prefix_sums = []
        prefix_sum = 0
        
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        
        self.total_sum = prefix_sum
        
    
    def pickIndex(self) -> int:
        # Generate a random target between 1 and total sum
        target = random.randint(1, self.total_sum)
        
        # Binary search to find the index
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return left
    
    
# Example usage:
w = [1, 3]
solution = Solution(w)

# Test pickIndex multiple times
results = [solution.pickIndex() for _ in range(10)]
print("Picked indices:", results)
        