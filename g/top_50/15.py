# from sortedcontainers import SortedList
# import heapq

# def busiestServers(k, arrival, load):
#     request_count = [0] * k
#     available_servers = SortedList(range(k))
#     busy_servers = []
    
#     for i, start_time in enumerate(arrival):
#         # Free up servers that have finished off processing
#         while busy_servers and busy_servers[0][0] <= start_time:
#             end_time, server_id = heapq.heappop(busy_servers)
#             available_servers.add(server_id)
            
#         if not available_servers:
#             continue
        
#         # Find the next available server
#         idx = available_servers.bisect_left(i % k)
#         if idx == len(available_servers):
#             idx = 0
            
#         server_id = available_servers[idx]
#         available_servers.remove(server_id)
        
#         # Assign the request
#         request_count[server_id] += 1
#         heapq.heappush(busy_servers, (start_time + load[i], server_id))
        
#     max_request = max(request_count)
#     return [i for i, count in enumerate(request_count) if count == max_request]


def busiestServers(k, arrival, load):
    # Keep track of the next available time for each server
    next_available = [0] * k
    
    # Count how many requests each server has handled 
    request_count = [0] * k
    
    for i in range(len(arrival)):
        arrival_time = arrival[i]
        server = i % k
        
        for _ in range(k):
            if next_available[server] <= arrival_time:
                next_available[server] = arrival_time + load[i]
                request_count[server] += 1
                break
            
            # Move on to the next server
            server = (server + 1) % k
    
    # Get the max request        
    max_request = max(request_count)
    
    busiest = [i for i, count in enumerate(request_count) if count == max_request]
    
    return busiest


# class Server:
#     def __init__(self, id):
#         self.id = id
#         self.busy_until = 0
#         self.requests_handled = 0
        
        
# def find_busiest_servers(k, arrival, load):
#     # Initialize servers
#     servers = [Server(i) for i in range(k)]
    
#     # Process each requests
#     for i in range(len(arrival)):
#         current_time = arrival[i]
#         preferred_server = i % k
        
#         # Find available server starting from preferred server
#         assigned = False
#         checked = 0
#         server_idx = preferred_server
        
#         while checked < k:
#             if servers[server_idx].busy_until <= current_time:
#                 servers[server_idx].busy_until = current_time + load[i]
                
#                 servers[server_idx].requests_handled += 1
                
#                 assigned = True
                
#                 break
            
#             # Move to the next server
#             server_idx = (server_idx + 1) % k
#             checked += 1
            
#         # Drop request if no server is available
#         if not assigned:
#             continue
        
#     max_requests = max(server.requests_handled for server in servers)
        
#     return [server.id for server in servers if server.requests_handled == max_requests]
            
        
k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]
result = busiestServers(k, arrival, load)
print(result)