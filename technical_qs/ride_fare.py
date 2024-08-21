def adjust_ride_fare(rides):
    adjusted_rides = []
    
    for ride in rides:
        # Check if distance is less than 1 mile
        if ride['distance'] < 1:
            # Remove the surcharge from the fare
            ride['fare'] -= ride['surcharge']
            
            # Set the surcharge to 0
            ride['surcharge'] = 0
            
        adjusted_rides.append(ride)
    
    return adjusted_rides
            

# Example usage:
rides = [
    {"id": "1", "distance": 0.5, "surcharge": 5, "fare": 20},
    {"id": "2", "distance": 2.3, "surcharge": 5, "fare": 25},
    {"id": "3", "distance": 0.8, "surcharge": 5, "fare": 15}
]

adjusted_rides = adjust_ride_fare(rides)
print(adjusted_rides)