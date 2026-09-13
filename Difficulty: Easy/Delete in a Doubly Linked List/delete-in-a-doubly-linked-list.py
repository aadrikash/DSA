""" Structure of a Doubly Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        curr = head
        
        for i in range(1,x):
            curr = curr.next
        
        if curr.prev is None:
            head = curr.next
            
            if head is not None:
                head.prev = None
            
            return head
            
        
        curr.prev.next = curr.next
        
        if curr.next is not None:
            curr.next.prev = curr.prev
            
        return head 
        
        