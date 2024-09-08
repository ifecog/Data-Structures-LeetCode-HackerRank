import json, re


def correct_num_bedrooms(jsondata):
    """We want to query an API endpoint to receive data about currently available apartment listings from a rental website. Among the data fields is a column called num_bedrooms, which takes the value of 1 for a "1-bedroom" apartment and 0 for a "studio". Note: This rental agency only works with studios and 1-bedroom apartments, so there will never be 2+ bedroom listings. Each listing includes information about a "studio" or a "1-bedroom" apartment, so there will never be a listing with both a "studio" and "1-bedroom" offerings in one posting. The algorithm used occasionally mistags the num bedrooms value. Specifically, sometimes a "studio" is tagged as having num_bedrooms = 1 or a "1-bedroom" is tagged as num_bedrooms = 0. Further investigation revealed it to be an issue with one of the data fields, description, and the way our algorithm parsed the field to extract a num_bedrooms value. For example: "description": "Beautiful 1-bedroom apartment with nearby yoga studio." was detected as a yoga studio instead of 1-bedroom and incorrectly had num_bedrooms = 1. Your task is to write a function that takes in the jsonData and corrects this problem. The GET request retrieves the data as a string which looks like this: JsonData - [ "id":"3", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1 While correcting the problem remember the following edge cases: If the word "studio" or "1-bedroom" is preceded immediately by any of the words "yoga", "dance" or "art", don't consider it for num bedrooms value. If the description does not contain the word "studio" or "1-bedroom", do not change the value for num bedrooms. The rules above should be applied regardless of punctuation or letter casing within the description field. Your end goal is to return an array of integers representing num bedrooms for each rental listing example [0, 1, 1, 1, 0, 0]. Example For jsonData "[{"id": "", "agent": "Radulf Katlego", "unit": "#3, "description": "This luxurious studio apartment is in the heart of downtown.","num bedrooms": 1), {"id":" the output should be solution(jsonData) [0, 1, 1, 0].

    Args:
        jsondata (json): api endpoint response
    """
    
    listings = json.loads(jsondata)
    corrected_bedrooms = []
    
    for listing in listings:
        description = listing.get('description', '').lower()
        num_bedrooms = listing.get('num bedrooms')
        
        if re.search(r'\b(yoga|dance|art)\s+studio\b', description):
            corrected_bedrooms.append(1 if '1-bedroom' in description else 0)
            continue
        
        if '1-bedroom' in description and 'studio' not in description:
            corrected_bedrooms.append(1)
        elif 'studio' in description and '1-bedroom' not in description:
            corrected_bedrooms.append(0)
        else:
            corrected_bedrooms.append(num_bedrooms)
    
    return corrected_bedrooms

jsonData = '[{"id": "1", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1}, {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1}, {"id": "3", "agent": "Jane Doe", "unit": "5", "description": "Modern 1-bedroom apartment.", "num bedrooms": 0}, {"id": "4", "agent": "John Smith", "unit": "8", "description": "Spacious dance studio space.", "num bedrooms": 0}]'

# Test the function
print(correct_num_bedrooms(jsonData))
