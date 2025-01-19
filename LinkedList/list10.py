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
    
    
def delete_middle(head):
    if not head or not head.next:
        return None
    
    prev = None
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = slow.next
    
    return head

# Test Case 1: Delete middle node from a list with odd length
head1 = create_linked_list([1, 2, 3, 4, 5])
new_head1 = delete_middle(head1)
print_linked_list(new_head1)