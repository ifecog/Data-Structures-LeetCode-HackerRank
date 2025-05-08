"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.left = [] # Max heap (store negaative value)
        self.right = [] # Min heap 
        
    def addNum(self, num):
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        
        else:
            heapq.heappush(self.right, num)
            
        # Balance the heaps
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
            
    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        return (-self.left[0] + self.right[0]) / 2
    
mf = MedianFinder()
mf.addNum(2)
mf.addNum(3)
print(mf.findMedian())  # Output: 2.5
mf.addNum(4)
print(mf.findMedian())