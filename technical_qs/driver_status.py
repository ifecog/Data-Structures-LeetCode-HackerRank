def driver_availability_status(details):
    adjusted_driver_data = []
    
    for detail in details:
        if detail['current_trip_id'] == '' and detail['status'] == 'on-trip':
            detail['status'] = 'offline'
        
        adjusted_driver_data.append(detail)
    
    return adjusted_driver_data

# Example usage:
details = [
  {"id": "1", "status": "on-trip", "last_trip_completed": "2024-08-01", "current_trip_id": ""},
  {"id": "2", "status": "online", "last_trip_completed": "2024-08-01", "current_trip_id": "T234"},
  {"id": "3", "status": "on-trip", "last_trip_completed": "2024-08-01", "current_trip_id": "T567"},
  {"id": "4", "status": "on-trip", "last_trip_completed": "2024-08-01", "current_trip_id": ""}
]


adjusted_details = driver_availability_status(details)
print(adjusted_details)

            
    