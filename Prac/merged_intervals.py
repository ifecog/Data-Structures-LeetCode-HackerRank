def merged_intervals(intervals):
    """Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Args:
        intervals (int): an array of intervals
    """
    
    # Sort intervals based on the starting point of each interval
    intervals.sort(key=lambda i: i[0])
    
    merged = []
    for interval in intervals:
        # Append the merged list with the current interval if the list is empty or the current interval does not overlap with the last merged interval.
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        
        # Merge overlapping intervals by updating the endpoint of the last merged interval
        merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
        

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merged_intervals(intervals)
print(result)


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 