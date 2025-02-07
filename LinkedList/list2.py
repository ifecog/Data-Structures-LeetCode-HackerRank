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


def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    else:
        return False


list = ListNode()
list.head = ListNode(1)
list.head.next = ListNode(2)
list.head.next.next = ListNode(3)
list.head.next.next.next = ListNode(4)
list.head.next.next.next.next = ListNode(5)
list.head.next.next.next.next.next = ListNode(6)
           
print(middle_node(list.head).val)
print(has_cycle(list.head))