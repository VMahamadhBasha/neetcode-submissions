class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       from collections import Counter
       d=Counter(nums)
       for i in d.keys():
        if d[i]==1:
            return i
        
