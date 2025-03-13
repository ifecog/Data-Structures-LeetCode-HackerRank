import heapq

def mostBooked(n, meetings):
    meetings.sort()
    occupied_rooms = []
    
    available_rooms = list(range(n))
    heapq.heapify(available_rooms)
    
    room_usage = [0] * n
    
    for start, end in meetings:
        while occupied_rooms and occupied_rooms[0][0] <= start:
            _, room = heapq.heappop(occupied_rooms)
            heapq.heappush(available_rooms, room)
            
        if available_rooms:
            room = heapq.heappop(available_rooms)
        else:
            end_time, room = heapq.heappop(occupied_rooms)
            start, end = end_time, end_time + (end - start)
            
        heapq.heappush(occupied_rooms, (end, room))
        room_usage[room] += 1
        
    max_meetings = max(room_usage)
    
    return room_usage.index(max_meetings)


# Example usage:
n = 3
meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
print("Busiest Room:", mostBooked(n, meetings))
