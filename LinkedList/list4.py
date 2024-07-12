class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def has_cycle(head):
    # This is solved using 2 pointers, slow and fast. move slow pointer one step at a time and move fast pointer 2 steps at a time. If there is a cycle, the fast pointer would eventually meet the slow pointer
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False