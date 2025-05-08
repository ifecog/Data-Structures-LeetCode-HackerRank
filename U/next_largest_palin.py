def nearestPalindrome(n):
    length = len(n)
    print(length)
    if n == '1':
        return '0'
    
    # Generate possible palindrome candidates
    candidates = set()
    
    # Edge cases: All 9s, 99s, 999s and 11s, 101s, 1001s, etc
    high = '1' + '0' * (length - 1) + '1'
    low = '9' * (length - 1) if length > 1 else '0'
    
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
    print(candidates)
    return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

            
# Example usage:
n = "12345"
output = nearestPalindrome(n)
print(output)
            