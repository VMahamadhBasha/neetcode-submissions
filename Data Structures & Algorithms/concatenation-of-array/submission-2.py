class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums)):
        #     res.append(nums[i])
        # for i in range(len(nums)):
        #     res.append(nums[i])
        # return res
        n=len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums