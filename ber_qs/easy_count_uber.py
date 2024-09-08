def easy_count_uber(coordinates):
    """There is a long road with markers on it after each unit of distance. There are some ubers standing on the road. You are given the starting and ending coordinate of each uber (both inclusive).
    
    Note: At any given marker there may be multiple ubers or there may be none at all.

    Your task is to find the number of markers on which at least one uber is present. An uber with coordinates (l, r) is considered to be present on a marker m if and only if l ≤ m ≤ r.

    Args:
        coordinates (int): an array of coordinates
    """
    
    # Initialize an empty set to store unique markers since sets do not store duplicates
    markers = set()
    
    for left, right in coordinates:
        # Add each marker in the range (left, right) to the set (duplicates are automatically eliminated)
        for marker in range(left, right + 1):
            markers.add(marker)
    
    # The number of unique markers is the length of the set
    return len(markers)


# Example usage:
coordinates = [[4, 7], [-1, 5], [3, 6]]
result = easy_count_uber(coordinates)
print(result)