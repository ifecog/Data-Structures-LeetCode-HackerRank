from sortedcontainers import SortedList
import heapq

def busiestServers(k, arrival, load):
    request_count = [0] * k
    # Sorted list to keep track of available servers
    available_servers = SortedList(range(k))
    # Priority queue for busy servers (end_time, server_id)
    busy_servers = []
    
    for i, start_time in enumerate(arrival):
        # Free up servers that have finished off processing
        while busy_servers and busy_servers[0][0] <= start_time:
            end_time, server_id = heapq.heappop(busy_servers)
            available_servers.add(server_id)
            
        if not available_servers:
            continue
        
        # Find the next available server
        idx = available_servers.bisect_left(i % k)
        if idx == len(available_servers):
            idx = 0
            
        server_id = available_servers[idx]
        available_servers.remove(server_id)
        
        # Assign the request
        request_count[server_id] += 1
        heapq.heappush(busy_servers, (start_time + load[i], server_id))
        
    max_request = max(request_count)
    return [i for i, count in enumerate(request_count) if count == max_request]
