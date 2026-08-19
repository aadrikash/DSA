class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        

        left = 0
        while left < len(chars):
            right = left 

            while right < len(chars) and chars[left] == chars[right]:
                right += 1
            count  = right - left 

            result.append(chars[left])

            if count > 1:
                result.extend(str(count))

            left = right
        
        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
                