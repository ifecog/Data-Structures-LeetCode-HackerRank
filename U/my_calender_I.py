class MyCalendar:
    def __init__(self):
        self.intervals = []
        
        
    def book(self, startTime, endTime):
        # Find the position to insert the new interval
        left, right = 0, len(self.intervals)
        
        while left < right:
            mid = (left + right) // 2
            
            if self.intervals[mid][1] <= startTime:
                left = mid + 1
            else:
                right = mid
                
        # Check if the new interval overlaps with the next interval
        if left < len(self.intervals) and self.intervals[left][0] < endTime:
            return False
        
        # Insert the new interval
        self.intervals.insert(left, (startTime, endTime))
        
        print(self.intervals)
        
        return True
    
myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # ✅ True (No conflicts)
print(myCalendar.book(15, 25))  # ❌ False (Overlap with [10,20))
print(myCalendar.book(20, 30))  # ✅ True (No conflicts)

        
        
"""You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar."""