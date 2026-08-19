
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        equal = []

        for num in nums :
            if num == pivot:
                equal.append(num)
            elif num < pivot:
                less.append(num)
            else:
                more.append(num)
        return less + equal + more

'''
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        # Smaller elements
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1

        # Greater elements
        for num in reversed(nums):
            if num > pivot:
                result[right] = num
                right -= 1

        # Fill remaining positions with pivot
        while left <= right:
            result[left] = pivot
            left += 1

        return result

'''