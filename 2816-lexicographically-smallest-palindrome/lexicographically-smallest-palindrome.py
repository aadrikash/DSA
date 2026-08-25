class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)

        low = 0 
        high = len(s) -1 
        
        while low < high:
            smallest = min(s[low], s[high])

            s[low] = smallest
            s[high]= smallest

            low += 1
            high -= 1

        return ''.join(s)    