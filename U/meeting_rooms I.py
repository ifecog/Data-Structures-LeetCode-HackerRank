def canAttendMeetings(intervals):
    """
    Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.

    Args:
        intervals (array): an array of meeting pairs
    """
    
    intervals.sort(key=lambda i: i[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
        
    return True
            