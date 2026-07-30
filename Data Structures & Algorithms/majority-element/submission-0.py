class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        d=Counter(nums)
        n=len(nums)
        if(n%2!=0):
            n=n//2+1
        else:
            n=n//2
        for i in d.keys():
            if d[i]>=n:
                return i
        