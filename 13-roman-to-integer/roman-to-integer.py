class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = { 'I': 1, 'V': 5, 'X': 10, 'L': 50 , 'C' : 100 , 'D' : 500 , 'M': 1000}

        n = len(s)
        i = 0
        sum = 0 

        while i < n:
            if i < n-1 and pairs[s[i]] < pairs[s[i + 1]]:
                sum += pairs[s[i + 1]] - pairs[s[i]]
                i += 2
            else:
                sum += pairs[s[i]]
                i += 1
        return sum        


        