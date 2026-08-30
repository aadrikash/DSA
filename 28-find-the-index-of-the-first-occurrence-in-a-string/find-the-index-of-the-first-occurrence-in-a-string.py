class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        i = 0
        while i <= n - m :
            j = 0

            while j < m :
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == m :
                return i 

            i += 1

        return -1 
        