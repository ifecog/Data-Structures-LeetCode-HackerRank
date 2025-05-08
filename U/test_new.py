from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    length = len(beginWord)
    
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(length):
            pattern = word[:i] + '*' + word[i+1:]
            all_combo_dict[pattern].append(word)
            
    queue = deque([((beginWord, 1))])
    visited = set([beginWord])
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(length):
            pattern = current_word[:i] + '*' + current_word[i+1:]
            
            for neighbor in all_combo_dict[pattern]:
                if neighbor == endWord:
                    return level + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                    
            all_combo_dict[pattern] = []
    
    return 0
    

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
    
    



# import heapq

# def candy(ratings):
#     n = len(ratings)
#     candies = [1] * n
    
#     for i in range(1, n):
#         if ratings[i] > ratings[i - 1]:
#             candies[i] = candies[i - 1] + 1
            
#     for i in range(n - 2, -1, -1):
#         if ratings[i] > ratings[i + 1]:
#             candies[i] = max(candies[i], candies[i + 1] + 1)
            
#     return sum(candies)

# ratings = [1, 0, 2]
# print(candy(ratings))


# def furthestBuilding(heights, bricks, ladders):
#     n = len(heights)
#     height_diff = []
    
#     for i in range(n - 1):
#         diff = heights[i + 1] - heights[i]
        
#         if diff > 0:
#             heapq.heappush(height_diff, diff)
            
#         if len(height_diff) > ladders:
#             bricks -= heapq.heappop(height_diff)
            
#         if bricks < 0:
#             return i
        
#     return n - 1

# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
# print(furthestBuilding(heights, bricks, ladders))

# def findMeetingBuilding(heights, queries):
#     n, q = len(heights), len(queries)
    
#     ans = [-1] * q
#     deferred = [[] for _ in range(n)]
#     qp = []
    
#     for i in range(q):
#         a, b = queries[i]
        
#         if a > b:
#             a, b = b, a
            
#         if a == b or heights[a] < heights[b]:
#             ans[i] = b
#         else:
#             deferred[b].append((heights[a], i))
            
#     for i in range(n):
#         for query in deferred[i]:
#             heapq.heappush(qp, query)
            
#         while qp and qp[0][0] < heights[i]:
#             ans[qp[0][1]] = i
            
#             heapq.heappop(qp)
            
#     return ans

# heights = [6,4,8,5,2,7]
# queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]

# print(findMeetingBuilding(heights, queries))


# def canSeePersonsCount(heights):
#     n = len(heights)
#     result = [0] * n

#     stack = []
    
#     for i in range(n - 1, -1, -1):
#         count = 0
        
#         while stack and stack[-1] < heights[i]:
#             stack.pop()
#             count += 1
            
#         if stack:
#             count += 1
            
#         result[i] = count
        
#         stack.append(heights[i])
    
#     return result


# # Example usage
# heights = [10, 6, 8, 5, 11, 9]
# print(canSeePersonsCount(heights))