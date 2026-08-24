class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        s = list(s)
        n = len(s)

        low = 0
        high = n-1
        while low <= high:
            if s[low] not in vowel:
                low += 1
            elif s[high] not in vowel:
                high -= 1
            else:
                s[low], s[high] = s[high] , s[low]
                low += 1
                high -= 1
                
            
        
        return ''.join(s)
        