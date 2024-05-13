# 2. Kth smallest element in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def kth_smallest(root, k):
    stack = []
    count = 0
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        current = current.right
    
    return -1
        
# Example usage:
# Construct a binary search tree: [3,1,4,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 1
print(kth_smallest(root, k))

# # 1. Reverse Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        

# def reverse_list(head):
#     prev = None
#     current = head
    
#     while current is not None:
#         # Store the next node temporarily
#         next_node = current.next
        
#         # Reverse the pointer direction
#         current.next = prev
        
#         # Move previous and current pointer one step forward
#         prev = current
#         current = next_node
    
#     return prev