class Solution:
    def compressedString(self, word: str) -> str:
        result = ""

        left = 0 
        while left < len(word):
            right = left 
            while right < len(word) and word[left]== word[right] and right - left < 9:
                right += 1

                count = right - left 
            result += str(count)
            result += word[left]
            left = right
            
        
        return result 
        