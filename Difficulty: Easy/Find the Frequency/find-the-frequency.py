"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        hash_map = {}
        n = len(arr)
        for num in arr:
            hash_map[num] = hash_map.get(num,0)+1
        return hash_map.get(x,0)
        # code here
        