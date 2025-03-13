import heapq

def schedule_course(courses):
    courses.sort(key=lambda i: i[1])
    
    max_heap = []
    current_time = 0
    
    for duration, lastDay in courses:
        heapq.heappush(max_heap, -duration)
        current_time += duration
        
        if current_time > lastDay:
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
            
    return len(max_heap)

# Test the example case
courses = [[5,5], [4,6], [2,6]]
print(schedule_course(courses))
    
#     # time, count = 0, 0
    # for duration, last_day in courses:
    #     if time + duration <= last_day:
    #         time += duration
    #         count += 1
            
    # return count
    
# heap = [2, 4, 3, 7, 9]
# heapq.heapify(heap)

# heapq.heappush(heap, 1)
# heapq.heappush(heap, 0)
# print(heap)