from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the position of the next non-val element
        k = 0  
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
