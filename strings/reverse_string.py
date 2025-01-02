def reverse_string(s):
    """Write a function that reverses a string. the input string is given as an array of characters s. You must do this by modifying the input array-in-place with 0(1) extra memory.

    Args:
        s (string): an array of characters
    """
    
    # initialize 2 pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
        

# Example usage
test_string = ['a', 'y', 'o', 'm', 'i', 'd', 'e']
reverse_string(test_string)
print(test_string)