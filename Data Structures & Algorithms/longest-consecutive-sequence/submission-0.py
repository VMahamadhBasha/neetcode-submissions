class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=0
        s=set(nums)
        for i in nums:
            if i-1 not in s:
                j,k=1,1
                while i+j in s:
                    k+=1
                    j+=1
                c=max(c,k)
        return c
