class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_position = len(nums) - 1


        for idx in range(len(nums) - 2 , -1 ,-1 ):

            if idx + nums[idx] >= final_position:
                final_position = idx

        return final_position == 0 
        