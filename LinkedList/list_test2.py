import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()       
    
def create_cycle(values, pos):
    dummy = ListNode(0)
    curr = dummy
    cycle_entry = None
    for i, val in enumerate(values):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_entry = curr
    if cycle_entry:
        curr.next = cycle_entry
    return dummy.next

    



def reverse_between(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move prev to the node just before left
    for _ in range(left - 1):
        prev = prev.next
        
    # Reverse the sublist from left to right
    current = prev.next
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
        
    return dummy.next