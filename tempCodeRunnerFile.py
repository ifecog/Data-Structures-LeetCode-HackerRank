import json

def correct_num_bedrooms(jsonData):
    # Load json data
    listings = json.loads(jsonData)
    
    corrected_bedrooms = []
    
    for listing in listings:
        description = listing.get('description', '').lower()
        num_bedrooms = listing.get('num_bedrooms', 0)
        
        invalid_preceeding_words = ['yoga', 'dance', 'art']
        
        # Nested function to check if keyword is valid
        def is_valid_keyword(description, keyword):
            keyword_pos = description.find(keyword)
            
            while keyword_pos != -1:
                valid = True
                
                for word in invalid_preceeding_words:
                    preceeding_word = description[keyword_pos - len(word) - 1:keyword_pos].strip(' ,.;!')
                    
                    if preceeding_word == word:
                        valid = False
                        break
                
                if valid:
                    return True
                
                # Find the next occurence of the keyword
                keyword_pos = description.find(keyword, keyword_pos + 1)
            
            return False
        
        # Determine the correct number of bedrooms
        studio_present = is_valid_keyword(description, 'studio')
        one_bedroom_present = is_valid_keyword(description, '1-bedroom')
        
        if studio_present and not one_bedroom_present:
            corrected_bedrooms.append(0)
        elif one_bedroom_present and not studio_present:
            corrected_bedrooms.append(1)
        else:
            corrected_bedrooms.append(num_bedrooms)
    
    return corrected_bedrooms


jsonData = '[{"id": "1", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1}, {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1}, {"id": "3", "agent": "Jane Doe", "unit": "5", "description": "Modern 1-bedroom apartment.", "num bedrooms": 0}, {"id": "4", "agent": "John Smith", "unit": "8", "description": "Spacious dance studio space.", "num bedrooms": 0}]'

# Test the function
print(correct_num_bedrooms(jsonData))
