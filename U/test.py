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
    


def threeSum(nums):
    nums.sort()
    n = len(nums)
    
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                    
            elif current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
    
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

def find_three_numbers(nums, target):
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            
            elif current_sum < target:
                left += 1
                
            else:
                right -= 1
                
    return []
        

# # Example usage
# nums = [12, 3, 4, 1, 6, 9]
# target = 24
# print(find_three_numbers(nums, target)) 