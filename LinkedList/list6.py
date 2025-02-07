class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()       

def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def remove_nodes(head):
    """
    You are given the head of a linked list.

    Remove every node which has a node with a greater value anywhere to the right side of it.

    Return the head of the modified linked list.

    Args:
        head (int): The head of the list

    Returns:
        _type_: _description_
    """
    
    def reverse_list(head):
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev        
            prev = current
            current = next_node    
        return prev

    head = reverse_list(head)
    
    # Traverse the reversed list and keep only nodes greater than or equal to the max_so_far
    max_so_far = float('-inf')
    dummy = ListNode(0)
    current = head
    new_tail = dummy
    
    while current:
        if current.val >= max_so_far:
            max_so_far = current.val
            new_tail.next = current
            new_tail = current
            
        current = current.next

    # End the new list
    new_tail.next = None
    
    # Reverse the list back to the oririnal order
    return reverse_list(dummy.next)


# Test Case
head = create_linked_list([3, 13, 5, 6, 7, 4, 10, 2])
new_head = remove_nodes(head)
print_linked_list(new_head)