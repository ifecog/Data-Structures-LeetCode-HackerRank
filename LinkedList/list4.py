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


def reverse_between(head, left, right):
    """
    Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

    Args:
        left (int): Left pointer
        right (int): Right pinter
    """
    
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # 1. Move 'prev' to the node just before left
    for _ in range(left - 1):
        prev = prev.next
        
    # 2. Reverse the sublist from left to right
    current = prev.next    
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next
        