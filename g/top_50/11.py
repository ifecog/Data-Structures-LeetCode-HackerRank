class RLEIterator:
    def __init__(self, encoding: list[int]):
        self.encoding = encoding
        self.index = 0
        
    
    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if self.encoding[self.index] >= n:
                # Consume n elements from the current sum
                self.encoding[self.index] -= n
                
                return self.encoding[self.index + 1]
            
            else:
                # Move the next run, reducing n accordingly
                n -= self.encoding[self.index]
                self.index += 2
        
        return -1
    
# Example usage
encoding = [3, 8, 0, 9, 2, 5]
rle_iterator = RLEIterator(encoding)
print(rle_iterator.next(2))  # Exhausts 2 elements, returns 8
print(rle_iterator.next(1))  # Exhausts 1 element, returns 8
print(rle_iterator.next(1))  # Exhausts 1 element, returns 5
print(rle_iterator.next(2))  # No elements left, returns -1