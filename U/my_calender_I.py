"""You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar."""

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
        
        # print(self.intervals)
        
        return True
    
myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # ✅ True (No conflicts)
print(myCalendar.book(15, 25))  # ❌ False (Overlap with [10,20))
print(myCalendar.book(20, 30))  # ✅ True (No conflicts)

        
class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.overlaps = []
        
    def book(self, startTime, endTime):
        # First, check if the new event causes a triple booking
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                return False
            
        # If no triple booking, check for overlaps with existing events
        temp_overlaps = []
        for s, e in self.events:
            if startTime < e and endTime > s:
                # Add the overlapping interval
                overlap_start = max(startTime, s)
                overlap_end = min(endTime, e)
                temp_overlaps.append((overlap_start, overlap_end))
                
        # Add the new event to the calendar
        self.events.append((startTime, endTime))
        
        # Update the overlap list with new overlaps
        self.overlaps.extend(temp_overlaps)
        
        return True
    
# calendar = MyCalendarTwo()
# print(calendar.book(10, 20))  # Returns True
# print(calendar.book(50, 60))  # Returns True
# print(calendar.book(10, 40))  # Returns True (overlaps with first event but no triple booking)
# print(calendar.book(5, 15))   # Returns False (would cause triple booking with first and third events)
# print(calendar.book(5, 10))   # Returns True (no overlap with any existing event)
# print(calendar.book(25, 55))  # Returns False (would cause triple booking with second and third events)
        