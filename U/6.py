"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.
"""
from collections import deque

class HitCounter:
    def __init__(self):
        self.queue = deque()
        
        
    def hit(self, timestamp):
        """Record a hit at a given timestamp."""
        self.queue.append(timestamp)
        # print(self.queue)
        
        
    def getHits(self, timestamp):
        """Returns the number of hits in the last 5 minutes."""
        # print(self.queue[0])
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
        
        return len(self.queue)
    

counter = HitCounter()

counter.hit(1)    
counter.hit(2)    
counter.hit(3)    
print(counter.getHits(300))