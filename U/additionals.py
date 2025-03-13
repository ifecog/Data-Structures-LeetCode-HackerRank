# Consecutive Pairs
def count_consecutive_pairs(query):
    max_n = max(x[0] for x in query)
    line = [0] * (max_n + 1)
    
    same_color_pairs = 0
    result = []
    
    for idx, color in query:
        # Check the left and right neighbors
        left_same = (idx > 0 and line[idx - 1] == line[idx] and line[idx] != 0)
        right_same = (idx < max_n and line[idx + 1] == line[idx] and line[idx] != 0)
        
        # Remove the previous contributions
        if left_same:
            same_color_pairs -= 1
        if right_same:
            same_color_pairs -= 1
            
        # Update the color
        line[idx] = color
        
        # Update left_same and right_same
        left_same = (idx > 0 and line[idx - 1] == line[idx])
        right_same = (idx < max_n and line[idx + 1] == line[idx])
        
        # Add the current contributions
        if left_same:
            same_color_pairs += 1
        if right_same:
            same_color_pairs += 1
            
        result.append(same_color_pairs)
    
    return result

# Example usage
query = [[2,1],[3,1],[4,3],[5,1],[4,1]]
print(count_consecutive_pairs(query))


# # Rotate Box
# def rotateTheBox(boxGrid):
#     m, n = len(boxGrid), len(boxGrid[0])
    
#     # Rotate thr box by 90degrees to the right
#     rotated = [['.'] * m for _ in range(n)]    
#     for r in range(m):
#         for c in range(n):
#             rotated[c][m - 1 - r] = boxGrid[r][c]
            
#     # Apply Gravity
#     for col in range(m):
#         bottom = n - 1
        
#         for row in range(n - 1, -1, -1):
#             if rotated[row][col] == '*':
#                 bottom = row - 1
                
#             if rotated[row][col] == '#':
#                 rotated[row][col] = '.'
#                 rotated[bottom][col] = '#'
                
#                 bottom -= 1
                
#     return rotated
    
# boxGrid = [["#",".","*","."],
#             ["#","#","*","."]]

# output = rotateTheBox(boxGrid)
# for row in output:
#     print("".join(row))
    

# # Index of Sticks
# def collect_sticks(forest, bird):
#     n = len(forest)
    
#     nest_size = 0
#     picked_indices = []
    
#     direction = 1 # 1 for right, -1 for left
#     pos = bird
    
#     while nest_size < 100:
#         # 
#         if not (0 <= pos < n):
#             break
        
#         # Move in the current_direction
#         while 0 <= pos < n and forest[pos] == 0:
#             pos += direction
            
#         # Collect the stick
#         nest_size += forest[pos]
#         picked_indices.append(pos)
        
#         # Mark the stick ad collected
#         forest[pos] = 0

#         # Switch direction
#         direction *= -1
        
#     return picked_indices

# forest = [10, 50, 0, 100]
# bird = 2
# print(collect_sticks(forest, bird))


# # Maximum and Current Rating
# def max_and_current_rating(diff):
#     current_rating = 1500
#     max_rating = 1500
    
#     for change in diff:
#         current_rating += change
#         max_rating = max(max_rating, current_rating)
    
#     return [max_rating, current_rating]
    
# # Example Usage
# diff = [10, 50, -10, 100]
# print(max_and_current_rating(diff))


# # Easy Count Uber
# def easy_count_uber(coordinates):
#     # Initialize an emoty set to store unique markers since sets do not store duplicates
#     markers = set()
    
#     for left, right in coordinates:
#         for marker in range(left, right + 1):
#             markers.add(marker)
            
#     return len(markers)

# # Example usage:
# coordinates = [[4, 7], [-1, 5], [3, 6]]
# result = easy_count_uber(coordinates)
# print(result)