class myStack:
    def __init__(self, n):
        self.items = []
        self.size = n   # maximum capacity

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.size

    def push(self, x):
        if self.isFull():
            return  # do nothing if full
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.items[-1]
