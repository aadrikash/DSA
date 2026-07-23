class myQueue:
    def __init__(self, n):
        
        self.items = []
        self.size = n
        
        # Define Data Structures

    
    def isEmpty(self):
        return len(self.items) == 0
        # Check if queue is empty

    
    def isFull(self):
        return len(self.items) == self.size
        
        # Check if queue is full

    
    def enqueue(self, x):
        self.items.append(x)
        # Enqueue

    
    def dequeue(self):
        if len(self.items) ==  0 :
            
            return -1
        x = self.items.pop(0)
        return x 
        # Dequeue

    
    def getFront(self):
        if len(self.items) == 0:
            
            return -1
        return self.items[0]
        # Get front element
       
    
    def getRear(self):
        if len(self.items) == 0:
            return  -1
        
        return self.items[-1]
        # Get rear element 
        
        