class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[0]*n
        r=[0]*n
        left,right=1,1
        for i in range(n):
            l[i] =left
            left*=nums[i]
        for i in range(n-1,-1,-1):
            r[i]=right
            right *=nums[i]
        for i in range(n):
            l[i] *=r[i]
        return l