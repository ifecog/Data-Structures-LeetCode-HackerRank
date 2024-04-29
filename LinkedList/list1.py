class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """Given the head of a singly linked list, reverse the list, and return the reversed list.

    Args:
        head (_type_): _description_
    """
    
    prev = None
    current = head
    
    while current is not None:
        # Store the next node temporatily
        next_node = current.next
        
        # Reverse the pointer direction
        current.next = prev
        
        # Move previous and current pointer one step forward
        prev = current
        current = next_node
    
    return prev
    