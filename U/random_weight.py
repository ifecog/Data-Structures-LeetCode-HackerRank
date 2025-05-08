"""Random Pick With Weight
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w)."""

import random

class Solution:
    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0
        
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
            
        self.total_sum = prefix_sum
        
    def pickIndex(self):
        target = random.randint(1, self.total_sum)
        
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
        
        
def min_time(time, totalTrips):
    left = 1
    right = min(time) * totalTrips
    
    def canCompleteTrips(max_time):
        total_trips = 0
        
        for t in time:
            total_trips += max_time // t
            
        return total_trips >= totalTrips
    
    while left < right:
        mid = (left + right) // 2
        
        if canCompleteTrips(mid):
            right = mid
        else:
            left = mid + 1
            
    return left


def easyCountUber(coordinates):
    markers = set()
    
    for left, right in coordinates:
        for marker in range(left, right + 1):
            markers.add(marker)
            
    return len(markers)
        
coordinates=[[4, 7], [-1, 5], [3, 6]]
print(easyCountUber(coordinates))