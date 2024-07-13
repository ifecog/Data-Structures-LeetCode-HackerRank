def frequency_sort(s):
    sorted_str = ''
    char_freq = {}
    
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
        
    sorted_char = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    
    for char in sorted_char:
        sorted_str += char * char_freq[char]
    
    return sorted_str

# Example usage:
s = "tree"
result = frequency_sort(s)
print(result)  


# import json

# def correct_num_bedrooms(jsonData):
#     # Load json data
#     listings = json.loads(jsonData)
    
#     corrected_bedrooms = []
    
#     for listing in listings:
#         description = listing.get('description', '').lower()
#         num_bedrooms = listing.get('num_bedrooms', 0)
        
#         invalid_preceeding_words = ['yoga', 'dance', 'art']
        
#         # Nested function to check if keyword is valid
#         def is_valid_keyword(description, keyword):
#             keyword_pos = description.find(keyword)
            
#             while keyword_pos != -1:
#                 valid = True
                
#                 for word in invalid_preceeding_words:
#                     preceeding_word = description[keyword_pos - len(word) - 1:keyword_pos].strip(' ,.;!')
                    
#                     if preceeding_word == word:
#                         valid = False
#                         break
                
#                 if valid:
#                     return True
                
#                 # Find the next occurence of the keyword
#                 keyword_pos = description.find(keyword, keyword_pos + 1)
            
#             return False
        
#         # Determine the correct number of bedrooms
#         studio_present = is_valid_keyword(description, 'studio')
#         one_bedroom_present = is_valid_keyword(description, '1-bedroom')
        
#         if studio_present and not one_bedroom_present:
#             corrected_bedrooms.append(0)
#         elif one_bedroom_present and not studio_present:
#             corrected_bedrooms.append(1)
#         else:
#             corrected_bedrooms.append(num_bedrooms)
    
#     return corrected_bedrooms


# jsonData = '[{"id": "1", "agent": "Ton Jett", "unit": "12", "description": "Beautiful 1-bedroom apartment with nearby yoga studio.", "num bedrooms": 1}, {"id": "2", "agent": "Radulf Katlego", "unit": "#3", "description": "This luxurious studio apartment is in the heart of downtown.", "num bedrooms": 1}, {"id": "3", "agent": "Jane Doe", "unit": "5", "description": "Modern 1-bedroom apartment.", "num bedrooms": 0}, {"id": "4", "agent": "John Smith", "unit": "8", "description": "Spacious dance studio space.", "num bedrooms": 0}]'

# # Test the function
# print(correct_num_bedrooms(jsonData))

# def min_available_duration(slots1, slots2, duration):
#     slots1.sort()
#     slots2.sort()
    
#     i, j = 0, 0
#     while i < len(slots1) and j < len(slots2):
#         start = max(slots1[i][0], slots2[j][0])
#         end = min(slots1[i][1], slots2[j][1])
        
#         if start - end >= duration:
#             return [start, start + duration]
        
#         if slots1[i][1] < slots2[j][1]:
#             i += 1
#         else:
#             j += 1
    
#     return []

# # Example usage:
# slots1 = [[10,50],[60,120],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 8
# print(min_available_duration(slots1, slots2, duration))


