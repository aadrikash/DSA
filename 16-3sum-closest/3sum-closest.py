class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0 
        closest_sum = float("inf")


        for i in range(len(nums)):


            j = i+1
            k = len(nums) - 1

            while j < k :

                curr_sum = nums[i] + nums[j] + nums[k]

                if (abs(target - curr_sum)) < (abs(target - closest_sum)):
                    closest_sum = curr_sum
                
                elif curr_sum < target :
                    j += 1
                
                elif curr_sum > target :
                    k -= 1
                else:
                    return curr_sum

                
        return closest_sum
        