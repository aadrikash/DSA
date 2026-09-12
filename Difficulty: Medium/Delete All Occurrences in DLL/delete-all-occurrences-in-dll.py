# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, k):
        # Handle special case: single node that matches the key
        if not head.next and head.data == k:
            return None

        temp = head
        new_head = head

        while temp is not None:
            if temp.data == k:
                # Update links
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev

                # Update head if needed
                if temp == new_head:
                    new_head = temp.next
            else:
                # Only move previous when node is not deleted
                previous = temp
            temp = temp.next

        return new_head
