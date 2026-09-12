# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None
class Solution:
    #Function to remove duplicates from sorted doubly linked list.
    def removeDuplicates(self, head):
        cur = head  # Current node pointer for traversal

        while cur:
            # Check if current node is duplicate of previous node
            if cur.prev and cur.prev.data == cur.data:
                # Handle case where previous node is the head
                if cur.prev == head:
                    cur.prev = None        # Remove backward link
                    head = cur            # Update head to current node
                else:
                    # Remove the previous duplicate node by updating links
                    cur.prev.prev.next = cur     # Connect prev's prev to current
                    cur.prev = cur.prev.prev     # Connect current to prev's prev

            cur = cur.next  # Move to next node

        return head