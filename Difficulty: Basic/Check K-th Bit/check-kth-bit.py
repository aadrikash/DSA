class Solution:
    def checkKthBit(self, n, k):
        binary = bin(n)[2:]
        binary = binary[::-1]
        
        if k >= len(binary):
            return False
        
        if binary[k] == '1':
            return True
        else:
            return False
        