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

def detect_cycle(head):
    """
    Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

    Do not modify the linked list.

    Args:
        head (int): The head of the list
    """
    if not head or not head.next:
        return None
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
        
    else:
        return None
    
    # Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow


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

# Test Case
head = create_cycle([3, 2, 0, -4], 1)
cycle_start = detect_cycle(head)
print(cycle_start.val if cycle_start else "No cycle")  # Output: 2
