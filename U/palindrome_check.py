def isPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
            
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  


def validPalindrome(s):
    def is_palindrome_range(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        
        left += 1
        right -= 1
        
    return True

print(validPalindrome("abca"))       # True (remove 'b' or 'c')
print(validPalindrome("racecar")) 