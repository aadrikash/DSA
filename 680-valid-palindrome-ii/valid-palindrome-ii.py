class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        def ispallindrome(left,right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1  

            return True

        low = 0 
        high = len(s) - 1

        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return (
                    ispallindrome(low+1,high) or 
                    ispallindrome(low,high- 1)
                )
        return True 

        