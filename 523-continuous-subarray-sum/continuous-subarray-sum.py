class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #first index where it appeared  
        remainder = { 0 : -1}
        total = 0

        for i in range(len(nums)):
            #add current element to prefix sum 
            total += nums[i]
            #we only care about the remainder 
            rem = total % k 

            #same remainder seen before 
            if rem in remainder:
                # subarray check for more than two values
                if i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i 
        return False






            