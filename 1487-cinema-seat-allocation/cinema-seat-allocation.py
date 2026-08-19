from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved = defaultdict(set)

        #store reserved seats row-wise
        for row,seat in reservedSeats:
            reserved[row].add(seat)
        
        #Start by assuming every row can fit 2 families
        answer = 2* n 

        #Check only rows with reserved seats

        for row in reserved:
            seats = reserved[row]

            left_free = all(seat not in seats for seat in range(2,6))
            middle_free = all(seat not in seats for seat in range(4,8))
            right_free = all(seat not in seats for seat in range(6,10))

            if left_free and right_free:
                continue
            elif left_free or middle_free or right_free:
                answer -= 1
            else:
                answer -= 2
        return answer



        