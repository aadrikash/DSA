class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for i in range(len(word)):
            
            if word[i] == ch :
                low = 0 
                high = i 
                while low < high :
                    word[low],word[high] = word[high],word[low]
                    low += 1
                    high -= 1
                break
        return ''.join(word) 

        