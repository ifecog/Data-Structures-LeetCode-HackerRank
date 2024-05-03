def length_of_longest_substring(s):
    char_index_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        


# def leftmost_column_with_one(binaryMatrix):
#     # Initiaize row and col
#     row, col = 0, len(binaryMatrix) - 1
#     leftmost_col = -1
    
#     while row < len(binaryMatrix) and col >= 0:
#         if binaryMatrix[row][col]:
#             leftmost_col = col
#             col -= 1
#         row += 1
    
#     return leftmost_col


# # Example usage:
# binaryMatrix = [
#     [0, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1],
#     [0, 0, 0, 0]
# ]

# print(leftmost_column_with_one(binaryMatrix)) 