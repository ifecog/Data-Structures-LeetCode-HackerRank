class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


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
    

# Create the linked list
list = ListNode()
list.head = ListNode(1)
list.head.next = ListNode(2)
list.head.next.next = ListNode(3)
list.head.next.next.next = ListNode(4)
list.head.next.next.next.next = ListNode(5)

# Reverse the linked list
reversed_head = reverse_list(list.head)

# Print the reversed linked list
print_linked_list(reversed_head)