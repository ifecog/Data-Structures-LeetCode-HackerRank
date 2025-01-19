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
        
        
def is_palindrome(head):
    if not head or not head.next:
        return True
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True

# Test Case 1: Palindrome
# head1 = create_linked_list([1, 2, 2, 1])
# print(is_palindrome(head1)) 

# Test Case 2: Not a Palindrome
head2 = create_linked_list([1, 2, 3])
print(is_palindrome(head2))