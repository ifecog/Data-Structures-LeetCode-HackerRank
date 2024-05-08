# 1. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def reverse_list(head):
    prev = None
    current = head
    
    while current is not None:
        # Store the next node temporarily
        next_node = current.next
        
        # Reverse the pointer direction
        current.next = prev
        
        # Move previous and current pointer one step forward
        prev = current
        current = next_node
    
    return prev