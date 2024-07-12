class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def middle_node(head):
    """Given a non-empty, singly linked list with head node head, return a middle node of linked list. If there are two middle nodes, return the second middle node.

    Args:
        head (int): The head of the linked list
    """
    
    # This is solved by setting 2 pointers, slow and fast
    # Move 'slow' one step at a time and 'fast' 2 steps at a time.When fast reaches the end of the list, slow would be at the middle
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

