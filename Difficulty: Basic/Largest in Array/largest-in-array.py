class Solution:
    def largest(self, arr):
        # code here
        n = len(arr)
        largest = float("-inf")
        for i in range(0,n):
            largest = max(largest,arr[i])
        return largest 