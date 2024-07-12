class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 4. Find the middle of a linked list
def find_middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
        
        
 

# # 3. Merge 2 sorted linked lists
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


# # 2. Chect list cycle
# def has_cycle(head):
#     slow = head
#     fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
    
#     return False


# 1. Reverse List
# def reverse_list(head):
#     # Start from the head and set pointers
#     prev = None
#     current = head
    
#     while current is not None:
#         # Store the next node temporarily
#         next_node = current.next
        
#         # Reverse the pointer direction
#         current.next = prev
        
#         # Move the prev and current one step ahead
#         prev = current
#         current = next_node
    
#     return prev

