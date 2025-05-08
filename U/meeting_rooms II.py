def minMeetingRooms(intervals):
    """
    Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

    Args:
        intervals (array): An array of interval pairs
    """
    
    if not intervals:
        return 0
    
    # Separate start and end times
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    
    start = end = 0
    rooms, max_rooms = 0, 0
    
    while start < len(intervals):
        if start_times[start] < end_times[end]:
            rooms += 1
            start += 1
            
        else:
            rooms -= 1
            end += 1
            
        max_rooms = max(max_rooms, rooms)

            
    return max_rooms

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))