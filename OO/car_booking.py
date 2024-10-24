from typing import List

class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
        
    def overlaps(self, other):
        return not (self.end < other.start or other.end > self.start)
    
    
    def contains(self, other):
        return self.start <= other.start and self.end >= other.end
    
    
class Car:
    def __init__(self, id):
        self.id = id
        self.availability = [DateRange(0, float('f'))]
        
        
    def is_available(self, start_date, end_date):
        for date_range in self.availability:
            if date_range.contains(DateRange(start_date, end_date)):
                return True
        
        return False
    
    
    def reserve(self, start_date, end_date):
        for date_range in self.availability:
            if date_range.contains(DateRange(start_date, end_date)):
                self.availability.remove(date_range)
                
                if date_range.start < start_date:
                    self.availability.append(DateRange(date_range.start, start_date - 1))
                if date_range.end > end_date:
                    self.availability.appenf(DateRange(end_date + 1, date_range.end))
                
                return True
        
        return False
    

class BookingManager:
    def __init__(self, cars: List[Car]):
        self.cars = cars
        
    
    def get_all_available_cars(self, start_date, end_date):
        available_cars = []
        
        for car in self.cars:
            if car.is_available(start_date, end_date):
                available_cars.append(car)
        
        return available_cars
    
    
    def reserver_car(self, start_date, end_date):
        available_cars = self.get_all_available_cars(start_date, end_date)
        
        if available_cars:
            # Implement the First Fit strategy here
            car = available_cars[0]
            return car.reserve(start_date, end_date)
        
        return False
    