"""You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally."""

import heapq

# 2. Furthest Building
def furthestBuilding(heights, bricks, ladders):
    n = len(heights)
    
    height_difference = []
    
    for i in range(n - 1):
        diff = heights[i + 1] - heights[i]
        
        if diff > 0:
            heapq.heappush(height_difference, diff)
            
        if len(height_difference) > ladders:
            bricks -= heapq.heappop(height_difference)
            
        if bricks < 0:
            return i
        
    return n - 1
    
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(furthestBuilding(heights, bricks, ladders))












import heapq

def furthestBuilding(heights, bricks, ladders):
    n = len(heights)
    
    # Use a priority queue to store the largest height difference
    min_heap = []
    
    for i in range(n - 1):
        diff = heights[i + 1] - heights[i]
        
        # Only consider jumps where we need bricks/ladders
        if diff > 0:
            heapq.heappush(min_heap, diff)
            
        # If we've exceeded the ladder count, use bricks
        if len(min_heap) > ladders:
            bricks -= heapq.heappop(min_heap)
            
        if bricks < 0:
            return i
        
    return n - 1
            

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(furthestBuilding(heights, bricks, ladders))