class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left = 0
        right = len(plants) - 1

        waterA = capacityA
        waterB = capacityB

        refills = 0

        while left < right:

            #Alice water from left

            if waterA < plants[left]:
                refills += 1
                waterA = capacityA
            waterA -= plants[left]
            left += 1


            # Bob waters from right

            if waterB < plants[right]:
                refills += 1
                waterB = capacityB

            waterB -= plants[right]
            right -= 1

            # if middle one is remaining 


            if left == right:


                if max(waterA , waterB) < plants[left]:
                    refills += 1

        
        return refills


