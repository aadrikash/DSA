# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, nodes):
        n = len(nodes)
        
        if n == 0 :
            return None
            
        nodes = [Node(x) for x in nodes]
        
        for i in range(n):
            left = 2*i + 1
            right = 2*i + 2
            if left < n :
                nodes[i].left  = nodes[left]
            if right < n :
                nodes[i].right = nodes[right]
        return nodes[0]
    # code here
        