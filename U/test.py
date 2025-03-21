"""I recently appeared for Uber's Backend Engineer role's Online Assesment (OA) and faced following problems. The OA was hosted on code signal and I was given 70 minutes to solve all the 4 questions. I was able to solve 3 of them completly and in the last one I hit TLE. My assessment score came out to be 510. Here are the questions:

Question 1
Start with 1500 rating. You're given a diff array that defines the amount your rating has changed. After performing diff array changes in your initial rating return the max rating so far and your current rating. Example: Input: diff=[10,50,-10,100] Output: [1650,1650]

Question 2
You're given a forest array where 0 means empty space and +ve integer means a stick of size forest[i]. You're also give an index bird which denotes the init place of a bird in forest. Bird will always be at an empty index. The bird wants to build a nest of size 100 using the sticks in forest. In order to do so it follows the following algo:

It flies to right until it finds a stick.

Brings it back to its nest to build it.

Then turns it direction and does the step 2.

The bird keep following above until its nest of size 100 or greater is built. You need to return an array denoting the index of sticks that the bird picked to create the nest sorted in the order it picked them. Example: Input: forest=[10,50,0,100] bird=2 Output: [3]

Question 3
This was directly from the Uber tagged questions: https://leetcode.com/problems/rotating-the-box/description/

Question 4
You are given a number line of length N. You're given a 2d array query, where query[i][0] is the coordinate which this query colors with query[i][1] color. For each query, you need to tell the number consecutive pairs of same color in the number line. Initially all numbers are not colored and can be assumed to be 0. Example: Input: query=[[2,1],[3,1],[4,3],[5,1],[4,1]] Output: [0,1,1,1,3] Would really appreciate if someone can share the solution for this one or its equivalent LC."""



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            
        node.is_end = True
        
def find_words(board, words):
    m, n = len(board), len(board[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    found_words = set()
    
    trie = Trie()
    
    for word in words:
        trie.insert(word)
        
    def dfs(i, j, node, path):
        if node.is_end:
            found_words.add(path)
            node.is_end = False
            
        if not (0 <= i < m and 0 <= j < n) or board[i][j] not in node.children:
            return
            
        char = board[i][j]
        next_node = node.children[char]
        
        board[i][j] = '#'
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            dfs(ni, nj, next_node, path + char)
            
        board[i][j] = char
        
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie.root.children:
                dfs(i, j, trie.root, '')
        
    
    return list(found_words)

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))   


# def exist(board, word):
#     m, n = len(board), len(board[0])
#     directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
#     def dfs(i, j, k):
#         if k == len(word):
#             return True
        
#         if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[k]:
#             return 
        
#         temp, board[i][j] = board[i][j], ModuleNotFoundError
        
#         for di, dj in directions:
#             ni, nj = i + di, j + dj
            
#             if dfs(ni, nj, k + 1):
#                 return True
            
#         board[i][j] = temp
        
#         return False
    
#     for i in range(m):
#         for j in range(n):
#             if dfs(i, j, 0):
#                 return True
            
#     return False

# # Example usage
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# print(exist(board, word))
    


# def threeSum(nums):
#     nums.sort()
#     n = len(nums)
    
#     result = []
    
#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
        
#         left, right = i + 1, n - 1
        
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
            
#             if current_sum == 0:
#                 result.append([nums[i], nums[left], nums[right]])
                
#                 # Skip duplicates for the second number
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
                
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
                    
#                 left += 1
#                 right -= 1
                    
#             elif current_sum < 0:
#                 left += 1
#             elif current_sum > 0:
#                 right -= 1
    
#     return result

# # Example usage
# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

# def find_three_numbers(nums, target):
#     nums.sort()
#     n = len(nums)
    
#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
        
#         left, right = i + 1, n - 1
        
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
            
#             if current_sum == target:
#                 return [nums[i], nums[left], nums[right]]
            
#             elif current_sum < target:
#                 left += 1
#             elif current_sum > target:
#                 right -= 1
                
#     return []
        

# # Example usage
# nums = [12, 3, 4, 1, 6, 9]
# target = 24
# print(find_three_numbers(nums, target)) 