# Uber Count
def easy_count_uber(coordinates):
    # Initialize an empty set to store unique markers since sets do not store duplicates
    markers = set()
    
    for left, right in coordinates:
        # Add each marker in the range(left, right) to the set (duplicates are automatically eliminated)
        for marker in range(left, right + 1):
            markers.add(marker)
    
    return len(markers)
    
    
# Example usage:
coordinates = [[4, 7], [-1, 5], [3, 6]]
result = easy_count_uber(coordinates)
print(result)


