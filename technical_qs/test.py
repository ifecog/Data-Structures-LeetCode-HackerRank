import json, re


# Ride Fare Adjustment
def adjust_ride_fare(rides):
    adjusted_rides = []
    
    for ride in rides:
        if ride['distance'] < 1:
            ride['fare'] -= ride['surcharge']
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


# # Corrected Number of Bedrooms
# def correct_num_bedrooms(jsonData):
#     listings = json.loads(jsonData)
#     corrected_bedrooms = []
    
#     for listing in listings:
#         description = listing.get('description', '').lower()
#         num_bedrooms = listing.get('num bedrooms')
        
#         if re.search(r'\b(yoga|dance|art)\s+studio\b', description):
#             corrected_bedrooms.append(1 if '1-bedroom' in description else 0)
#             continue
        
#         if '1-bedroom' in description and 'studio' not in description:
#             corrected_bedrooms.append(1)
#         elif 'studio' in description and '1-bedroom' not in description:
#             corrected_bedrooms.append(0)
#         else:
#             corrected_bedrooms.append(num_bedrooms)
    
#     return corrected_bedrooms

# jsonData = '[{"id": "1", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1}, {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1}, {"id": "3", "agent": "Jane Doe", "unit": "5", "description": "Modern 1-bedroom apartment.", "num bedrooms": 0}, {"id": "4", "agent": "John Smith", "unit": "8", "description": "Spacious dance studio space.", "num bedrooms": 0}]'

# # Test the function
# print(correct_num_bedrooms(jsonData))
