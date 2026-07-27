class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b not in d:
                d[nums[i]]=i
            else:
                return [d[b],i]