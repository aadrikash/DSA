class Solution:
    def findMin(self, n: int) -> int:
        coins = [10, 5, 2, 1]
        i = 0
        result = []
    
        total = n
    
        while total > 0:
            if total >= coins[i]:
                result.append(coins[i])
                total = total - coins[i]
            else:
                i += 1
    
        return len(result)