# 2. Flood Fill
def flood_fill(image, sr, sc, color):
    original_color = image[sr][sc]
    
    # If the original color is the same as the color to be changed to, return the original image grid
    if original_color == color:
        return image
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
            return
        
        # If the image of the current pixel is the same as the original color, replace it with the new color
        if image[r][c] == original_color:
            image[r][c] = color
            
            # Recurcively explore neighboring pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    
    # Start DFS from the starting pixel
    dfs(sr, sc)
    
    return image
    
     
# Example usage
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(flood_fill(image, sr, sc, color))   


# # 1. Number of Islands
# def num_islands(grid):
#     island_count = 0
    
#     def dfs(r, c):
#         if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
#             return 
        
#         grid[r][c] = '0'
        
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)
        
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 island_count += 1
                
#                 # Recursively explore neighboring cells
#                 dfs(i, j)
    
#     return island_count

# # Example usage:
# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# print(num_islands(grid))