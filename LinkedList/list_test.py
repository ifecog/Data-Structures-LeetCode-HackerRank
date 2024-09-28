class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

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
    
    current.next = list1 if list1 else list2
    
    return dummy.next

        
# # 1. Reverse List
# def reverse_list(head):
#     prev = None
#     current = head
    
#     while current:
#         # Store the next node temporarily
#         next_node = current.next
        
#         # Revese the pointer direction
#         current.next = prev
        
#         # Move previos node and current pointer one step forward
#         prev = current
#         current = next_node
    
#     return prev


# # 2. Middle Node
# def middle_node(head):
#     slow = head
#     fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
    
#     return slow


# 3. Cyclic Property
# def has_cyclle(head):
#     slow = head
#     fast = head
    
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
    
#     return False


# def print_list(head):
#     current = head
#     while current:
#         print(current.val, end=' ')
#         current = current.next
#     print()
   
   
list = ListNode()
list.head = ListNode(1)
list.head.next = ListNode(2)
list.head.next.next = ListNode(3)
list.head.next.next.next = ListNode(4)
list.head.next.next.next.next = ListNode(5)         

# reversed_head = reverse_list(list.head)

# # Print the reversed linked list
# print_list(reversed_head)

