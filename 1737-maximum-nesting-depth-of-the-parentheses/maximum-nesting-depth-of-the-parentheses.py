class Solution:
    def maxDepth(self, s: str) -> int:

        count = 0
        maxi = 0
        
        for ch in s:
            if ch == "(":
                count += 1
                maxi = max(count,maxi)

            
            elif ch == ")":
                count -= 1
    
        return maxi 
                