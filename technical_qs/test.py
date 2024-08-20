import json
import re

def correct_num_bedrooms(jsonData):
    listings = json.loads(jsonData)
    corrected_bedrooms = []

    for listing in listings:
        description = listing.get("description", "").lower()
        num_bedrooms = listing.get("num bedrooms")

        # Check for disqualifying phrases like "yoga studio" or "dance studio"
        if re.search(r'\b(yoga|dance|art)\s+studio\b', description):
            corrected_bedrooms.append(1 if "1-bedroom" in description else 0)
            continue

        # Correcting the number of bedrooms based on the description
        if "1-bedroom" in description and "studio" not in description:
            corrected_bedrooms.append(1)
        elif "studio" in description and "1-bedroom" not in description:
            corrected_bedrooms.append(0)
        else:
            # If the description is ambiguous or does not contain relevant keywords
            corrected_bedrooms.append(num_bedrooms)
    
    return corrected_bedrooms


jsonData = '[{"id": "1", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1}, {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1}, {"id": "3", "agent": "Jane Doe", "unit": "5", "description": "Modern 1-bedroom apartment.", "num bedrooms": 0}, {"id": "4", "agent": "John Smith", "unit": "8", "description": "Spacious dance studio space.", "num bedrooms": 0}]'

# Test the function
print(correct_num_bedrooms(jsonData))


# # Example Usage
# jsonData = '''
# [
#     {"id": "1", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1},
#     {"id": "2", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1},
#     {"id": "3", "agent": "Lisa Chen", "unit": "21", "description": "Charming 1-bedroom with modern amenities.", "num bedrooms": 0},
#     {"id": "4", "agent": "John Doe", "unit": "45", "description": "Spacious studio with open floor plan.", "num bedrooms": 0}
# ]
# '''

# print(correct_num_bedrooms(jsonData))
