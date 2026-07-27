class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            s=1
            for j in range(len(nums)):
                if i==j:
                    continue
                s *=nums[j]
            res.append(s)
        return res