def nearestPalindrome(n):
    length = len(n)
    
    if n == '1':
        return '0'
    
    # Set to store all possible palinromic candidates
    candidates = set()
    
    # Edge cases: All 9s, 99s, etc., 11s, 101s, etc.
    high = '1' + '0' * (length - 1) + '1'
    low = '9' * (length - 1) if length > 1 else 0
    
    candidates.add(high) 
    candidates.add(low)
    
    # Generate palindromes based on the first half
    prefix = int(n[:(length + 1) // 2])
    
    for diff in [-1, 0, 1]:
        new_prefix = str(prefix + diff)
        
        if length % 2 == 0:
            candidate = new_prefix + new_prefix[::-1]
        else:
            candidate = new_prefix + new_prefix[-2::-1]
        
        candidates.add(candidate)
        
    candidates.discard(n)
    
    return min(candidates, key=lambda i: (abs(int(i) - int(n)), int(i)))

# Example usage:
n = "10"
output = nearestPalindrome(n)
print(output)
