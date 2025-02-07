import random

class Solution:
    def __init__(self, w: list[int]):
        self.prefix_sums = []
        prefix_sum = 0
        
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        
        self.total_sum = prefix_sum
        
    
    def pickIndex(self) -> int:
        target = random.randint(1, len(self.total_sum))
        
        left, right = 0, len(self.prefix_sums) - 1
        while right < left:
            mid = (right + left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left