def minimum_time(time, totalTrips):
    # This is solved using the binary search approach
    left = 1
    # Set the right pointer to the minumum time multiplied by the total trips. This is the worst case scenario where the fastest bus completes all trips
    right = min(time) * totalTrips
    
    # Helper function to determine if it is possible to complete the required number of trips within a max_time
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
        
        return total_trips >= totalTrips
    
    # Implement binary search algorithm
    while left < right:
        mid = (left + right) // 2
        
        if can_complete_trips(mid):
            # If true, search the lower half
            right = mid
        else:
            # Search the upper half
            left = mid + 1
    
    # When left meets right, we have found the minimum timed
    return left
    
    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
