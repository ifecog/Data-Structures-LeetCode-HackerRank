def reverse_words(s):
    """_summary_

    Args:
        s (_type_): _description_
    """
    words = s.split()
    reversed_words = words[::-1]
    
    reversed_s = ''.join(reversed_words)
    
    return reversed_s

# Example usage
input_string = "I will do it."
output_string = reverse_words(input_string)
print(output_string) 
