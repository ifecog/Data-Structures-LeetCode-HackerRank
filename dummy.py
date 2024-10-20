# Number of Bedrooms
import json, re

def correct_num_bedrooms(jsondata):
    listings = json.loads(jsondata)
    corrected_bedrooms = []
    
    for listing in listings:
        description = listing.get('description', '').lower()
        num_bedrooms = listing.get('num_bedrooms')
        
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




# # Camel Case Solution
# def solution(src):
#     words = src.split()
#     modified_words = []
    
#     for word in words:
#         if '_' in word:
#             parts = word.split('_')
            
#             leading = ''
#             trailing = ''
            
#             while parts[0] == '':
#                 leading += '_'
#                 parts.pop(0)
            
#             while parts[-1] == '':
#                 trailing += '_'
#                 parts.pop()
            
#             if word.istitle():
#                 camel_case = parts[0].capitalize() + ''.join(part.capitalize() for part in parts[1:])
#             else:
#                 camel_case = parts[0].lower() + ''.join(part.capitalize() for part in parts[1:])
            
#             modified_word = leading + camel_case + trailing
            
#         else:
#             modified_word = word
    
#         modified_words.append(modified_word)
    
#     return ' '.join(modified_words)

# # Example usage
# src = "This is the doc_string for __secret_fun"
# print(solution(src))

