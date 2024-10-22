def minimum_time(time, totalTrips):
    """You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

    Args:
        time (array<int>): an array of integers representing time
        total_trips (int): least total trips completed
    """
    
    # Initiate the left pointer to 1 unit which is the min possible time
    left = 1
    # Set the right pointer to the min time multiplied by the total Trips. This is the worst case scenario where the fastest bus completes all trips
    right = min(time) * totalTrips
    
    # Function to determine the possiblity of completing the erquired number of trips within a max time.
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
            
        return total_trips >= totalTrips
    
    # Binary search
    while left < right:
        mid = (left + right) // 2
        
        if can_complete_trips(mid):
            # If true, search the lower half
            right = mid
        else:
            left = mid + 1
    
    # When the left pointer meets the right pointer, we have found the minumum time
    return left

    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
