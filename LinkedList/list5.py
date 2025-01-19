import math

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


def insert_greatest_common_divisors(head):
    """
    Given the head of a linked list head, in which each node contains an integer value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

    Return the linked list after insertion.

    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

    Args:
        head (_type_): _description_
    """
    
    if not head or not head.next:
        return head
    
    curr = head
    while curr and curr.next:
        next_node = curr.next
        gcd_val = math.gcd(curr.val, next_node.val)
        
        # Create new GCD node and insert it
        gcd_node = ListNode(gcd_val, next_node)
        curr.next = gcd_node
        
        curr = next_node
    
    return head

head = create_linked_list([18, 6, 12, 9])
new_head = insert_greatest_common_divisors(head)
print_linked_list(new_head)