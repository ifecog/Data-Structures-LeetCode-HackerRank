"""You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1."""









import heapq

def findMeetingBuilding(heights, queries):
    n, q = len(heights), len(queries)
    
    # Array to store answers for each query
    ans = [-1] * q
    
    # Deferred queries waiting for a taller building
    deferred = [[] for _ in range(n)]
    
    # Minimum heap to process the queries in lieue of the heights
    query_processor = []
    
    # Step1: Preprocess the query
    for i in range(q):
        a, b = queries[i]
        
        if a > b:
            a, b = b, a
            
        # If alice can already reach Bob, the result at that point is b
        if a == b or heights[a] < heights[b]:
            ans[i] = b
            
        else:
            # Defer this query and wait for a taller building
            deferred[b].append((heights[a], i))
            
    # Step2: Process buildings from left to right
    for i in range(n):
        for query in deferred[i]:
            heapq.heappush(query_processor, query)
            
        while query_processor and query_processor[0][0] < heights[i]:
            ans[query_processor[0][1]] = i
            
            heapq.heappop(query_processor)
            
    return ans



heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]

print(findMeetingBuilding(heights, queries))
