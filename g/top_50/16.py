import heapq

def mostBooked(n, meetings):
    # Sort the meetings by the start times
    meetings.sort()
    
    # Min-Heap to track (end_time, room_number) of ongoing meetings
    occupied_rooms = []
    
    # Min-Heap to track the available rooms by room number
    available_rooms = list(range(n))
    heapq.heapify(available_rooms)
    
    # Track how many times each room is used
    room_usage = [0] * n
    
    for start, end in meetings:
        # Free up rooms that have completed meetings before the current meeting starts
        while occupied_rooms and occupied_rooms[0][0] <= start:
            _, room = heapq.heappop(occupied_rooms)
            heapq.heappush(available_rooms, room)
            
        # If a room is available, assign it
        if available_rooms:
            room = heapq.heappop(available_rooms)
        else:
            # Delay the meeting until the earliest room frees up
            end_time, room = heapq.heappop(occupied_rooms)
            start, end = end_time, end_time + (end - start)
            
        # Assign the meeting to the room
        heapq.heappush(occupied_rooms, (end, room))
        room_usage[room] += 1
        
    max_meetings = max(room_usage)
    
    return room_usage.index(max_meetings)

# Example usage:
n = 3
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
print("Busiest Room:", mostBooked(n, meetings))
    