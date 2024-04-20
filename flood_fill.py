def flood_fill(image, sr, sc, color):
    """An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

    Return the modified image after performing the flood fill.

    Args:
        image (array): an m x n integer grid
        sr (int): starting pixel row
        sc (int): starting pixel column
        color (int): replaced color
    """
    
    # Get the original color of the starting image
    original_color = image[sr][sc]
    
    # If the original color is the same as the color to be changed to, return original image grid
    if original_color == color:
        return image
    
    # Define a DFS function to fill connected pixels
    def dfs(r, c):
        # Check if the current pixel is within the image bounds
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
            return
        
        # Check if the color of the current pixel is te same as the original color and replace with the new color
        if image[r][c] == original_color:
            image[r][c] = color
            
            # Recurcively explore the 4 neighboring pixels
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