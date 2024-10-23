from typing import List

class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
        
    def overlaps(self, other) -> bool:
        return not (self.end < other.start or other.end > self.start)
    
    
    def contains(self, other) -> bool:
        return self.start <= other.start and self.end >= other.end
    
    
class Car:
    def __init__(self, id):
        self.id = id
        self.availability = [DateRange(0, float('f'))]
        
        
    def is_available(self, start_date, end_date) -> bool:
        for date_range in self.availability:
            if date_range.contains(DateRange(start_date, end_date)):
                return True
        
        return False
    
    