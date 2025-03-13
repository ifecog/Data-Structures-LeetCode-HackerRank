def minHeightShelves(books, shelfWidth):
    n = len(books)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        width, max_height = 0, 0
        
        # Try placing books on the current shelf
        for j in range(i - 1, -1, -1):
            width += books[j][0]
            
            if width > shelfWidth:
                break
            
            max_height = max(max_height, books[j][1])
            dp[i] = min(dp[i], dp[j] + max_height)
    
    return dp[n]
        
# Example usage
books = [[1, 3], [2, 4], [3, 2]]
shelf_width = 6
print("Minimum possible bookshelf height:", minHeightShelves(books, shelf_width))