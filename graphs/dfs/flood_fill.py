def flood_fill(image, sr, sc, color):
    # Get the original color of the starting image
    original_color = image[sr][sc]
    
    # If the original color is the same as the color to be changed to, return the original image grid
    if original_color == color:
        return image
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
            return
        
        # Check if the color of the current pixel is the same asthe original color and replace with the new color
        if image[r][c] == original_color:
            image[r][c] = color
            
            # Recursively explore neighboring pixels
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