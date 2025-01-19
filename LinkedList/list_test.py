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

import math

def insert_greatest_common_divisors(head):
    if not head or not head.next:
        return head
    
    current = head
    while current and current.next:
        next_node = current.next
        gcd_val = math.gcd(current.val, next_node.val)
        
        gcd_node = ListNode(gcd_val, next_node)
        current.next = gcd_node
        
        current = next_node
    
    return head

head = create_linked_list([18, 6, 12, 9])
new_head = insert_greatest_common_divisors(head)
print_linked_list(new_head)

# def reverse_between(head, left, right):
#     if not head or left == right:
#         return head
    
#     dummy = ListNode(0)
#     dummy.next = head
#     prev = dummy
    
#     # Move prev to the node just before left
#     for _ in range(left - 1):
#         prev = prev.next
        
#     # Reverse the sublist from left to right
#     current = prev.next
#     for _ in range(right - left):
#         next_node = current.next
#         current.next = next_node.next
#         next_node.next = prev.next
#         prev.next = next_node
    
#     return dummy.next

        
# def reverse_list(head):
#     prev = None
#     current = head
    
#     while current is not None:
#         # Store the next node temporarily
#         next_node = current.next
#         # Reverve the pointer direction
#         current.next = prev
        
#         # Move the initial pointers one step forward
#         prev = current
#         current = next_node
    
#     return prev


# list = ListNode()
# list.head = ListNode(1)
# list.head.next = ListNode(2)
# list.head.next.next = ListNode(3)
# list.head.next.next.next = ListNode(4)
# list.head.next.next.next.next = ListNode(5)
# list.head.next.next.next.next.next = ListNode(6)
           
# print_linked_list(reverse_list(list.head)) 


# def merge_lists(list1, list2):
#     dummy = ListNode()
#     current = dummy
    
#     while list1 and list2:
#         if list1.val < list2.val:
#             current.next = list1
#             list1 = list1.next
#         else:
#             current.next = list2
#             list2 = list2.next
        
#         current = current.next
    
#     current.next = list1 if list1 is not None else list2
    
#     return dummy.next

# list1 = ListNode()
# list1.head = ListNode(1)
# list1.head.next = ListNode(2)
# list1.head.next.next = ListNode(3)

# list2 = ListNode()
# list2.head = ListNode(3)
# list2.head.next = ListNode(4)
# list2.head.next.next = ListNode(5)

# print(merge_lists(list1.head, list2.head))