# Solve Uber Interview Questions
import heapq

"""There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue."""


# 3. Find Building Where Alice and Bob Can Meet
def findMeetingBuilding(heights, queries):
    
    n, q = len(heights), len(queries)
   
    ans = [-1] * q
   
    deferred = [[] for _ in range(n)]
   
    query_processor = []
   
    for i in range(q):
        a, b = queries[i]
       
        if a > b:
            a, b = b, a
            
        if a == b or heights[b] > heights[a]:
            ans[i] = b
        else:
            deferred[b].append((heights[a], i))
    
    for i in range(n):
        for query in deferred[i]:
            heapq.heappush(query_processor, query)
            
        while query_processor and query_processor[0][0] < heights[i]:
            ans[query_processor[0][1]] = i
            
            heapq.heappop(query_processor)       
   
    return ans

heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]

print(findMeetingBuilding(heights, queries))

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


# 1. Candy
def candy(ratings):
    n = len(ratings)
    
    candies = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
            
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)


ratings = [1, 0, 2]
print(candy(ratings)) 

