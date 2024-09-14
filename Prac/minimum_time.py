def minimum_time(time, totalTrips):
    """You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

    Args:
        time (array<int>): an array of integers representing time
        total_trips (int): least total trips completed
    """
    # This is solved using binary search approach
    
    # Set the left pointer to the minimum possible time which is 1 unit
    left = 1
    # Set the right pointer to the maximum possible time which is when the fastest cab does all the trips by itself
    right = min(time) * totalTrips
    
    # Helper function to determine if it is possible to complete the required number of trips within max_time
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
        
        return total_trips >= totalTrips
    
    # Implement binary search algorithm
    while left < right:
        mid = (right + left) // 2
        
        if can_complete_trips(mid):
            # If true, search the lower half
            right = mid
        else:
            # If false, search the upper half
            left = mid + 1
    
    # When left meets right, we have found the minimum time
    return left
   
    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
