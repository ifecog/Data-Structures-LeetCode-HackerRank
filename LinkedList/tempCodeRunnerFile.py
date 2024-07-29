def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Create the linked list
list = ListNode()
list.head = ListNode(1)
list.head.next = ListNode(2)
list.head.next.next = ListNode(3)
list.head.next.next.next = ListNode(4)
list.head.next.next.next.next = ListNode(5)

# Reverse the linked list
reversed_head = reverse_list(list.head)

# Print the reversed linked list
print_linked_list(reversed_head)