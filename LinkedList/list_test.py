class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def reverse_list(head):
    prev = None
    current = head
    
    while current is not None:
        # Store the next node temporarily
        next_node = current.next
        # Reverve the pointer direction
        current.next = prev
        
        # Move the initial pointers one step forward
        prev = current
        current = next_node
    
    return prev


def print_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()
    
list = ListNode()
list.head = ListNode(1)
list.head.next = ListNode(2)
list.head.next.next = ListNode(3)
list.head.next.next.next = ListNode(4)
list.head.next.next.next.next = ListNode(5)
list.head.next.next.next.next.next = ListNode(6)
           
print_list(reverse_list(list.head)) 


def merge_lists(list1, list2):
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
            
        current = current.next
    
    current.next = list1 if list1 is not None else list2

    return dummy.next