# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Queue class template
class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        # Initialize your data members

    def isEmpty(self):
        return  self.front is None
            
        # Return True if queue is empty, else False
        
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            
            self.rear.next = new_node
            self.rear = new_node
        
        self.count += 1
       
        # Add element x to the rear
        
    def dequeue(self):
        if self.front is None:
            return -1
        popped = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        self.count -= 1
        return popped
        # Remove the front element

    def getFront(self):
        if self.front is None:
            return -1
            
        return self.front.data
        # Return front element
        # return -1 if empty

    def size(self):
        return self.count
        # Return current size
